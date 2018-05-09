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
		for child in self.children:
			child.update(window, events)

		pass

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
	def __init__(self, image, position, size, callback):
		super(Button, self).__init__(size)

		self.image = pygame.transform.scale(image, size)
		self.position = position

		# Called when
		self.callback = callback

	def update(self, window, events):
		window.blit(self.image, self.position)
		
		super(Button, self).update(window, events)
