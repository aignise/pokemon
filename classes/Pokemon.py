class Pokemon:
	def __init__(self, name, level):
		self.name = name
		self.level = level
		self.moves = []

	def stats(self, hp, attack, defence):
		self.hp = hp
		self.attack = attack
		self.defence = defence