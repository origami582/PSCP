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
		self.get_node("Setting").visible = False 
		#music 
		self.music = self.get_node("AudioStreamPlayer")

	def _on_newgame_pressed(self):
		#open popup
		self.get_node("Level_select").visible = True
		Globals.hp = 100
		strength = 10
		
	def _on_Continew_pressed(self):
		#pass
		print("Continue")

	def _on_lederbord_pressed(self):
		#pass
		self.get_node("Setting").visible = True

	def _on_closepop_pressed(self):
		#close popup
		self.get_node("Level_select").visible = False 

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

	def _on_music_changed(self, value: float):
		db_value = -80 + value 
		self.music.volume_db = db_value

	def _on_continew_pressed(self):
		self.get_node("Setting").visible = False
