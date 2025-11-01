from py4godot.classes import gdclass
from py4godot.classes.Control import Control
#Connect files to charactor
from stage.charactor import Globals
from stage.save_reload import load_game


@gdclass
class main(Control):
	"""
	Main menu scene script. Handles UI interactions like starting a new game,
	continuing, options, and quitting.
	"""
	def __init__(self):
		# Don't forget to call the parent class's constructor!
		super().__init__()
		self.reload = load_game()

	def _ready(self):
		"""Called when the node is 'ready', i.e., when both the node and its children have entered the scene tree."""
		# Use the centralized AudioPlayer to play the menu music.
		# "Rosette" is used here as an example menu theme.
		self.get_node("/root/AudioPlayer").call("play_music", "Rosette")
	def _on_newgame_pressed(self):
		"""Handles the 'New Game' button press, showing the difficulty/level selection popup."""
		#open popup
		self.get_node("Level_select").visible = True

	def _on_Continue_pressed(self):
		"""Handles the 'Continue' button press, loading the saved game state."""
		print("Continue")
		self.reload.load()
		if Globals.previous_scene_path != "" and Globals.player is not None:
			self.get_tree().change_scene_to_file(Globals.previous_scene_path)
		else:
			print("No save presence.")

	def _on_option_pressed(self):
		"""Handles the 'Option' button press, showing the settings menu."""
		self.get_node("Setting").visible = True

	def _on_setting_back_pressed(self):
		"""Handles the 'Back' button press within the settings menu."""
		# Close setting popup
		self.get_node("Setting").visible = False

	def _on_closepop_pressed(self):
		"""Handles the close button press on the level selection popup."""
		#close popup
		self.get_node("Level_select").visible = False

	#exitgame
	def _on_exitgame_pressed(self):
		"""Handles the 'Exit Game' button press, quitting the application."""
		self.get_tree().quit()

	#difficult select and var to scale with exp_gain and monster status
	def _on_easy_pressed(self):
		"""Sets difficulty to Easy and starts a new game."""
		#add Globals. forward
		Globals.new_game()
		Globals.difficulty = 1
		# Change scene to outside of labyrinth instead
		self.get_tree().change_scene_to_file("res://stage/outside/outside.tscn")
	def _on_medium_pressed(self):
		"""Sets difficulty to Medium and starts a new game."""
		#add Globals. forward
		Globals.new_game()
		Globals.difficulty = 1.5
		# Change scene to outside of labyrinth instead
		self.get_tree().change_scene_to_file("res://stage/outside/outside.tscn")
	def _on_hard_pressed(self):
		"""Sets difficulty to Hard and starts a new game."""
		#add Globals. forward
		Globals.new_game()
		Globals.difficulty = 2
		# Change scene to outside of labyrinth instead
		self.get_tree().change_scene_to_file("res://stage/outside/outside.tscn")
	def _on_sound_changed(self, value: float):
		# Call the new master volume function on the global AudioPlayer.
		# The value from the HSlider (0-100) is passed directly.
		self.get_node("/root/AudioPlayer").call("set_master_volume", value)
