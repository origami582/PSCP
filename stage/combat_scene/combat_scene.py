from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from py4godot.classes.Label import Label
from py4godot.classes import Input
from ..charactor import Globals
from ..maingame import maingame
from ..random_events import random_event_picker
from .monster import Monster

@gdclass
class combat_scene(Control):
	"""Manages the combat sequence between the player and a monster."""
	def _ready(self) -> None:
		"""Initializes the combat scene by setting up UI and spawning a monster."""
		self.get_node("Attack_Button").disabled = False # type: ignore
		self.get_node("Flee_Button").disabled = False
		self.get_node("Textbox").visible = False


		# Get a reference to the label node
		self.monster_hp_label = self.get_node("HP_monster")
		self.monster_bar = self.get_node("Monster_bar")
		self.player_hp_label = self.get_node("HP_player")
		self.player_bar = self.get_node("Player_bar")
		self.monster_node = self.get_node("Monster")
		self.textbox_node = self.get_node("Textbox")

		# Randomly pick monster from available pool and create an instance
		selected_encounter = self.pick_monster()
		if Globals.room == 9:
			# Setup boss instead of normal monster
			self.monster = Monster().setup_boss(boss_type=selected_encounter)
			# --- Dynamic Music Logic ---
			if selected_encounter == "Roland":
				self.get_node("/root/AudioPlayer").call("play_music", "Roland2")
			else:
				# Default boss music
				self.get_node("/root/AudioPlayer").call("play_music", "Boss2")
		else:
			# Setup normal monster
			self.monster = Monster().setup_monster(monster_type=selected_encounter)
			# Play normal battle music
			self.get_node("/root/AudioPlayer").call("play_music", "Mirage")

		# Set monster texture after setup
		self.monster_texture = self.monster.texture_path

		# Change monster texture here
		self.monster_node.call("update_texture", self.monster_texture)


		# Update the label with the initial HP values
		self.monster_hp_label.call("update_hp", self.monster.hp, self.monster.max_hp)
		self.monster_bar.call("update_monster_bar", self.monster.hp, self.monster.max_hp)
		self.player_hp_label.call("update_hp", Globals.player.actual_hp, Globals.player.max_hp)
		self.player_bar.call("update_player_bar", Globals.player.actual_hp, Globals.player.max_hp)


	def player_died(self):
		"""Disables combat buttons and shows the death screen."""
		Globals.player.lifes -= 1
		Globals.player.actual_hp = Globals.player.max_hp
		print("DEBUG: Player died - Live reducted by 1")
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

	def pick_monster(self):
		"""Picks a random monster from the encounter pool."""
		# Picking which monster encounter
		if Globals.room == 9:
			selected_encounter = random_event_picker.pick_random_boss()
		else:
			selected_encounter = random_event_picker.pick_random_encounter()
		print(f"Encountering: {selected_encounter}")	# Debug
		return selected_encounter

	def _on_attack_button_pressed(self) -> None:
		"""Handles the event when the player's attack button is pressed."""
		# Get the textbox and its label, then update the text
		self.textbox_node.visible = True
		self.textbox_node.get_node("Text").call("clear_text")

		# Player attacks monster
		dice_face = random_event_picker.dice_roll()
		self.textbox_node.get_node("Text").call("show_dice_roll", dice_face)
		player_damage = Globals.player.strength * dice_face
		print(f"Dice roll: {dice_face}, Damage: {player_damage}")  # Debug
		self.monster.take_damage(amount=player_damage)
		self.get_node("Attack_Button").visible = False
		self.get_node("Flee_Button").visible = False
		self.textbox_node.get_node("Text").call("show_player_attack",
										   self.monster.monster_type,
										   player_damage)
		monster_node = self.get_node("Monster")
		if monster_node:
			monster_anim_player = monster_node.get_node("Monster_AnimationPlayer")
			if monster_anim_player:
				monster_anim_player.play("hit_flash")

		if self.monster.is_dead:
			# Special check for Roland's second phase
			if self.monster.monster_type == "Roland":
				self.textbox_node.get_node("Text").call("clear_text")
				self.textbox_node.get_node("Text").call("show_roland_transform")

				# Change the music for the second phase!
				self.get_node("/root/AudioPlayer").call("play_music", "GoneAngels")

				# Transform into The_Black_Silence
				self.monster = Monster().setup_boss(boss_type="The_Black_Silence")
				self.monster_node.call("update_texture", self.monster.texture_path)

				# Update UI for the new phase and allow the player to act again
				self.update_ui_elements()
				# We don't set wait_for_next_scene, the textbox will clear on the next 'ui_accept'
				return

			# Monster is dead, show victory message and wait for player to continue.
			self.textbox_node.get_node("Text").call("show_monster_dead",
											   self.monster.monster_type,
											   self.monster.exp_reward)
			self.wait_for_next_scene = True
			# Update HP bars and return to prevent monster from attacking.
			self.update_ui_elements()
			return

		# Monster attacks player, if it's still alive
		monster_damage = self.monster.atk
		Globals.player.actual_hp -= monster_damage
		self.textbox_node.get_node("Text").call("show_monster_attack",
										   self.monster.monster_type,
										   monster_damage)
		#animationformc
		# Check if player died from the counter-attack
		if Globals.player.actual_hp <= 0:
			self.player_died()
			return # Stop further execution if player is defeated

		self.update_ui_elements()

	def _on_flee_button_pressed(self):
		"""Handles the event when the flee button is pressed."""
		remain_hp = Globals.player.flee_penalty()
		self.get_node("Attack_Button").visible = False
		self.get_node("Flee_Button").visible = False
		self.wait_for_next_scene = True
		self.textbox_node.visible = True
		self.textbox_node.get_node("Text").call("clear_text")

		print(f"Debug player hp: {remain_hp}")
		if remain_hp <= 0:
			self.textbox_node.get_node("Text").call("show_flee", True, self.monster.monster_type, 0)
			print("died")
			# We will wait for input before calling player_died()
		else:
			penalty = Globals.player.get_penalty()
			# Player survived, return to stage1
			self.textbox_node.get_node("Text").call("show_flee", False, self.monster.monster_type, penalty)
			# We will wait for input before changing the scene

	def update_ui_elements(self):
		"""Updates all HP-related UI elements."""
		self.monster_hp_label.call("update_hp", self.monster.hp, self.monster.max_hp)
		self.monster_bar.call("update_monster_bar", self.monster.hp, self.monster.max_hp)
		self.player_hp_label.call("update_hp", Globals.player.actual_hp, Globals.player.max_hp)
		self.player_bar.call("update_player_bar", Globals.player.actual_hp, Globals.player.max_hp)

	def _input(self, event):
		"""Handles player input for advancing dialogue in the textbox."""
		if hasattr(self, "wait_for_next_scene") and self.wait_for_next_scene:
			if event.is_action_pressed("ui_accept"):
				self.wait_for_next_scene = False
				if self.monster.is_dead:
					print("Monster Defeated")
					print(f"You gained {self.monster.exp_reward} EXP!!!")
					Globals.room += 1
					Globals.player.gain_exp(amount=self.monster.exp_reward)
					self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
				elif Globals.player.actual_hp <= 0: # Died from fleeing
					self.player_died()
				else: # Fled successfully
					self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

			return
		if event.is_action_pressed("ui_accept"):
			self.get_node("Textbox").visible = False
			self.get_node("Attack_Button").visible = True
			self.get_node("Flee_Button").visible = True
