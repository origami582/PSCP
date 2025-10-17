from py4godot.classes import gdclass
from py4godot.classes.Label import Label
### idk where file about dmg mon
from .monster import Monster

@gdclass
class textpanel(Label):
	def _ready(self):
		self.update_textpanel()

	def _process(self, delta):
		#loop print update_textpanel
		self.update_textpanel()

	def update_textpanel(self):
		#print update_textpanel
		self.text = f"test"
