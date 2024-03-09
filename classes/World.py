class World:
	def __init__(self, region):
		self.region = region

	def fence(self):
		pass

	def road(self):
		pass

	def trees(self):
		pass

	def signs(self, message):
		self.message = message

	def pc(self):
		pass

################################
class Town(World):
	def __init__(self, town_name):
		self.town_name = town_name

##################################
class Building(World):
	def __init__(self, building_type):
		self.building_type = building_type

	def pokemon_centre(self, town):
		self.town = town

	def pokemart(self, town):
		self.town = town

	def gym(self, town):
		self.town = town

################################
class Terrain(World):
	def __init__(self):
		pass

	def grass(self):
		pass

	def water(self):
		pass

	def mud(self):
		pass

#################################
class Battlefield(World):
	def __init__(self):
		pass