class Pokemon:
	def __init__(self, pokemon_id, name, pokemon_type, level, hp, attack, defence, special_attack, special_defence, speed):
		self.pokemon_id = pokemon_id
		self.name = name
		self.pokemon_type = pokemon_type
		self.level = level
		self.moves = []
		self.hp = hp
		self.attack = attack
		self.defence = defence
		self.special_attack = special_attack
		self.special_defence = special_defence
		self.speed = speed

	def gain_experience(self, xp):
		self.xp = xp

	def level_up(self):
		self.level += 1

	def learn_move(move):
		self.moves.append(move)

	def evolve(self):
		pass

	def attack(self, move):
		attack_power = self.level * self.attack * move

	def take_damage(self, attack):
		pass