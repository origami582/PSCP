from py4godot.classes import gdclass

@gdclass
class Globals:
	hp = 100
	strength = 10

	level = 1
	exp = 0
	exp_total = 0
	exp_req = 0
	# new
	difficult = 1

	@staticmethod
	def get_req_exp(level):
		return round((level ** 1.8) + level * 4)

	@staticmethod
	def init_character():
		Globals.level = 1
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
	def skip_penalty():
		# HP reduction
		print("Penalized")
		Globals.hp -= 10
		return Globals.hp
		
