from py4godot.classes import gdclass
from py4godot.classes.Control import Control

@gdclass
class treasure(Control):
	def _on_chest_pressed(self):
		print(f"You received items")
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
