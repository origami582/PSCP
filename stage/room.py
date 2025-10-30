from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .charactor import Globals

"""
Development note (Mon): There is absolutely no need to waste every frame updating
label that does not change in any values or texts.
Instead it should be connected to a signal that fires when a room is cleared.
"""

@gdclass
class room(Label):
	"""A UI Label node to display the current floor and room number."""
	def _ready(self):
		"""Called when the node is 'ready'. Initializes the label text."""
		self.update_room()

	def _process(self, delta):
		'''
		This function is a waste of resource	- Mon
		(Note: This should be connected to a signal that fires when a room is cleared,
		instead of updating every frame.)
		'''
		#loop print update_level
		self.update_room()

	def update_room(self):
		"""
		Updates the label's text to show the current floor and room.
		Handles wrapping the room number and incrementing the floor.
		"""
		#print update_level
		if Globals.room >= 10:
			Globals.room = 1
			Globals.floor += 1
		self.text = f"Floor:{Globals.floor} Room: {Globals.room}"
