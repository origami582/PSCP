extends Node2D

func update_display(lives):
	$Heart1.visible = (lives >= 1)
	$Heart2.visible = (lives >= 2)
	$Heart3.visible = (lives >= 3)
