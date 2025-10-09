from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label
from .combat_scene import combat_scene
#if kit fix hp ma delete this
from .monster_stat import Monster

@gdclass	#need soda to fix this later
# fix name class HP_monster --> HP_monster_label
class HP_monster_label(Label):
	def _ready(self):
		self.update_level()
	
	def _process(self, delta):
		#loop print update_level
		self.update_level()
	
	def update_level(self):
		#print update_level
		#kit fix this i test hp form monster_stat because combat_scene can not use
		self.text = f"HP remaining: {Monster.base_hp}"
