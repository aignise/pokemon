class Player:
	def __init__(self, name, pokemon):
		self.name = name
		self.pokemon = pokemon

	def badges(self, badges):
		self.badges = badges

	def capture_pokemon(self, wild_pokemon):
		self.pokemon.append(wild_pokemon)

	def select_pokemon(self, pokemon):
		self.pokemon = pokemon

	def bagpack(self, items):
		self.items = items

	def money(self, amount):
		self.amount = amount

"""
players = []
for i in range(0,5):
	player = Player(i,['squirtle','charmander','pikachu'])
	players.append(player)

print(players)
"""