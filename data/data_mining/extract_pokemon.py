import requests
import time
import pandas as pd

def single_pokemon():
	# Fetch data for Bulbasaur
	response = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
	data = response.json()

	# Extract relevant information
	name = data["name"]
	types = [t["type"]["name"] for t in data["types"]]
	stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
	moves = [move["move"]["name"] for move in data["moves"]]

	# Print the extracted data
	print(f"Name: {name}")
	print(f"Types: {types}")
	print(f"Stats: {stats}")
	print(f"Moves: {moves}")

def count_pokemon():
	# Fetch the total number of Pokemon
	response = requests.get("https://pokeapi.co/api/v2/pokemon")
	total_pokemon = response.json()["count"]
	return total_pokemon

# Function to fetch data for a single Pokemon
def fetch_pokemon_data(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    data = response.json()
    return {
        "name": data["name"],
        "types": [t["type"]["name"] for t in data["types"]],
        "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
        "moves": [move["move"]["name"] for move in data["moves"]],
    }

def collect_all_pokemon(total_pokemon):
	all_pokemon_data = []
	for pokemon_id in range(1, total_pokemon + 1):
		try:
			pokemon_data = fetch_pokemon_data(pokemon_id)
			all_pokemon_data.append(pokemon_data)
			print(f"Fetched data for Pokémon ID: {pokemon_id}")
			#time.sleep(0.5)  # Adjust the sleep time as needed
		except Exception as e:
			print(f"Failed to fetch data for Pokémon ID: {pokemon_id}. Error: {e}")
	    #time.sleep(1)  # Delay to respect the API's rate limit

	return all_pokemon_data

def store_data():
	total_pokemon = count_pokemon()
	all_pokemon_data = collect_all_pokemon(total_pokemon)

	# Convert the list of dictionaries to a DataFrame
	pokemon_df = pd.DataFrame(all_pokemon_data)

	# Normalize and clean data if necessary
	# For example, ensure all stats are integers
	pokemon_df['stats'] = pokemon_df['stats'].apply(lambda x: {k: int(v) for k, v in x.items()})

	# Inspect the data for any inconsistencies or missing values
	#print(pokemon_df.head())  # Print the first few rows to inspect the data
	#print(pokemon_df.isnull().sum())  # Check for missing values

	# Save the cleaned data to a CSV file
	pokemon_df.to_csv('pokemon_data.csv', index=False)