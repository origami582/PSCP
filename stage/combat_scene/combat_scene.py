from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from .monster import Monster
from ..charactor import Globals
from py4godot.classes.Label import Label
from ..maingame import maingame

@gdclass
class combat_scene(Control):
	def _ready(self):
		self.get_node("Attack_Button").disabled = False
		self.get_node("Flee_Button").disabled = False
		self.get_node("dead_screen").visible = False
		
	def player_died(self):
		'''call this function when player is dead'''
		self.get_node("Attack_Button").disabled = True
		self.get_node("Flee_Button").disabled = True
		self.get_node("dead_screen").visible = True
	
	Cuurent_HP = Monster.slime_hp
	def _on_attack_button_pressed(self):		#button pressed to attack monster
		if Monster.slime_hp <= 0:		#check monster hp for change scence
			print("Monster Defeated")
			print(f"You gained 50 EXP!!!")
			Globals.gain_exp(50)		#Gained EXP after defeated monster
			# Status report will always trigger after returning to maingame (stage1.tscn) :)
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
		Monster.slime_hp -= Globals.strength		#damage
		combat_scene.Cuurent_HP = Monster.slime_hp
		print(f"HP remainig: {combat_scene.Cuurent_HP}")

	def _on_flee_button_pressed(self):
		remain_hp = Globals.flee_penalty()
		print(f"Debug player hp: {remain_hp}")
		if remain_hp <= 0:
			print("died")
			self.player_died()		# call function above when player is dead
			### Maybe call result scence here?
		else:
			# Player survived, return to main stage
			self.get_tree().change_scene_to_file("res://stage/stage1.tscn")
			
	def _on_died_back_to_menu_pressed(self):
		self.get_tree().change_scene_to_file("res://stage/main_menu.tscn")
