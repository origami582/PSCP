from py4godot.classes import gdclass
from .monster_stat import Monster_stat

@gdclass
class Monster:
	"""
	Represents a single monster instance in combat.
	This class stores its type, stats, and current state.
	"""

	def __init__(self):
		"""Initializes a new monster with default empty stats."""
		self.monster_type:str = ''
		self.hp:float = 0
		self.max_hp:float = 0
		self.atk:float = 0
		self.exp_reward:int = 0

	def debug_report(self):
		"""Prints the current stats of the monster for debugging."""
		print("\n-------------------------------------")
		print(f"Monster Type: {self.monster_type}")
		print(f"HP: {self.hp}/{self.max_hp}")
		print("-------------------------------------\n")

	def setup_monster(self, monster_type:str):
		"""Configures the monster's stats based on its type."""
		self.monster_type = monster_type

		if monster_type in Monster_stat.MONSTER_DATA:
			# Get dictionary item of that monster and store in monster_data
			monster_data = Monster_stat.MONSTER_DATA[monster_type]

			# Set stats from retrived data
			self.hp = monster_data['hp_scaler']() * Monster_stat.BASE_HP
			self.atk = monster_data['atk_scaler']() * Monster_stat.BASE_ATK
			self.max_hp = self.hp
			self.exp_reward = monster_data['exp_reward']

			# Print debug
			self.debug_report()

		return self

	def take_damage(self, amount: int):
		"""Reduces the monster's HP by a given amount."""
		self.hp -= amount
		if self.hp < 0:
			self.hp = 0

		# Debug block
		print(f"{self.monster_type} took {amount} damage.")
		self.debug_report()
		# Debug block

	@property
	def is_dead(self):
		"""Returns True if the monster's HP is 0 or less."""
		return self.hp <= 0
