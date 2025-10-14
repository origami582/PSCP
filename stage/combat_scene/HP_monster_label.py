from py4godot.classes import gdclass
#lebel for text box output
from py4godot.classes.Label import Label

@gdclass
class HP_monster_label(Label):
	combat_scene_node: object = None

	def _ready(self):
		# Get the parent node, which is the combat_scene.
		self.combat_scene_node = self.get_parent()
		self.update_hp_label()

	def update_hp_label(self):
		"""Updates the label's text. This is called by combat_scene."""
		# Check if the monster exists to avoid errors.
		if self.combat_scene_node and self.combat_scene_node.monster:
			monster = self.combat_scene_node.monster
			self.text = f"Monster HP: {int(monster.hp)} / {int(monster.max_hp)}"
