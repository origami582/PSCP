from py4godot.classes import gdclass
from py4godot.classes.Control import Control

@gdclass
class main(Control):
	# popup close
	def _ready(self):
		#ready game this pop up close
		self.get_node("CanvasLayer").visible = False
	def _on_newgame_pressed(self):
		#open popup
		self.get_node("CanvasLayer").visible = True

	def _on_Continew_pressed(self):
		#pass
		print("Continue")

	def _on_lederbord_pressed(self):
		#pass
		print("Leaderboard")

	def _on_closepop_pressed(self):
		#close popup
		self.get_node("CanvasLayer").visible = False

	#exitgame
	def _on_exitgame_pressed(self):
		self.get_tree().quit()

	#Level
	def _on_easy_pressed(self):
		pass
	#Level
	def _on_medium_pressed(self):
		pass

	#Level
	def _on_hard_pressed(self):
		pass
