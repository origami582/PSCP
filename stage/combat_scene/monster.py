from py4godot.classes import gdclass
from .monster_stat import Monster_stat

@gdclass
class Monster:
	"""
	This will store a blueprint for a monster.
	appearance(later), and state.
	"""
	BASE_HP = 100

	def __init__(self):
		self.monster_type:str = ''
		self.hp:float = 0
		self.max_hp:float = 0
		# self.atk:float = 0
		self.exp_reward:int = 0

	def debug_report(self):
		'''for unify debuging purpose'''
		print("\n-------------------------------------")
		print(f"Monster Type: {self.monster_type}")
		print(f"HP: {self.hp}/{self.max_hp}")
		print("-------------------------------------\n")

	def setup_monster(self, monster_type:str):
		'''Setup a monster'''
		self.monster_type = monster_type

		if monster_type in Monster_stat.MONSTER_DATA:
			# Get dictionary item of that monster and store in monster_data
			monster_data = Monster_stat.MONSTER_DATA[monster_type]

			# Set stats from retrived data
			self.hp = monster_data['hp_scaler'] * Monster.BASE_HP
			self.max_hp = self.hp
			self.exp_reward = monster_data['exp_reward']

			# Print debug
			self.debug_report()

		return self

	def take_damage(self, amount: int):
		self.hp -= amount
		if self.hp < 0:
			self.hp = 0

		# Debug block
		print(f"{self.monster_type} took {amount} damage.")
		self.debug_report()
		# Debug block

	@property
	def is_dead(self):
		return self.hp <= 0
