from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from ..random_events import random_event_picker
from ..charactor import Globals

@gdclass
class treasure(Control):
	def _on_chest_pressed(self):
		pass

	def _on_debug_back_pressed(self):
		print(f"DEBUG: Debug back")
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
