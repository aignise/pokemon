class Pokemon:
	def __init__(self, pokemon_id, name, pokemon_type, level):
		self.pokemon_id = pokemon_id
		self.name = name
		self.pokemon_type = pokemon_type
		self.level = level
		self.moves = []

	def stats(self, hp, attack, defence, speed):
		self.hp = hp
		self.attack = attack
		self.defence = defence
		self.speed = speed

	def evolve(self):
		pass