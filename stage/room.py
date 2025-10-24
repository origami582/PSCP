from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .charactor import Globals

'''
Development note (Mon): There is absolutely no need to waste every frame updating
label that does not change in any values or texts
'''

@gdclass
class room(Label):
	def _ready(self):
		self.update_level()

	def _process(self, delta):
		'''
		This function is a waste of resource	- Mon
		'''
		#loop print update_level
		self.update_room()

	def update_room(self):
		#print update_level
		if Globals.room >= 10:
			Globals.room = 1
			Globals.floor += 1
		self.text = f"Floor:{Globals.floor} Room: {Globals.room}"
