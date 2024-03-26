import requests
import time
import pandas as pd

# Fetch the total number of moves
def count_moves():
    response = requests.get("https://pokeapi.co/api/v2/move")
    total_moves = response.json()["count"]
    return total_moves

# Function to fetch data for a single move
def fetch_move_data(move_id):
    response = requests.get(f"https://pokeapi.co/api/v2/move/{move_id}")
    move_data = response.json()
    return {
        "name": move_data.get("name", ""),
        "type": move_data["type"]["name"] if move_data.get("type") else "",
        "power": move_data.get("power"),
        "accuracy": move_data.get("accuracy"),
        "pp": move_data.get("pp"),
    }

# Collect data for all moves
def collect_all_moves(total_moves):
    all_moves_data = []
    for move_id in range(1, total_moves + 1):
        try:
            move_data = fetch_move_data(move_id)
            all_moves_data.append(move_data)
            print(f"Fetched data for move ID: {move_id}")
            time.sleep(0.5)  # Sleep to avoid hitting rate limits
        except Exception as e:
            print(f"Failed to fetch data for move ID: {move_id}. Error: {e}")
    return all_moves_data

def store_data():
    total_moves = count_moves()
    all_moves_data = collect_all_moves(total_moves)

    # Convert the list of move data to a pandas DataFrame
    moves_df = pd.DataFrame(all_moves_data)

    # Inspect the first few rows to ensure it looks correct
    print(moves_df.head())

    # Save the DataFrame to a CSV file
    moves_df.to_csv('pokemon_moves.csv', index=False)

store_data()
