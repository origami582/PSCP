from py4godot.classes import gdclass
from ..charactor import Globals

@gdclass
class Monster_stat:
	"""
	A static class that holds the master dictionary for all monster stats.
	This acts as a central data store for monster blueprints.
	"""
	# These are now lambda functions to be calculated at runtime, ensuring they use the current difficulty.
	BASE_HP = lambda: 100 * Globals.difficulty
	BASE_ATK = lambda: 10 * Globals.difficulty

	MONSTER_DATA = {
		"slime": {
			"hp_scaler": lambda: 0.8 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.2 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m8.png",
			"exp_reward": lambda: (50 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"stacked_slime": {
			"hp_scaler": lambda: 1.0 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.5 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m10.png",
			"exp_reward": lambda: (60 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"dark_slime": {
			"hp_scaler": lambda: 1.2 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.7 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m15.png",
			"exp_reward": lambda: (75 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"goblin": {
			"hp_scaler": lambda: 1.2 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 0.8 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m9.png",
			"exp_reward": lambda: 75 * Globals.difficulty * ((Globals.floor * 0.2) + 1)
		},
		"goblin_barbarian": {
			"hp_scaler": lambda: 1.4 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.3 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m11.png",
			"exp_reward": lambda: 80 * Globals.difficulty * ((Globals.floor * 0.2) + 1)
		},
		"goblin_knight": {
			"hp_scaler": lambda: 2.0 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.9 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m14.png",
			"exp_reward": lambda: 120 * Globals.difficulty * ((Globals.floor * 0.2) + 1)
		},
		"wraith": {
			"hp_scaler": lambda: 1.1 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 0.5 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m4.png",
			"exp_reward": lambda: (30 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"lingering_wraith": {
			"hp_scaler": lambda: 1.5 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.0 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m23.png",
			"exp_reward": lambda: (40 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"grim": {
			"hp_scaler": lambda: 1.7 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 1.6 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m18.png",
			"exp_reward": lambda: (90 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		},
		"cuckcoo": {
			"hp_scaler": lambda: 2 + ((Globals.floor - 1) * 0.5),
			"atk_scaler": lambda: 0.5 + ((Globals.floor - 1) * 0.5),
			"texture_path": "res://img/Enemies/sento_m29.png",
			"exp_reward": lambda: (50 * Globals.difficulty) * ((Globals.floor * 0.2) + 1)
		}
}

	BOSS_DATA = {
		# Bosses should have significantly higher stats than normal monsters.
		# These scalers are much more aggressive.
		"Cho": {
			"hp_scaler": lambda: 5.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 3.0 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/Cho.png",
			"exp_reward": lambda: 500 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Titanoboa": {
			"hp_scaler": lambda: 6.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 3.0 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m27.png",
			"exp_reward": lambda: 550 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Queen_of_Love": {
			"hp_scaler": lambda: 5.5 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 3.5 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m34.png",
			"exp_reward": lambda: 640 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Titan_golem": {
			"hp_scaler": lambda: 7.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 4.0 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m28.png",
			"exp_reward": lambda: 710 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Perfect_golem": {
			"hp_scaler": lambda: 8.2 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 5.2 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m35.png",
			"exp_reward": lambda: 840 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Man_eater": {
			"hp_scaler": lambda: 9.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 5.8 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m32.png",
			"exp_reward": lambda: 860 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"False_dragon": {
			"hp_scaler": lambda: 10.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 4.0 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m30.png",
			"exp_reward": lambda: 750 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Dragon_lord": {
			"hp_scaler": lambda: 10.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 7.0 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/sento_m33.png",
			"exp_reward": lambda: 1000 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"Roland": {
			# Special secret boss Roland from LoR
			"hp_scaler": lambda: 5.5 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 4.5 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/Roland (Small).png",
			"exp_reward": lambda: 900 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		},
		"The_Black_Silence": {
			# Roland stage 2 (You're a dead man!)
			"hp_scaler": lambda: 30.0 + ((Globals.floor - 1) * 1.5),
			"atk_scaler": lambda: 20.0 + ((Globals.floor - 1) * 1.0),
			"texture_path": "res://img/Enemies/The_Black_Silence (Small).png",
			"exp_reward": lambda: 4000 * Globals.difficulty * ((Globals.floor * 0.5) + 1)
		}
	}
