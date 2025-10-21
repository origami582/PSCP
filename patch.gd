extends Node

func _enter_tree() -> void:
	get_tree().node_added.connect(_on_node_added)
	
func _on_node_added(node) -> void:
	var popup = node as PopupMenu
	if popup:
		popup.transparent_bg = true
	
