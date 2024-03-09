class Character:
	def __init__(self, name):
		self.name = name

	def speak(self, say):
		self.say = say

class Trainer(Character):
	def __init__(self, trainer_type, trainer_pokemon):
		self.trainer_type = trainer_type
		self.pokemon = trainer_pokemon
