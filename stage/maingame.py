from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from .charactor import Globals
from .random_events import random_event_picker
from .save_reload import save_game


@gdclass
class maingame(Control):
	"""Controls the main game screen, where the player progresses through rooms."""
	def _ready(self):
		'''
		Called when the node is 'ready'. Initializes the game state.
		'''
		self.get_node("Back_Button").disabled = False
		self.get_node("Next_Button").disabled = False
		self.get_node("Return_Button").disabled = False
		# Initialize a new game/character if one doesn't already exist.
		if Globals.player is None:
			Globals.new_game()
		self.save = save_game()
		self.status_update()

	def _input(self, event):
		"""
		Handles global input events for the main game screen.
		- 'Press_B': Opens the backpack scene.
		- 'Press_X': Returns to the main menu.
		"""
		# Check if the 'Press_B' action is pressed (mapped to 'B' key in Project Settings)
		if event.is_action_pressed("Press_B"):
			print("Debug: 'B' key pressed, chaning to backpack scene")
			Globals.previous_scene_path = "res://stage/stage1.tscn"
			self.get_tree().change_scene_to_file("res://stage/backpack_scene/backpack_scene.tscn")
		if event.is_action_pressed("Press_X"):
			print("Debug: 'X' key pressed, returning to title")
			self._on_back_button_pressed()		# Basically the same as pressing the back button itself.

	def status_update(self):
		"""Prints the player's current status to the console for debugging."""
		print("\n-------------------------------------")
		print(f"Level: {Globals.player.level}")
		print(f"HP: {Globals.player.actual_hp}/{Globals.player.max_hp}")
		print(f"EXP: {Globals.player.exp}/{Globals.player.exp_req}")
		print(f"Total EXP: {Globals.player.exp_total}")
		print("-------------------------------------\n")

	# Possibly the heart of the game sit here in this function
	def _on_next_pressed(self):
		"""
		Handles the 'Next' button press.
		Picks a random event and transitions to the appropriate scene.
		"""
		print("next")
		selected_event = random_event_picker.pick_random_event()
		print(selected_event)       # Debug
		match selected_event:
			case 'monster_encounter':
				# Change to combat scene
				print('monster')
				self.get_tree().change_scene_to_file("res://stage/combat_scene/combat_scene.tscn")
			case 'treasure_chest':
				print('treasure')
				# Change scene to tresure chest
				self.get_tree().change_scene_to_file("res://stage/treasure_scene/treasure_scene.tscn")
			case 'rest_stop':
				print('rest_stop')
				# Change scene to rest stop

		# Only execute this block if the scene did NOT change
		### --- Debug ---
		Globals.player.gain_exp(amount=10) # Assuming you gain EXP from non-combat events
		self.status_update() # Prints the HP *after* the non-combat event
		### --- Debug ---

	# Idk reuturn to the begining or maybe rest stop and rest ig
	def _on_return_button_pressed(self):
		"""Placeholder for a 'Return' or 'Rest' action. Currently does nothing."""
		print("return")

		### Residue code block (Awaiting delete) ###
	def _on_skip_pressed(self):
		"""Legacy/debug function. Prints the current difficulty."""
		print("skip")
		#check difficult
		print(Globals.difficulty)
		### Residue code block (Awaiting delete) ###

	def _on_back_button_pressed(self):
		"""Saves the game and returns to the main menu."""
		print("Back")
		print("Debug: Progress automatically saved!")
		Globals.previous_scene_path = "res://stage/stage1.tscn"
		self.save.save(character=Globals.player)
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")
