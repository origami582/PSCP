from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from ..charactor import Globals
from ..save_reload import save_game

@gdclass
class treasure(Control):
	wait_for_next_scene:bool = False
	def _ready(self):
		# Get the global music player and tell it to play the battle music.
		self.get_node("/root/AudioPlayer").call("play_music", "Fun")

		self.get_node("Textbox").visible = True
		self.get_node("Textbox").get_node("Text").call("clear_text")
		self.get_node("Textbox").get_node("Text").call("show_chest_room")
		self.wait_for_next_scene = True

		self.chest_openned = False
		self.save = save_game()
		self.player = Globals.player
		Globals.previous_scene_path = "res://stage/treasure_scene/treasure_scene.tscn"

	def _on_chest_pressed(self):
		self.get_node("Textbox").visible = True
		self.get_node("Textbox").get_node("Text").call("clear_text")
		self.get_node("Textbox").get_node("Text").call("show_chest")
		self.wait_for_next_scene = True

		self.chest_openned = True

	def _input(self, event):
		"""Handles player input for advancing dialogue in the textbox."""
		if self.wait_for_next_scene and event.is_action_pressed("ui_accept"):
			self.get_node("Textbox").visible = False
			self.wait_for_next_scene = False
			if self.chest_openned:
				Globals.room += 1
				self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

	def _on_back_button_pressed(self):
		"""Save the game and return to the main menu."""
		self.save.save(character=self.player)
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")
