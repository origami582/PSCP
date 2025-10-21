from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from ..charactor import Globals

@gdclass
class backpack_scene(Control):
	def _input(self, event):
		# Check if the 'Press_B' action is pressed (mapped to 'B' key in Project Settings)
		if event.is_action_pressed("Press_B"):
			print(f"Debug: 'B' key pressed, changing back to {Globals.previous_scene_path}")
			if Globals.previous_scene_path:
				self.get_tree().change_scene_to_file(Globals.previous_scene_path)
