from py4godot.classes import gdclass
from py4godot.classes.Control import Control
#Connect files to charactor
from stage.charactor import Globals

@gdclass
class main(Control):
	# popup close
	def _ready(self):
		#ready game this pop up close
		self.get_node("CanvasLayer").visible = False

	def _on_newgame_pressed(self):
		#open popup
		self.get_node("CanvasLayer").visible = True
		Globals.hp = 100
		strength = 10
		
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

	#difficult select and var to scale with exp_gain and monster status 
	def _on_easy_pressed(self):
		#add Globals. forward
		Globals.difficult = 1
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
	def _on_medium_pressed(self):
		#add Globals. forward
		Globals.difficult = 1.5
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
	def _on_hard_pressed(self):
		#add Globals. forward
		Globals.difficult = 2
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
