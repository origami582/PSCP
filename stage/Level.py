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
	"""A UI Label node to display the current floor level."""
	def _ready(self):
		"""Called when the node is 'ready'. Initializes the label text."""
		self.update_level()

	def _process(self, delta):
		'''
		This function is a waste of resource	- Mon
		(Note: This should be connected to a signal that fires when the floor changes,
		instead of updating every frame.)
		'''
		#loop print update_level
		self.update_level()

	def update_level(self):
		"""
		Updates the label's text to show the current floor.
		"""
		#print update_level
		self.text = f"Level: {Globals.floor}"
