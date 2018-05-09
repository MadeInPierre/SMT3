import pygame

class ScreenStates():
    INACTIVE = 0
    ACTIVE   = 1

class Component(Object):
	def __init__(self, size):
		self.size = size
		self.children = []

	def add(self, child):
		self.children.append(child)

	def update(self, window, events):
		result = False

		for child in self.children:
			result = child.update(window, events)

			if result:
				return result

		return False

class Screen(Component):
    '''
		Called when the screen gain focus
    '''
    def focus(self):
    	pass

    '''
		Called when the screen loose focus
    '''
    def unfocus(self):
    	pass

    def update(self, window, events):
    	super(Screen, self).update(window, events)
        return False

class Button(Component):
	'''
		Create button with images for specific states
	'''
	def __init__(self, content, position, size):
		super(Button, self).__init__(size)

		if isinstance(content, pygame.Surface):
			self.image = pygame.transform.scale(content, size)
		else:
			color, text = content

			self.image = pygame.Surface(size)
			self.image.fill(color)

		self.position = position

	def update(self, window, events):
		# TODO manage click

		window.blit(self.image, self.position)

		return False


class EventButton(Button):
	def __init__(self, image, position, size, callback):
		super(EventButton, self).__init__(image, position, size)

		# Called when clicked
		self.callback = callback

	def update(self, window, events):
		# TODO manage click

		window.blit(self.image, self.position)

		return False



class ScreenChangeButton(Button):
	def __init__(self, image, position, size, screen=True):
		super(ScreenChangeButton, self).__init__(image, position, size)

		# Screen displayed on click
		self.screen = screen

	def update(self, window, events):
		# TODO manage click
		if False:
			return self.screen

		window.blit(self.image, self.position)

		return False
