from py4godot.classes import gdclass
import random

@gdclass
class random_event_picker:
	@staticmethod
	def pick_random_event(event_pool: dict) -> str:
		"""
		Picks a single random event from a dictionary of events and their weights.

		Args:
			event_pool: A dictionary where keys are event names (str)
						and values are their weights (int or float).

		Returns:
			The name of the chosen event.
		"""
		# Separate the events and weights into two lists
		events = list(event_pool.keys())
		weights = list(event_pool.values())

		# random.choices returns a list, so we take the first element
		chosen_event = random.choices(events, weights=weights, k=1)[0]
		return chosen_event
