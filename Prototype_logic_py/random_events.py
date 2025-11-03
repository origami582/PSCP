'''
This is a prototype code for picking random events from available pool
'''
import random

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

if __name__ == "__main__":
	# Define the pool of possible events and their weights.
	# The weights don't have to sum to 100. They are relative to each other.
	available_events = {
		"monster_encounter": 60,
		"treasure_chest": 20,
		"trap": 30,
		"friendly_npc": 10,
		"rest_stop": 5,
	}

	print(f"Picking a random event from: {available_events}")
	selected_event = pick_random_event(available_events)
	print(f"The chosen event is: '{selected_event}'")
