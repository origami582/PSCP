extends AudioStreamPlayer

## The default volume for music in decibels. -10 is a good starting point. 0 is full volume.
@export var default_volume_db: float = -10.0
## The time in seconds for music to fade in or out.
@export var fade_duration: float = 0.60

# In the Inspector, you'll now define music like this:
# Key: "battle_music"
# Value: (Dictionary) with "path", optional "volume_db", and optional "loops"
@export var music_library: Dictionary = {
	"II_A1": {"path": "res://Sound/canto_II_A1.mp3", "volume_db": -10.0, "loops": true},
	"III_B2": {"path": "res://Sound/canto_III_B2.mp3", "volume_db": -10.0, "loops": true},
	"III_D1": {"path": "res://Sound/canto_III_D1.mp3", "volume_db": -10.0, "loops": true},
	"Coo": {"path": "res://Sound/Mourning Dove Coo.mp3", "volume_db": -7.0, "loops": true},
	"Nightingale": {"path": "res://Sound/nightingale.mp3", "volume_db": -5.0, "loops": true},
	"Rosette": {"path": "res://Sound/sys act18mini.mp3", "volume_db": -5.0, "loops": true},
	"DeepSea": {"path": "res://Sound/sys rglk2theme2distort.mp3", "volume_db": -6.0, "loops": true},
	"MysticSea": {"path": "res://Sound/sys rglk2theme1.mp3", "volume_db": -8.0, "loops": true},
	"Mirage": {"path": "res://Sound/mirage sandbox 1.mp3", "volume_db": -8.0, "loops": true},
	"Boss2": {"path": "res://Sound/bat rglk2boss2.mp3", "volume_db": -6.0, "loops": true},
	"Fun": {"path": "res://Sound/sys act5fun.mp3", "volume_db": -10.0, "loops": true},
	"Roland2": {"path": "res://Sound/Roland 2.mp3", "volume_db": -9.0, "loops": true},
	"GoneAngels": {"path": "res://Sound/Gone Angels.mp3", "volume_db": -7.0, "loops": true}
}

# This dictionary will store the actual pre-loaded audio resources.
var _preloaded_music: Dictionary = {}
var _current_tween: Tween
var _should_loop: bool = false


func _ready():
	# Pre-load all music resources when the game starts.
	for music_name in music_library:
		var music_info = music_library[music_name]
		if music_info is Dictionary and music_info.has("path"):
			var path = music_info["path"]
			if FileAccess.file_exists(path):
				_preloaded_music[music_name] = load(path)
			else:
				printerr("Audio Error: Music file not found at path: ", path)

	connect("finished", _on_music_finished)


## Plays music from the library based on the provided name.
func play_music(music_name: String):
	if _preloaded_music.has(music_name):
		var music_stream = _preloaded_music[music_name]
		# Don't do anything if the requested music is already playing.
		if stream != music_stream:
			# Get the target volume for the new track.
			var music_info = music_library[music_name]

			# If music is already playing, fade it out first.
			# The fade_out function will then call a function to play the new track.
			if playing:
				fade_out(music_stream, music_info)
			else:
				# If nothing is playing, just start the new track immediately.
				_play_and_fade_in(music_stream, music_info)
	else:
		printerr("Audio Error: Music track '", music_name, "' not found in music_library.")

## Stops the currently playing music.
func stop_music():
	fade_out(null, null) # Fade out and don't play anything next.

func fade_out(next_stream, next_music_info):
	# Kill any existing tween to avoid conflicts.
	if _current_tween:
		_current_tween.kill()
	_current_tween = create_tween()
	# Animate volume_db from its current value down to a "silent" value.
	_current_tween.tween_property(self, "volume_db", -80.0, fade_duration).from_current()

	# When the fade-out is finished, decide what to do next.
	if next_stream:
		# If a new track is queued, play it.
		_current_tween.tween_callback(_play_and_fade_in.bind(next_stream, next_music_info))
	else:
		# If no new track, just stop the player.
		_current_tween.tween_callback(stop)

func fade_in(target_db: float):
	if _current_tween:
		_current_tween.kill()
	_current_tween = create_tween()
	# Start from silent and fade up to the target volume.
	volume_db = -80.0
	_current_tween.tween_property(self, "volume_db", target_db, fade_duration)

func _play_and_fade_in(music_stream, music_info):
	# This is the new central function for starting a track.
	var target_volume = music_info.get("volume_db", default_volume_db)
	_should_loop = music_info.get("loops", true)

	stream = music_stream
	play()
	fade_in(target_volume)

func _on_music_finished():
	# This signal is connected in _ready(). It will only be called when a track naturally ends.
	if _should_loop:
		play()

## Sets the master volume for all music by controlling the 'Music' audio bus.
## 'value' is expected to be a volume in decibels (dB), e.g., from -80 to 0.
func set_master_volume(value: float):
	var music_bus_idx = AudioServer.get_bus_index("Music")
	if music_bus_idx != -1:
		# The value is already in decibels, so we can apply it directly.
		AudioServer.set_bus_volume_db(music_bus_idx, value)
