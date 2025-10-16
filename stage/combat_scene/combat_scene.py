from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from py4godot.classes.Label import Label
from ..charactor import Globals
from ..maingame import maingame
from ..random_events import random_event_picker
from .monster import Monster
from py4godot.classes import Input

@gdclass
class combat_scene(Control):
	def _ready(self) -> None:
		self.get_node("Attack_Button").disabled = False
		self.get_node("Flee_Button").disabled = False
		self.get_node("dead_screen").visible = False
		self.get_node("Textbox").visible = False

		# Get a reference to the label node
		self.hp_label = self.get_node("HP_monster")

		# Randomly pick monster from available pool and create an instance
		selected_encounter = self.pick_monster()
		self.monster = Monster().setup_monster(selected_encounter)

		# Update the label with the initial HP values
		self.hp_label.call("update_hp", self.monster.hp, self.monster.max_hp)

	def player_died(self):
		'''call this function when player is dead'''
		self.get_node("Attack_Button").disabled = True
		self.get_node("Flee_Button").disabled = True
		self.get_node("dead_screen").visible = True

	def pick_monster(self):
		'''picking random monster and display on screen'''
		# Picking which monster encounter
		selected_encounter = random_event_picker.pick_random_encounter()
		print(f"Encountering: {selected_encounter}")	# Debug
		return selected_encounter

	def _on_attack_button_pressed(self) -> None:
		# Player attacks monster
		self.monster.take_damage(Globals.strength)
		# Add Textbox here to use as swich turn
		self.get_node("Textbox").visible = True
		def _input(self, event):
			if event.is_action_pressed("ui_accept"):
				print("Text")
				self.get_node("Textbox").visible = False

		# Update the label with the new HP values
		self.hp_label.call("update_hp", self.monster.hp, self.monster.max_hp)

		if self.monster.is_dead:
			print("Monster Defeated")
			print(f"You gained {self.monster.exp_reward} EXP!!!")
			Globals.room += 1
			Globals.gain_exp(self.monster.exp_reward) # Gained EXP after defeating monster
			# Status report will always trigger after returning to maingame (stage1.tscn) :)
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
		else:
			# Monster is not dead, it's their turn to attack! (We can add this logic here)
			print("Monster Attack!")

	def _on_flee_button_pressed(self):
		remain_hp = Globals.flee_penalty()
		print(f"Debug player hp: {remain_hp}")
		if remain_hp <= 0:
			print("died")
			self.player_died()      # call function above when player is dead
			### Maybe call result scence here?
		else:
			# Player survived, return to main stage
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

	def _on_died_back_to_menu_pressed(self):
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")


	def _on_textbox_hidden(self):
		pass
