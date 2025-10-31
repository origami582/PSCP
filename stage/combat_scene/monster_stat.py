from py4godot.classes import gdclass
from ..charactor import Globals

@gdclass	#monster base stat here to scale in monster cause we can't create var to keeo the scaled stat
class Monster_stat:
	"""
	A static class that holds the master dictionary for all monster stats.
	This acts as a central data store for monster blueprints.
	"""
	BASE_HP = 100 * Globals.difficulty
	BASE_ATK = 10 * Globals.difficulty

	MONSTER_DATA = {
		"slime": {
			"hp_scaler": lambda: 0.8 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.2 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m8.png",		# add texture path
			"exp_reward": (50 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"goblin": {
			"hp_scaler": lambda: 1.2 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 0.8 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/Boss.png",		# add texture path
			"exp_reward": 75 * Globals.difficulty * ((Globals.floor * 0.2) + 1)
		},
		# Add more monsters here
	}
