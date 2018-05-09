from ..bases import Screen

class Pokemoskito(Screen):
	def __init__(self):
		super(Pokemoskito, self).__init__()

	
	def focus(self):
		# TODO generate random monster
		pass

	def update(self, window, events):
		pass


class Entity(object):
	def __init__(self):
		# Life in percent
		self.life = 100

class Player(Entity):
	def __init__(self):
