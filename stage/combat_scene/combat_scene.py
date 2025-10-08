from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from .monster import Monster
from ..charactor import Globals
from py4godot.classes.Label import Label

@gdclass
class combat_scene(Control):
	def _on_button_pressed(self):		#button pressed to attack monster
		if Monster.slime_hp <= 0:		#check monster hp for change scence
			print("Monster Defeated")
			print(f"You gained 50 EXP!!!")
			Globals.gain_exp(50)		#Gained EXP after defeated monster
			print(f"Level: {Globals.level}")
			print(f"EXP: {Globals.exp}/{Globals.exp_req}")
			print(f"Total EXP: {Globals.exp_total}")
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
		Monster.slime_hp -= Globals.strength		#damage
		Cuurent_HP = Monster.slime_hp
		print(Cuurent_HP)
