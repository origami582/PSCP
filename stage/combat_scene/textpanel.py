from py4godot.classes import gdclass
from py4godot.classes.Label import Label
from ..charactor import Globals
from .monster import Monster

@gdclass
class textpanel(Label):
	"""A UI label for displaying combat text, like attack messages."""
	def _ready(self):
		# You can set some default text or leave it blank
		self.text = ""

	def show_player_attack(self, monster_name: str, damage: int):
		"""Updates the label to show the player's attack."""
		self.text += f"{monster_name} took {damage} damage!\n"

	def show_monster_dead(self, monster_name: str, exp: int):
		"""Updates the label to show the player's attack."""
		self.text += f"{monster_name} defeated!!! you gained {exp} EXP!!!\n"
