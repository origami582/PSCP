from py4godot.classes import gdclass
from py4godot.classes.Label import Label

@gdclass
class textpanel(Label):
	"""A UI label for displaying combat text, like attack messages."""
	def _ready(self):
		"""Initializes the label."""
		# You can set some default text or leave it blank
		self.text = ""

	def show_rest(self, cases: str):
		"""Show once enter rest stop scene"""
		match cases:
			case 'enter':
				self.text = "You found a good spot to rest!"
			case 'leave':
				self.text = "You gather your belongings and leave.\n"
				self.text += "Health fully restored!\n"
				self.text += "Life restored by 1!"

	def show_chest_room(self):
		"""Show once enter tresure room"""
		self.text = "You found a tresure chest?"

	def show_chest(self):
		"""For secret high rarity (honestly unfinish) scene"""
		self.text += "You open the chest and found... nothing?\n"
		self.text += "Perhaps you found a... secret?\n\n\n\n"
		self.text += "*This scene is unfinished :P"

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

	def show_roland_transform(self):
		"""Shows the transformation text for the Roland boss fight."""
		self.text += "Roland: '...Fine. Let's see how you handle this.'\n"
		self.text += "He becomes The Black Silence!\n"

	def show_flee(self,  died: bool, monster_name: str, damage: int):
		"""Updates the label to show the player's attack."""
		if died:
			self.text += f"You died trying to flee from {monster_name}!\n"
		else:
			self.text += f"You take {damage} damages trying to flee!\n"

	def clear_text(self):
		"""Clears all text from the label."""
		self.text = ""
