from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from py4godot.classes.Label import Label
from ..charactor import Character, Globals
from ..maingame import maingame
from ..random_events import random_event_picker
from .monster import Monster
from py4godot.classes import Input

@gdclass
class combat_scene(Control):
	"""Manages the combat sequence between the player and a monster."""
	def _ready(self) -> None:
		"""Initializes the combat scene by setting up UI and spawning a monster."""
		self.get_node("Attack_Button").disabled = False # type: ignore
		self.get_node("Flee_Button").disabled = False
		self.get_node("dead_screen").visible = False
		self.get_node("Textbox").visible = False

		# Get a reference to the label node
		self.hp_label = self.get_node("HP_monster")
		self.monster_bar = self.get_node("Monster_bar")

		# Randomly pick monster from available pool and create an instance
		selected_encounter = self.pick_monster()
		self.monster = Monster().setup_monster(monster_type=selected_encounter)
		# Update the label with the initial HP values
		self.hp_label.call("update_hp", self.monster.hp, self.monster.max_hp)
		self.monster_bar.call("update_monster_bar", self.monster.hp, self.monster.max_hp)
	def player_died(self):
		"""Disables combat buttons and shows the death screen."""
		# self.get_node("Attack_Button").disabled = True
		# self.get_node("Flee_Button").disabled = True
		# self.get_node("dead_screen").visible = True
		# Globals.player_lives -= 1 # minus player lives
		# print(f"Player died! Lives remaining: {Globals.player_lives}") #debug
		# if Globals.player_lives > 0:
		# 	print("You Lose the fight but stand up again...")
		# else :
		# 	print("You are Wiped")

		Globals.player.lifes -= 1
		Globals.player.actual_hp = Globals.player.max_hp
		print("DEBUG: Player died - Live reducted by 1")
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

	def pick_monster(self):
		"""Picks a random monster from the encounter pool."""
		# Picking which monster encounter
		selected_encounter = random_event_picker.pick_random_encounter()
		print(f"Encountering: {selected_encounter}")	# Debug
		return selected_encounter

	def _on_attack_button_pressed(self) -> None:
		"""Handles the event when the player's attack button is pressed."""
		# Player attacks monster
		self.monster.take_damage(amount=Globals.player.strength)
		self.get_node("Attack_Button").visible = False
		self.get_node("Flee_Button").visible = False

		# Get the textbox and its label, then update the text
		textbox_node = self.get_node("Textbox")
		if self.monster.is_dead:
			textbox_node.get_node("Text").call("show_monster_dead",\
											  self.monster.monster_type,\
												self.monster.exp_reward)
			textbox_node.visible = True
			self.wait_for_next_scene = True 
			
		else:
			textbox_node.get_node("Text").call("show_player_attack",\
											  self.monster.monster_type,\
												Globals.player.strength)
			textbox_node.visible = True

		# Update the label with the new HP values
		self.hp_label.call("update_hp", self.monster.hp, self.monster.max_hp)


	def _on_flee_button_pressed(self):
		"""Handles the event when the flee button is pressed."""
		remain_hp = Globals.player.flee_penalty()
		print(f"Debug player hp: {remain_hp}")
		if remain_hp <= 0:
			print("died")
			self.player_died()      # call function above when player is dead
			if Globals.player.lifes <= 0:
				self.get_node("dead_screen").visible = True
				self.get_node("Textbox").visible = False
				self.get_node("Attack_Button").visible = False
		else:
			# Player survived, return to stage1
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")


	def _on_died_back_to_menu_pressed(self):
		"""Handles returning to the main menu from the death screen."""
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")

	def _input(self, event):
		"""Handles player input for advancing dialogue in the textbox."""
		if hasattr(self, "wait_for_next_scene") and self.wait_for_next_scene:
			if event.is_action_pressed("ui_accept"):
				self.wait_for_next_scene = False
				print("Monster Defeated")
				print(f"You gained {self.monster.exp_reward} EXP!!!")
				Globals.room += 1
				Globals.player.gain_exp(amount=self.monster.exp_reward)
				self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
			return
		if event.is_action_pressed("ui_accept"):
			self.get_node("Textbox").visible = False
			self.get_node("Attack_Button").visible = True
			self.get_node("Flee_Button").visible = True

		# Check if the 'Press_B' action is pressed (mapped to 'B' key in Project Settings)
		if event.is_action_pressed("Press_B"):
			print("Debug: 'B' key pressed, chaning to backpack scene")
			Globals.previous_scene_path = "res://stage/combat_scene/combat_scene.tscn"
			self.get_tree().change_scene_to_file("res://stage/backpack_scene/backpack_scene.tscn")

	def _on_textbox_hidden(self):
		"""Callback for when the textbox is hidden (currently unused)."""
		pass
