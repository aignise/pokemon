class Pokemon:
	def __init__(self, pokemon_id, name, pokemon_type, level):
		self.pokemon_id = pokemon_id
		self.name = name
		self.pokemon_type = pokemon_type
		self.level = level
		self.moves = []

	def base_stats(self, hp, attack, defence, speed):
		self.hp = hp
		self.attack = attack
		self.defence = defence
		self.speed = speed

	def gain_experience(self, xp):
		self.xp = xp

	def level_up(self):
		self.level += 1

	def evolve(self):
		pass