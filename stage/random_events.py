from py4godot.classes import gdclass
import random
"""
Main randomizer of the game, handling most of the in-game random events and encounter.
Using standard python random module.
"""
@gdclass
class random_event_picker:
	STANDARD_EVENT_POOL = {
		# Event structure is:
		# 'Event name' : probability(int, float)
		"monster_encounter": 50,
		"treasure_chest": 50,
		"rest_stop": 0
		# Add more events here
	}
	STANDARD_ENCOUNTER_POOL = {
		# Encounter structure is:
		# 'Encounter name': probability(int, float)
		"slime": 100,
		'goblin': 0
		# Add more encounters here
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
		chosen_event = random.choices(events, weights=weights, k=1)[0]
		return chosen_event

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

		chosen_encounter = random.choices(encounter, weights=weights, k=1)[0]
		return chosen_encounter

	# maybe should add card randomizer here
