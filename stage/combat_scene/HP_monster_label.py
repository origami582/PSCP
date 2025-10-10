from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .combat_scene import combat_scene
from .monster import Monster

@gdclass	#need soda to fix this later
class HP_monster_label(Label):
	def _ready(self):
		self.update_level()
	
	def _process(self, delta):
		#loop print update_level
		self.update_level()
	
	def update_level(self):
		#print update_level
		self.text = f"Slime HP remaining: {combat_scene.Cuurent_HP}"
