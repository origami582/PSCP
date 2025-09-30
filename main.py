from py4godot.classes import gdclass
from py4godot.classes.Control import Control

@gdclass
class main(Control):

	def _on_newgame_pressed(self):
		self.get_tree().change_scene_to_file("stage\\stage1.tscn")

	def _on_Continew_pressed(self):
		print("Continue")

	def _on_lederbord_pressed(self):
		print("Leaderboard")
	def _on_exit_pressed(self):
		 ### exit
		self.get_tree().quit()
