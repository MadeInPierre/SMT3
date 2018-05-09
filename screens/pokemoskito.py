from ..bases import Screen
import pygame

'''
	Return largest size of a square in a grid with given rows and columns and the
	associated padding
'''
def grid(size, cols, rows, padding=0):
	gridsize = min((size[0] - padding) / cols - padding, \
		(size[1] - padding) / rows - padding)

	margin = ((size[0] - (gridsize + padding) * cols - padding) / 2, \
		(size[1] - (gridsize + padding) * rows - padding) / 2)

	return (gridsize, margin, padding)

def position(grid, pos):
	size, margin, padding = grid
	x, y = pos

	return (x * (padding + size) + margin, \
		y * (padding + size) + margin)

def size(grid, width=1, height=1):
	size, margin, padding = grid

	return (width * size + (width - 1) * padding, \
		height * size + (height - 1) * padding)

def add(pos1, pos2):
	x1, y1 = pos1
	x2, y2 = pos2

	return (x1 + x2, y1 + y2)

class Pokemoskito(Screen):
	def __init__(self, size):
		super(Pokemoskito, self).__init__(size)

		self.grid = grid(size, 3, 3)
		self.buttongrid = grid(size(self.grid), 3, 2, 20)

		self.actions = []

		#self.ui = pygame.image.load("assets/pokemoskito/ui.png")

		# Initialize buttons
		for x in range(2):
			for y in range(2):
				self.add(
					EventButton(((50*x+100,50*y+100,150),),
					add(position(self.grid, 1, 3),
					position(self.buttongrid, x, y)),
					size(self.buttongrid, 1, 1)), lambda: print("oui")
				)

	def focus(self, player):
		self.player = player
		self.enemy = Enemy()
		# TODO generate random monster
		pass

	def update(self, window, events):

		pass


class Entity(object):
	def __init__(self, texture, size):
		# Life in percent
		self.life = 100
		self.texture = pygame.transform.resize(texture, size)

class Enemy(Entity):
	def __init__(self, size):
		# TODO load random texture
		surface = pygame.Surface(size)
		surface.fill((255, 150, 200))

		super(Enemy, self).__init__(surface, size)

