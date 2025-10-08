from py4godot.classes import gdclass
from py4godot.classes.Control import Control

@gdclass
class combat_scene(Control):
	def _on_attack_pressed(self):
		print("test")
