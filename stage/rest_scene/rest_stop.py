from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from ..charactor import Globals
from..save_reload import save_game


@gdclass
class rest_stop(Control):
	wait_for_next_scene = False
	def _ready(self):
		self.get_node("Textbox").visible = True
		self.get_node("Textbox").get_node("Text").call("clear_text")
		self.get_node("Textbox").get_node("Text").call("show_rest", 'enter')
		self.wait_for_next_scene = True

		self.forward = False
		self.save = save_game()
		self.player = Globals.player
		Globals.previous_scene_path = "res://stage/rest_scene/rest_stop.tscn"
		self.live_counter = self.get_node("Lives")

	def _process(self, delta):
		self.live_counter.call("update_display", Globals.player.lifes)

	def _input(self, event):
		"""Handles player input for advancing dialogue in the textbox."""
		if self.wait_for_next_scene and event.is_action_pressed("ui_accept"):
			self.wait_for_next_scene = False
			self.get_node("Textbox").visible = False
			if self.forward:
				Globals.room += 1
				Globals.player.actual_hp = Globals.player.max_hp
				Globals.player.lifes += 1
				self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

	def _on_back_button_pressed(self):
		"""Save the game and return to the main menu."""
		self.save.save(character=self.player)
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")

	def _on_next_button_pressed(self):
		self.get_node("Textbox").visible = True
		self.get_node("Textbox").get_node("Text").call("clear_text")
		self.get_node("Textbox").get_node("Text").call("show_rest", 'leave')
		self.wait_for_next_scene = True

		self.forward = True
