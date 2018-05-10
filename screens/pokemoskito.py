<<<<<<< HEAD
from ..bases import Screen
from ..util import Grid

import pygame

=======
from bases import Screen
>>>>>>> master

class Pokemoskito(Screen):
	def __init__(self, size):
		super(Pokemoskito, self).__init__(size)

		self.grid = Grid(size, 3, 3)
		self.buttongrid = Grid(size(self.grid), 3, 2, 20)

		self.actions = []
		self.turn = 0
		
		#self.ui = pygame.image.load("assets/pokemoskito/ui.png")

		# Initialize buttons
		for x in range(2):
			for y in range(2):
				self.add(
					EventButton(
						((50*x+100,50*y+100,150),),
						self.grid.pos(1, 3, self.buttongrid.pos(x, y)),
						self.buttongrid.size(),
						lambda: print("oui")
					)
				)

	def focus(self, player):
		self.player = player
		self.enemy = Enemy()
		# TODO generate random monster
		pass

	def content(self, window, position, entity):
		x, y = self.grid.pos(position)
		size = self.grid.size(2, 1)

		#window.text(entity.name, (x, y))
		#window.rect((x, y + size * 4 / 6), (size * entity.life / 100, size / 6))

	def update(self, window, events):
		# Affichage de l'ui de base
		#window.blit(self.ui, (0, 0))

		# Affichage des personnages
		window.blit(self.enemy.texture, self.grid.pos(3, 1))
		window.blit(self.player.texture, self.grid.pos(1, 2))

		# Affichage des métadonnées
		self.content(window, (1, 1), self.player)
		self.content(window, (3, 2), self.enemy)

		# Et des enfants
		super(Pokemoskito, self).update(window, events)


class Entity(object):
	def __init__(self, name, texture, size):
		# Life in percent
		self.life = 100
		self.name = name
		self.texture = pygame.transform.resize(texture, size)

class Enemy(Entity):
	def __init__(self, name, size):
		# TODO load random texture
		surface = pygame.Surface(size)
		surface.fill((255, 150, 200))

		super(Enemy, self).__init__(name, surface, size)
