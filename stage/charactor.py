from py4godot.classes import gdclass

@gdclass
class Character:
	"""Represents a single character in the game, like the player or an enemy."""
	FLEE_HP_THRESHOLD = 20
	FLEE_PENALTY_PERCENTAGE = 0.25
	FLEE_PENALTY_FLAT = 5

	def __init__(self, strength=10, max_hp=100):
		self.strength = strength
		self.max_hp = max_hp
		self.actual_hp = max_hp

		self.level = 1
		self.exp = 0
		self.exp_total = 0
		self.exp_req = self._get_req_exp(level=self.level + 1)

	def _get_req_exp(self, level):
		"""Calculates the required experience for a given level."""
		return round(number=(level ** 1.8) + level * 4)

	def gain_exp(self, amount: int):
		"""Adds experience to the character and levels up if necessary."""
		if amount <= 0:
			return

		self.exp_total += amount
		self.exp += amount

		while self.exp >= self.exp_req:
			self.exp -= self.exp_req
			self._level_up()

	def _level_up(self):
		"""Increases character level and updates required experience."""
		self.level += 1
		# Future improvement: Increase max_hp or other stats on level up.
		self.exp_req = self._get_req_exp(level=self.level + 1)

	def flee_penalty(self):
		"""Applies a penalty to HP for fleeing and returns the new HP."""
		print("Applying flee penalty...")  # Debug

		if self.actual_hp >= self.FLEE_HP_THRESHOLD:
			penalty = int(self.actual_hp * self.FLEE_PENALTY_PERCENTAGE)
			print(f"Penalty: {penalty} HP (percentage based)")  # Debug
		else:
			# TODO: Adjust penalty based on difficulty level
			penalty = self.FLEE_PENALTY_FLAT
			print(f"Penalty: {penalty} HP (flat rate)")  # Debug

		self.actual_hp -= penalty
		if self.actual_hp < 0:
			self.actual_hp = 0

		return self.actual_hp

@gdclass
class Globals:
	"""A class for storing true global game state and singletons."""
	player: Character = None  # This will hold the instance of the player's Character
	difficulty = 1
	room = 1
	floor = 1
	previous_scene_path = ""

	@staticmethod
	def new_game():
		"""Initializes a new game, creating a new player character."""
		Globals.player = Character(strength=10, max_hp=100)
		Globals.difficulty = 1
		Globals.room = 1
		Globals.floor = 1
		Globals.previous_scene_path = ""

	
