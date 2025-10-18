from py4godot.classes import gdclass

@gdclass	#monster base stat here to scale in monster cause we can't create var to keeo the scaled stat
class Monster_stat:
	"""
	A static class that holds the master dictionary for all monster stats.
	This acts as a central data store for monster blueprints.
	"""
	BASE_HP = 100

	MONSTER_DATA = {
		"slime": {
			"hp_scaler": 0.8,
			# "atk_scaler": 1.2,
			"texture_path": "",		# add texture path
			"exp_reward": 50
		},
		"goblin": {
			"hp_scaler": 1.2,
			# "atk_scaler": 0.8,
			"texture_path": "",		# add texture path
			"exp_reward": 75
		},
		# Add more monsters here
	}
