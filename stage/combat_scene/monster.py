from py4godot.classes import gdclass
from .monster_stat import Monster

@gdclass
class Monster: #use base_stat from monster_status and scale here
	slime_hp = Monster.base_hp * Monster.slime
	print(f"Slime HP: {slime_hp}")
