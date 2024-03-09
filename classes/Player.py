class Player:
	def __init__(self, name):
		self.name = name
		self.pokemon = []

	def capture_pokemon(self, wild_pokemon):
		self.pokemon.append(wild_pokemon)

	def select_pokemon(self, pokemon):
		self.pokemon = pokemon