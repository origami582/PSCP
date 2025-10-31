from py4godot.classes import gdclass
from .charactor import Globals
import random
"""
Main randomizer of the game, handling most of the in-game random events and encounter.
Using standard python random module.
"""
@gdclass
class random_event_picker:
	"""
	A utility class with static methods to handle weighted random selections for game events and encounters.
	"""

	STANDARD_EVENT_POOL = {
		# Event structure is:
		# 'Event name' : probability(int, float)
		"monster_encounter": 70,
		"treasure_chest": 0.001,	# Ditch (appear as a secret)
		"rest_stop": 0
		# Add more events here
	}
	STANDARD_ENCOUNTER_POOL = {
		# Encounter structure is:
		# 'Encounter name': probability(int, float)
		# Common
		"slime": 55,
		"goblin": 50,
		# Uncommon
		"stacked_slime": 20,
		"dark_slime": 15,
		"goblin_barbarian": 25,
		"goblin_knight": 15,
		"wraith": 20,
		# Rare
		"lingering_wraith": 10,
		"grim": 10,
		"cuckcoo": 5, # Very rare
	}
	STANDARD_BOSS_POOL = {
		# Bosses that can appear on any floor
		"Titanoboa": 90,
		"Queen_of_Love": 80,
		"Titan_golem": 70,
		"False_dragon": 60,
		"Man_eater": 55,
		"Perfect_golem": 50,
		"Dragon_lord": 30,
		"Cho": 30,
		"Roland": 5000, # Special boss, ultra rare
	}
	@staticmethod
	def pick_random_event(event_pool: dict = None) -> str:
		"""
		Picks a single random event from a dictionary of events and their weights.

		Args:
			event_pool: A dictionary where keys are event names (str)
						and values are their weights (int or float).

		Returns:
			The name of the chosen event.
		"""
		if event_pool is None:
			event_pool = random_event_picker.STANDARD_EVENT_POOL

		# Separate the events and weights into two lists
		events = list(event_pool.keys())
		weights = list(event_pool.values())

		# random.choices returns a list, so we take the first element
		chosen_event = random.choices(population=events, weights=weights, k=1)[0]
		return chosen_event

	@staticmethod
	def pick_random_boss(boss_pool: dict = None) ->str:
		if boss_pool is None:
			boss_pool = random_event_picker.STANDARD_BOSS_POOL

		boss = list(boss_pool.keys())
		weights = list(boss_pool.values())

		chosen_boss = random.choices(population=boss, weights=weights, k=1)[0]
		return chosen_boss

	@staticmethod
	def pick_random_encounter(encounter_pool: dict = None) -> str:
		"""
		Picks a single random encounter(mainly monster encounters) from a dictionary of
		encounters and their weights.

		Args:
			encounter_pool: A dictionary where keys are encounter names (str)

		Return:
			The name of the chosen encounter.
		"""
		if encounter_pool is None:
			encounter_pool = random_event_picker.STANDARD_ENCOUNTER_POOL

		encounter = list(encounter_pool.keys())
		weights = list(encounter_pool.values())

		chosen_encounter = random.choices(population=encounter, weights=weights, k=1)[0]
		return chosen_encounter

	@staticmethod
	def dice_roll() -> int:
		'''
		Roll a dice!
		The dice roll is weighted based on the game's difficulty.
		- Easy: Higher chance for high rolls.
		- Medium: Standard, even chances.
		- Hard: Higher chance for low rolls.
		'''
		outcomes = [1, 2, 3, 4, 5, 6]

		# Define weights based on difficulty
		if Globals.difficulty <= 1.0: # Easy
			# Favors higher numbers
			weights = [10, 10, 15, 20, 25, 20]
		elif Globals.difficulty >= 2.0: # Hard
			# Favors lower numbers
			weights = [20, 25, 20, 15, 10, 10]
		else: # Medium / Normal
			# Standard even weights
			weights = [1, 1, 1, 1, 1, 1]

		# random.choices returns a list of k elements, so we take the first one.
		chosen_roll = random.choices(population=outcomes, weights=weights, k=1)[0]

		print(f"Dice roll (Difficulty: {Globals.difficulty}): {chosen_roll}") # Debug

		return chosen_roll
