import sys
import os
import pandas as pd
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from classes.Pokemon import Pokemon

csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'pokemon_data.csv') # Adjust the path to where your CSV file is located relative to `create_pokemon.py`

pokemon_data = pd.read_csv(csv_file_path) # Load Pokémon data from the corrected CSV file path

def single_pokemon(name):
	# Filter the DataFrame to find Bulbasaur
	bulbasaur_row = pokemon_data[pokemon_data['name'].str.lower() == 'bulbasaur'].iloc[0]

	# Parse the 'types' field from a string to an actual list
	# Assuming the types are stored as "['type1', 'type2']", etc.
	bulbasaur_types = json.loads(bulbasaur_row['types'].replace("'", '"'))

	# Parse the 'stats' field from a string to an actual dictionary
	# Assuming the stats are stored as "{'hp': value, 'attack': value, ...}", etc.
	bulbasaur_stats = json.loads(bulbasaur_row['stats'].replace("'", '"'))

	# Create the Pokémon object for Bulbasaur
	bulbasaur = Pokemon(
	    bulbasaur_row['name'],  # If there's no unique ID, using name as the identifier
	    bulbasaur_types,
	    5,  # Assuming base level is 5; change as necessary
	    bulbasaur_stats['hp'],
	    bulbasaur_stats['attack'],
	    bulbasaur_stats['defense'],  # Make sure to spell 'defense' as it is in your CSV
	    bulbasaur_stats['special-attack'],
	    bulbasaur_stats['special-defense'],
	    bulbasaur_stats['speed']
	)

	# Now you have a Pokémon object for Bulbasaur
	return bulbasaur

def create_all_pokemon():
	# Initialize an empty list to hold all the Pokémon objects
	all_pokemon = []

	# Iterate over each row in the DataFrame
	for index, row in pokemon_data.iterrows():
	    # Parse the 'types' and 'stats' fields from strings to actual lists/dicts
	    pokemon_types = json.loads(row['types'].replace("'", '"'))
	    pokemon_stats = json.loads(row['stats'].replace("'", '"'))

	    # Create a Pokémon object using the data from the current row
	    pokemon = Pokemon(
	        row['name'],  # If there's no unique ID, using name as the identifier
	        pokemon_types,
	        5,  # Assuming base level is 5; change as necessary
	        pokemon_stats['hp'],
	        pokemon_stats['attack'],
	        pokemon_stats['defense'],
	        pokemon_stats['special-attack'],
	        pokemon_stats['special-defense'],
	        pokemon_stats['speed']
	    )

	    all_pokemon.append(pokemon)
	return all_pokemon

#print(create_all_pokemon())
