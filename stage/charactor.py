from py4godot.classes import gdclass

@gdclass
class Character:
	"""
	Represents the player character, holding all their stats and game-related attributes.

	This class is the central data structure for the player. It manages everything
	from health and strength to experience and level progression.

	Attributes:
		strength (int): The character's attack power.
		max_hp (int): The maximum health points.
		actual_hp (int): The current health points.
		lifes (int): The number of extra lives the character has.
		level (int): The character's current level.
		exp (int): The experience points earned towards the next level.
		exp_total (int): The total experience points earned throughout the game.
		exp_req (int): The experience points required to reach the next level.

	How to Use:
		This class is typically instantiated once per game and stored in `Globals.player`.

		Example of creating a new character:
			`player_character = Character(strength=10, max_hp=100)`

		Example of accessing an attribute:
			`current_health = player_character.actual_hp`

	Adding New Variables:
		To add a new stat (e.g., `defense`), add it as an instance attribute in the `__init__` method.
		If the new stat needs to be saved when the player quits, you MUST also update the `save_data`
		dictionary in `save_reload.py` to include it in both the `save()` and `load()` methods.
	"""
	FLEE_HP_THRESHOLD = 20
	FLEE_PENALTY_PERCENTAGE = 0.25
	FLEE_PENALTY_FLAT = 5
	
	Strength_per_level = 10
	Max_hp_per_level = 20
	def __init__(self, strength=Strength_per_level, max_hp=Max_hp_per_level):
		"""
		Initializes a new character.
		Args:
			strength (int): The character's strength attribute.
			max_hp (int): The character's maximum health points.
		"""
		self.strength = strength
		self.max_hp = max_hp
		self.actual_hp = max_hp
		self.lifes = 3

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
		self.actual_hp = self.max_hp
		self.exp_req = self._get_req_exp(level=self.level + 1)
		self.strength += Character.Strength_per_level
		self.max_hp += Character.Max_hp_per_level

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
	"""A static-like class for storing global game state and singletons.

	This class acts as a centralized, globally accessible container for game-wide
	information that needs to persist across different scenes, such as the player
	object, game difficulty, and current progress (floor/room). It is essential
	for the save/load functionality.

	This class should NOT be instantiated. Its attributes are accessed directly.

	Attributes:
		player (Character): The single instance of the player's character.
		difficulty (float): A multiplier affecting game difficulty (e.g., 1.0 for Easy).
		room (int): The current room number on the floor.
		floor (int): The current floor number in the dungeon.
		previous_scene_path (str): The path to the last main scene, used for returning from menus.

	How to Use:
		`from .charactor import Globals`
		`# Accessing the player's strength`
		`player_strength = Globals.player.strength`
		`# Setting the difficulty`
		`Globals.difficulty = 1.5`
	"""
	player: Character = None  # This will hold the instance of the player's Character
	difficulty = 1.0
	room = 1
	floor = 1
	previous_scene_path = ""

	@staticmethod
	def new_game():
		"""Initializes a new game, creating a new player character."""
		Globals.player = Character(strength=40, max_hp=100)
		Globals.room = 1
		Globals.floor = 1
		Globals.previous_scene_path = ""
