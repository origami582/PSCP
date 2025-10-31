'''
A module to save game states, primary charactor.py parameters
for continuing the game from last save. once reopen the game
'''
from py4godot.classes import gdclass
import json
import base64
import os
from .charactor import Character, Globals

SAVE_PATH = "save/save.txt"
@gdclass
class save_game:
	"""Handles the logic for saving the game state to a file."""
	def save(self, character: Character):
		"""
		Saves the current character and global game state to a file.
		The data is saved as a base64 encoded JSON string.

		Args:
			character (Character): The player character instance to save.
		"""
		error = False
		try:
			# 1. Consolidate all data into a dictionary
			save_data = {
				"strength": character.strength,
				"max_hp": character.max_hp,
				"actual_hp": character.actual_hp,
				"lives": character.lifes,
				"level": character.level,
				"exp": character.exp,
				"exp_total": character.exp_total,
				"exp_req": character.exp_req,
				"difficulty": Globals.difficulty,
				"room": Globals.room,
				"floor": Globals.floor,
				"previous_scene_path": Globals.previous_scene_path,
			}

			# 2. Convert to JSON, encode to bytes, then encode with base64
			json_string = json.dumps(obj=save_data, indent=4)
			encoded_data = base64.b64encode(s=json_string.encode(encoding='utf-8'))

			with open(file=SAVE_PATH, mode="wb") as file: # 'wb' for writing bytes
				file.write(encoded_data)
		except (IOError, OSError) as e:
			print(f"Error: Could not save the game to file. Reason: {e}")
			error = True
		except AttributeError:
			print("Error: Invalid character data provided for saving. Cannot save.")
			error = True
		except Exception as e:
			print(f"An unexpected error occurred while saving the game: {e}")
			error = True
		finally:
			if not error:
				print("Game saved successfully.")
			else:
				print("Game save failed.")

@gdclass
class load_game:
	"""Handles the logic for loading the game state from a file."""
	def load(self):
		"""
		Loads the game state from the save file.
		It populates the Globals.player and other global variables.
		"""
		try:
			with open(file=SAVE_PATH, mode="rb") as file: # 'rb' for reading bytes
				encoded_data = file.read()

			# 1. Decode from base64, then decode bytes to JSON string
			json_string = base64.b64decode(s=encoded_data).decode(encoding='utf-8')

			# 2. Parse JSON string into a dictionary
			save_data = json.loads(s=json_string)

			# 3. Create a new character and populate its stats from the dictionary
			new_character = Character(
				strength=save_data["strength"],
				max_hp=save_data["max_hp"]
			)
			new_character.actual_hp = save_data["actual_hp"]
			new_character.lifes = save_data["lives"]
			new_character.level = save_data["level"]
			new_character.exp = save_data["exp"]
			new_character.exp_total = save_data["exp_total"]
			new_character.exp_req = save_data["exp_req"]

			# 4. Restore all global states
			Globals.player = new_character
			Globals.difficulty = save_data["difficulty"]
			Globals.room = save_data["room"]
			Globals.floor = save_data["floor"]
			Globals.previous_scene_path = save_data["previous_scene_path"]

			print("Game loaded successfully.")
		except (IOError, OSError) as e:
			print(f"Error: Could not load the game from file. Reason: {e}")
		except (json.JSONDecodeError, KeyError, TypeError) as e:
			print(f"Error: Save file is corrupted or has an invalid format. Reason: {e}")

@gdclass
class clear_save:
	"""Handles the logic for deleting the save game file."""
	def clear(self):
		"""
		Deletes the save file from the disk if it exists.
		"""
		try:
			if os.path.exists(SAVE_PATH):
				os.remove(SAVE_PATH)
				print("Save file cleared successfully.")
			else:
				print("No save file found to clear.")
		except OSError as e:
			print(f"Error: Could not clear the save file. Reason: {e}")
