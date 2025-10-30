extends Label

# It would be better if we work with label and display text in native GDscript

# This function updates the HP label.
# It takes the current HP and maximum HP as arguments.
func update_hp(current_hp, max_hp):
	text = "HP: " + str(current_hp) + " / " + str(max_hp)
	
