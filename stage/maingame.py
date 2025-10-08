from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from .charactor import Globals
from .random_events import random_event_picker


@gdclass
class maingame(Control):
	def _ready(self):
		'''
		Game init
		'''
		self.get_node("Back_Button").disabled = False
		self.get_node("Next_Button").disabled = False
		self.get_node("Flee_Button").disabled = False
		self.get_node("Battle_Button").visible = False
		self.get_node("Flee_Button").visible = True
		self.get_node("Next_Button").visible = True
		self.get_node("Monster_control").visible = False
		self.get_node("dead_panel").visible = False
		Globals.init_character()
		print(f"Level: {Globals.level}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")

	# Possibly the heart of the game sit here in this function
	def _on_next_pressed(self):
		print("next")
		events = {
			# Event structure is:
			# 'Event name' : probability(int, float)
			"monster_encounter": 60,
			"treasure_chest": 30,
			"rest_stop": 10
			# Add more events here
		}
		selected_event = random_event_picker.pick_random_event(events)
		print(selected_event)		# Debug
		match selected_event:
			case 'monster_encounter':
				# Still need monster randomization
				print('monster')
				self.get_node("Flee_Button").visible = False
				self.get_node("Next_Button").visible = False
				self.get_node("Battle_Button").visible = True
				self.get_node("Monster_control").visible = True
			case 'treasure_chest':
				print('treasure')
			case 'rest_stop':
				print('rest_stop')
		
		### --- Debug ---
		Globals.gain_exp(50)
		print(f"Level: {Globals.level}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")
		### --- Debug ---
	
	# Passing enemy HP logic to someone else in the team
	def _on_battle_button_pressed(self):
		# For now it will be one-hit kill for all enemies
		print("attack")
		self.get_tree().change_scene_to_file("res://stage/combat_scene/combat_scene.tscn")
		self.get_node("Battle_Button").visible = False
		self.get_node("Flee_Button").visible = True
		self.get_node("Next_Button").visible = True
		self.get_node("Monster_control").visible = False
		
		
	def _on_flee_button_pressed(self):
		print("skip")
		remain_hp = Globals.skip_penalty()
		print(remain_hp)
		if remain_hp < 0:
			print("died")
			self.get_node("Back_Button").disabled = True
			self.get_node("Next_Button").disabled = True
			self.get_node("Flee_Button").disabled = True
			self.get_node("dead_panel").visible = True

		### Residue code block (Awaiting delete) ###
	def _on_skip_pressed(self):
		print("skip")
		#check difficult
		print(Globals.difficult)
		### Residue code block (Awaiting delete) ###

	def _on_back_button_pressed(self):
		print("Back")
		self.get_tree().change_scene_to_file("res://main_menu.tscn")

	def _on_died_back_to_menu_pressed(self):
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")
