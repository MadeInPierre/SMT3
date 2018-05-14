from bases import Screen
from ..util import Grid
from collections import deque
import pygame


class Pokemoskito(Screen):
	def __init__(self, size):
		super(Pokemoskito, self).__init__(size)

		self.grid = Grid(size, 3, 3)
		self.buttongrid = Grid(size(self.grid), 3, 2, 20)
		self.messages = Messages()
		
		self.actions = [
			Action("Spit", 20, {"armor": -5}),
			Action("Intercourse break", -10, {"armor": 5}, 0),
			Action("Space Dog", 25),
			Action("AFK", 0, {"armor": 30})
		]
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
						self.createLambda(actions[x + 2 * y])
					)
				)
				
		self.add(self.messages)
		
	def createLambda(self, action):
		return lambda: if self.messages.disabled: action.apply(self.player, self.enemy)
	
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
	

class Messages(Paragraph):
	def __init__(self, size, position, font):
		self.messages = deque([])
		
		self.current = ""
		self.index = 0
		self.disabled = True

		super(Messages, self).__init__(size, position, font)
		
	def add(self, message):
		self.messages.appendleft(message)
		self.disabled = False
	
	def next(self):
		self.index = 0
		
		if len(self.messages) == 0:
			self.disabled = True
			return ""
			
		return self.messages.pop()
	
	def update(self, window, events):
		# touche entree
		if False and self.index == len(self.current):
			self.current = next()
			
		if not self.disabled:
			if self.index < len(self.current):
				# more delay?
				index += 1

				self.set_text(self.current[:index])
				
			super(Messages, self).update(window, events)

class Action(object):
	def __init__(self, name, damage=0, buff={}, target=1):
		self.name = name
		self.damage = damage
		self.buffs = buffs
		self.target = target
		
	def apply(self, source, enemy, messages):
		target = self.target == 0 ? source : enemy;
		
		messages.add(source.name + " uses " + self.name)
		
		# Apply damage
		if self.damage:
			target.damage(self.damage, messages)
		
		# Then (de)buffs
		if self.buffs:
			for name in self.buffs:
				target.stats[name] = self.buffs[name]

class Entity(object):
	def __init__(self, name, texture, size):
		# Life in percent
		self.life = 100
		self.name = name
		self.texture = pygame.transform.resize(texture, size)
		
		# Detailed stats
		self.stats = {
			armor: 10,
			poison: 0
		}
		
	def turnover(self):
		if self.stats.poison:
			self.life -= self.stats.poison

	def damage(self, damages, messages):
		# Heal
		if damages < 0:
			# We do not care about having more than 100% life :3
			self.life -= damages
			messages.add(self.name + " recovered " + damages + " HP")
		else:
			# With enough armor, damages heals
			dmg = damages * (50 - self.stats.armor) / 100
			
			self.life -= dmg
			messages.add(self.name + " lost " + dmg + " HP")
	
	def add(self, stat, value):
		if self.stats[stat]:
			self.stats[stat] += value
		else:
			self.stats[stat] = value
			
class Enemy(Entity):
	def __init__(self, name, size):
		# TODO load random texture
		surface = pygame.Surface(size)
		surface.fill((255, 150, 200))

		super(Enemy, self).__init__(name, surface, size)