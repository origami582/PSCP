from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .charactor import Globals
'''
Note: By 'level' it mean floor level
'''
@gdclass
class Level(Label):
	def _ready(self):
		self.update_level()

	def _process(self, delta):
		#loop print update_level
		self.update_level()

	def update_level(self):
		#print update_level
		self.text = f"Level: {Globals.floor}"
