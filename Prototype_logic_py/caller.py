'''A tester code to call 'random_events' module'''
import random_events

events = {
    "monster_encounter": 60,
    "treasure_chest": 40,
    # "trap": 30,
    # "friendly_npc": 10,
    # "rest_stop": 5,
}

selected = random_events.pick_random_event(events)
print(f"The chosen event is: '{selected}'")