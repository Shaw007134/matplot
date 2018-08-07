from random import randint

class Die():
	"""create a die class"""
	
	def __init__(self, num_sides=6):
		"""default is six sides"""
		self.num_sides = num_sides
		
	def roll(self):
		"""return a random value between 1 and 6"""
		return randint(1, self.num_sides)
		
		
