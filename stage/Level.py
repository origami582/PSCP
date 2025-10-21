from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .charactor import Globals

'''
Note: By 'level' it mean floor level
'''

'''
Development note (Mon): There is absolutely no need to waste every frame updating
label that does not change in any values or texts
'''

@gdclass
class Level(Label):
	def _ready(self):
		self.update_level()

	def _process(self, delta):
		'''
		This function is a waste of resource	- Mon
		'''
		#loop print update_level
		self.update_level()

	def update_level(self):
		#print update_level
		self.text = f"Level: {Globals.floor}"
