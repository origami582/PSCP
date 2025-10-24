from py4godot.classes import gdclass
from py4godot.classes.Control import Control
#Connect files to charactor
from stage.charactor import Globals
from stage.save_reload import load_game


@gdclass
class main(Control):
	def __init__(self):
		# Don't forget to call the parent class's constructor!
		super().__init__()
		self.reload = load_game()

	def _ready(self):
		#ready game this pop up close
		self.get_node("CanvasLayer").visible = False
		self.get_node("Setting").visible = False
		#music
		self.music = self.get_node("AudioStreamPlayer")


	def _on_newgame_pressed(self):
		#open popup
		self.get_node("Level_select").visible = True

	def _on_Continue_pressed(self):
		#pass
		print("Continue")
		self.reload.load()
		if Globals.previous_scene_path != "" and Globals.player is not None:
			self.get_tree().change_scene_to_file(Globals.previous_scene_path)
		else:
			print("No save presence.")

	def _on_option_pressed(self):
		#pass
		self.get_node("Setting").visible = True

	def _on_setting_back_pressed(self):
		# Close setting popup
		self.get_node("Setting").visible = False

	def _on_closepop_pressed(self):
		#close popup
		self.get_node("Level_select").visible = False

	#exitgame
	def _on_exitgame_pressed(self):
		self.get_tree().quit()

	#difficult select and var to scale with exp_gain and monster status
	def _on_easy_pressed(self):
		#add Globals. forward
		Globals.difficulty = 1
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
	def _on_medium_pressed(self):
		#add Globals. forward
		Globals.difficulty = 1.5
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
	def _on_hard_pressed(self):
		#add Globals. forward
		Globals.difficulty = 2
		self.get_tree().change_scene_to_file("res://stage/stage1.tscn")

	def _on_music_changed(self, value: float):
		db_value = -80 + (value * 1.5)
		self.music.volume_db = db_value
