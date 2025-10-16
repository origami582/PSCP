from py4godot.classes import gdclass
from py4godot.classes.Control import Control

@gdclass
class tresure(Control):
	
	def _on_button_pressed(self):
		print("You received items")
