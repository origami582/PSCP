extends Node2D

func update_display():
	print("updated heart")
	if Livecounter.live == 3 :
		$Heart1.show()
		$Heart2.show()
		$Heart3.show()
	elif Livecounter.live == 2:
		$Heart1.show()
		$Heart2.show()
		$Heart3.hide()
	elif Livecounter.live == 1:
		$Heart1.show()
		$Heart2.hide()
		$Heart3.hide()
	elif Livecounter.live == 0:
		$Heart1.hide()
		$Heart2.hide()
		$Heart3.hide()
