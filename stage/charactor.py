from py4godot.classes import gdclass

@gdclass
class Globals:
	max_hp = None
	actual_hp = None
	strength = 10

	level = 1
	exp = 0
	exp_total = 0
	exp_req = 0
	# new
	difficult = 1
	#
	room = 1
	floor = 1

	@staticmethod
	def get_req_exp(level):
		return round((level ** 1.8) + level * 4)

	@staticmethod
	def init_character():
		Globals.level = 1
		Globals.max_hp = 100
		Globals.actual_hp = Globals.max_hp
		Globals.exp = 0
		Globals.exp_total = 0
		Globals.exp_req = Globals.get_req_exp(Globals.level + 1)

	@staticmethod
	def gain_exp(amount: int):
		Globals.exp_total += amount
		Globals.exp += amount

		while Globals.exp >= Globals.exp_req:
			Globals.exp -= Globals.exp_req
			Globals.level_up()

	@staticmethod
	def level_up():
		Globals.level += 1
		Globals.exp_req = Globals.get_req_exp(Globals.level + 1)

	@staticmethod
	def flee_penalty():
		# HP reduction
		print("Penalized")      # Debug
		remaining_hp = Globals.max_hp
		if remaining_hp >= 20:      # Penalize by 25% of current hp if hp >= 20
			print("penalty 1")  # Debug
			penalty = int(Globals.actual_hp * ((25/100)))
			Globals.actual_hp -= penalty
		else:       # Penalize by constant when hp is lower than 20 for more strategic thinking
			print("Penalty 2")  # Debug
			penalty = 5     # need adjustment based on deficulty level later
			Globals.actual_hp -= penalty
		if Globals.actual_hp < 0:
			Globals.actual_hp = 0
		return Globals.actual_hp
