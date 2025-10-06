from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from .charactor import Globals

@gdclass
class maingame(Control):
	def _ready(self):
		self.get_node("dead_panel").visible = False
		Globals.init_character()
		print(f"Level: {Globals.level}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")

	def _on_skip_pressed(self):
		print("skip")
		#check difficult
		print(Globals.difficult)

	def _on_next_pressed(self):
		print("next")
		Globals.gain_exp(50)
		print(f"Level: {Globals.level}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")

	def _on_back_button_pressed(self):
		print("Back")
		self.get_tree().change_scene_to_file("res://main_menu.tscn")

	def _on_died_back_to_menu_pressed(self):
		self.get_tree().change_scene_to_file("res://main_menu.tscn")


	def _on_flee_button_pressed(self):
		print("skip")
		remain_hp = Globals.skip_penalty()
		print(remain_hp)
		if remain_hp < 0:
			print("died")
			self.get_node("dead_panel").visible = True
