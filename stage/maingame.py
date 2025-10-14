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
		self.get_node("Return_Button").disabled = False
		# ONLY initialize if the character hasn't been set up yet (a simple check)
		if Globals.max_hp is None:
			Globals.init_character()
		self.status_update()

	def status_update(self):
		'''for unify debuging purpose'''
		print(f"Level: {Globals.level}")
		print(f"HP: {Globals.actual_hp}/{Globals.max_hp}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")

	# Possibly the heart of the game sit here in this function
	def _on_next_pressed(self):
		print("next")
		selected_event = random_event_picker.pick_random_event()
		print(selected_event)       # Debug
		match selected_event:
			case 'monster_encounter':
				# Still need monster randomization
				print('monster')
				self.get_tree().change_scene_to_file("res://stage/combat_scene/combat_scene.tscn")
			case 'treasure_chest':
				print('treasure')
				# Change scene to tresure chest
			case 'rest_stop':
				print('rest_stop')
				# Change scene to rest stop

		# Only execute this block if the scene did NOT change
		### --- Debug ---
		Globals.gain_exp(50) # Assuming you gain EXP from non-combat events
		self.status_update() # Prints the HP *after* the non-combat event
		### --- Debug ---

	# Idk reuturn to the begining or maybe rest stop and rest ig
	def _on_return_button_pressed(self):
		print("return")

		### Residue code block (Awaiting delete) ###
	def _on_skip_pressed(self):
		print("skip")
		#check difficult
		print(Globals.difficult)
		### Residue code block (Awaiting delete) ###

	def _on_back_button_pressed(self):
		print("Back")
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")
