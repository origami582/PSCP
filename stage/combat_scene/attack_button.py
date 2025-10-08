from py4godot.classes import gdclass
from py4godot.classes.Control import Control

@gdclass
class Attack(Control):
	

	def _on_pressed(self):
		print("Hello")
