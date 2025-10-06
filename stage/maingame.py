from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from ..main import main
@gdclass
class maingame(Control):

	def _on_skip_pressed(self):
		print("skip")


	def _on_next_pressed(self):
		print("next")
