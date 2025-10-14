from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label

@gdclass
class HP_monster_label(Label):
	def __init__(self):
		self.text = ""

	def _ready(self):
		# The label starts empty. It will be updated by a signal.
		self.text = ""

	def _on_monster_hp_changed(self, current_hp: int, max_hp: int):
		self.text = f"Monster HP: {current_hp} / {max_hp}"
