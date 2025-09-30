"""character"""
def character_status():
	# char statsu here
	max_hp = 100		# input this later na
	strenght = 10		# This too
	# other status to scale here too

def level_char():
	# Level system
	level = 1
	exp = 0											# exp char have between lv.
	exp_total = 0
	exp_req = get_req_exp(level+1)					# exp req for next lv.

def get_req_exp(level):
	# exp req per next lv. which we need to cal later
	return round((level **1.8) + level * 4)			# formula to scale exp_req per level

def gain_exp(amount):
	# gain amout of exp per one lv.
	exp_total += amount
	exp += amount									# gain EXP
	while exp >= exp_req:							# loop for exp if exp that >= exp_req
		exp -= exp_req								# minus exp that >= exp_req for >1 lv.
		level_up()
		
def level_up():
	# lv. up func
	level += 1
	exp_req = get_req_exp(level+1)					# set a new req exp from formula

### doing status later
