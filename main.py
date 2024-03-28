from classes.Player import Player
from classes.Pokemon import Pokemon

ash = Player('ash',[])
#print(player1.name)

bulbasaur = Pokemon(
    'bulbasaur',  # If there's no unique ID, using name as the identifier
    ['grass'],
    5,  # Assuming base level is 5; change as necessary
    100,
    50,
    50,  # Make sure to spell 'defense' as it is in your CSV
    50,
    50,
    50
)

ash.capture_pokemon(bulbasaur)
#ash.capture_pokemon(bulbasaur)
print([pokemon.name for pokemon in ash.pokemon])
print(bulbasaur.level)
bulbasaur.level_up()
print(bulbasaur.level)