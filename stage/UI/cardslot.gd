extends PanelContainer

func _on_mouse_entered():
	GlobalPopup.ItemPopup(Rect2i( Vector2i(global_position), Vector2i(size)), null)

func _on_mouse_exited():
	GlobalPopup.HideItemPopup()
