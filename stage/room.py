from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .charactor import Globals

@gdclass
class room(Label):
	def _ready(self):
		self.update_level()

	def _process(self, delta):
		#loop print update_level
		self.update_room()

	def update_room(self):
		#print update_level
		if Globals.room >= 10:
			Globals.room = 1
			Globals.floor += 1
		self.text = f"Floot:{Globals.floor} Room: {Globals.room}"
