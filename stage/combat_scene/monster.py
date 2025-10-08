from py4godot.classes import gdclass
from .monster_stat import Monster

@gdclass
class Slime:
	slime_hp = Monster.base_hp * Monster.slime
	print(slime_hp)
