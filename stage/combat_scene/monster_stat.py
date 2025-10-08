from py4godot.classes import gdclass

@gdclass	#monster base stat here to scale in monster cause we can't create var to keeo the scaled stat
class Monster:
	base_hp = 100
	#type_monster for scaling
	slime = 0.8
