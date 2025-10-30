from py4godot.classes import gdclass
from py4godot.classes.Label import Label

@gdclass
class textpanel(Label):
	"""A UI label for displaying combat text, like attack messages."""
	def _ready(self):
		"""Initializes the label."""
		# You can set some default text or leave it blank
		self.text = ""

	def show_dice_roll(self, dice_face: int):
		"""Update label to show dice roll."""
		self.text += f"Dice roll: {dice_face}\n"

	def show_player_attack(self, monster_name: str, damage: int):
		"""Updates the label to show the player's attack."""
		self.text += f"You attack! {monster_name} took {damage} damage!\n"

	def show_monster_attack(self, monster_name: str, damage: int):
		"""Updates the label to show the monster's attack."""
		self.text += f"{monster_name} attacks! You took {damage} damage!\n"

	def show_monster_dead(self, monster_name: str, exp: int):
		"""Updates the label to show the player's attack."""
		self.text += f"{monster_name} defeated!!! you gained {exp} EXP!!!\n"

	def clear_text(self):
		"""Clears all text from the label."""
		self.text = ""
