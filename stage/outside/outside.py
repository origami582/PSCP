from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from ..charactor import Globals
from ..save_reload import save_game

@gdclass
class outside(Control):
	wait_for_next_scene = False
	next_scene_path = ""
	def _ready(self):
		# Get the global music player and tell it to play the battle music.
		self.get_node("/root/AudioPlayer").call("play_music", "Coo")

		self.get_node("Back_Button").disabled = False
		self.get_node("Next_Button").disabled = False

		self.player = Globals.player
		self.save = save_game()

		Globals.floor = 0
		Globals.room = 0


	def _input(self, event):
		"""Handles player input for advancing dialogue in the textbox."""
		if self.wait_for_next_scene and event.is_action_pressed("ui_accept"):
			self.get_node("Textbox").visible = False
			self.wait_for_next_scene = False
			if self.next_scene_path:
				self.get_tree().change_scene_to_file(self.next_scene_path)

	def _on_back_button_pressed(self):
		"""Saves the game and returns to the main menu."""
		print("Back")
		print("Debug: Progress automatically saved!")
		Globals.previous_scene_path = "res://stage/outside/outside.tscn"
		self.save.save(character=self.player)
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")

	def _on_next_button_pressed(self):
		"Enter stage1"
		Globals.floor = 1
		Globals.room = 1
		if Globals.is_returning_outside:
			self.player.lifes = 3       # Reset live count
			self.player.actual_hp = self.player.max_hp      # Reset HP
			self.get_node("Textbox").visible = True
			self.get_node("Textbox").get_node("Text").call("clear_text")
			self.get_node("Textbox").get_node("Text").call("show_enter")
			self.wait_for_next_scene = True
			Globals.is_returning_outside = False
			self.next_scene_path = "res://stage/stage1.tscn"
		else:
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
