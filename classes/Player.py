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

count = 1
for i in range(31):
	print(count)
	count*=2