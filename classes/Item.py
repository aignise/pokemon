class Item:
	def __init__(self, name):
		self.name = name
		
	def map(self):
		pass

	def pokedex(self):
		pass

	def running_shoes(self):
		pass

	def bike(self):
		pass:


class Repel(Item):
	def __init__(self, repel_type, repel_steps):
		self.repel_type = repel_type
		self.repel_steps = repel_steps


class Pokeball(Item):
	def __init__(self, pokeball_type, catchrate):
		self.pokeball_type = pokeball_type
		self.catchrate = catchrate

class Potion(Item):
	def __init__(self, potion_type, heal, status_change=None):
		self.pokemon_type = potion_type
		self.heal = heal
		self.status_change = status_change