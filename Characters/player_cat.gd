extends CharacterBody2D

@export var move_speed : float = 100
@export var starting_direction : Vector2 = Vector2(0,1)

@onready var animation_tree = $AnimationTree
@onready var state_machine = animation_tree.get('parameters/playback')

func _ready():
	update_animation_parameter(starting_direction)

func _physics_process(_delta):
	# Get input direction
	var input_direction = Vector2(
		Input.get_action_strength("Right") - Input.get_action_strength("Left"),
		Input.get_action_strength("Down") - Input.get_action_strength("Up")
	)
	
	update_animation_parameter(input_direction)
	
	# Update velocity
	velocity = input_direction * move_speed
	
	# Move and slide use velocity of character body to move character on the map
	move_and_slide()
	
	pick_new_state()

func update_animation_parameter(move_input : Vector2):
	# Dont change animation parameter if there are no movements
	if (move_input != Vector2.ZERO):
		animation_tree.set('parameters/idle/blend_position', move_input)
		animation_tree.set('parameters/walk/blend_position', move_input)

# pick new animation state based on whats happening
func pick_new_state():
	if (velocity != Vector2.ZERO):
		state_machine.travel('walk')
	else:
		state_machine.travel('idle')
	
