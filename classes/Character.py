class Character:
	def __init__(self, name):
		self.name = name

	def speak(self, say):
		self.say = say

###########################
class NurseJoy(Character):
	def __init__(self, town):
		self.town = town

class OfficerJenny(Character):
	def __init__(self, town):
		self.town = town

########################### 
class Trainer(Character):
	def __init__(self, trainer_type, trainer_pokemon):
		self.trainer_type = trainer_type
		self.pokemon = trainer_pokemon

class TeamRocket(Trainer):
	def __init__(self, name, pokemon):
		self.name = name
		self.pokemon = pokemon