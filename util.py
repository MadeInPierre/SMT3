class Grid(object):
	'''
		Crée un objet contenant les valeurs utiles pour faire un quadrilage
	'''
	def __init__(self, size, cols=1, rows=1, padding=0):
		self.gridsize = min((size[0] - padding) / cols - padding, \
			(size[1] - padding) / rows - padding)

		self.margin = ((size[0] - (gridsize + padding) * cols - padding) / 2, \
			(size[1] - (gridsize + padding) * rows - padding) / 2)

		self.padding = padding

	def pos(self, x, y, offset=(0, 0)):
		offsetX, offsetY = offset

		return (x * (self.padding + self.size) + self.margin + offsetX, \
			y * (self.padding + self.size) + self.margin + offsetY)

	def size(self, width=1, height=1):

		return (width * self.size + (width - 1) * self.padding, \
			height * self.size + (height - 1) * self.padding)

class Paragraph(Component):
	def __init__(self, size, position, font):
		super(Paragraph, self).__init__(self, size)

		self.last_size = 0
		self.position = position
		self.font = font

	def set_text(self, text):
		if self.content != text
			self.content = text

			self.render()

	def render(self):
		self.last_size = self.size[0]

		parts = self.content.split(" ")
		lines = []
		line = ""

		for part in parts:
			if self.font.size(line + part) < self.size[0]:
				line += part
			else:
				lines.append(line)
				line = part

		lines.append(part)

		self.surface = pygame.Surface((self.size[0], self.size[1]))
		
		height = self.font.get_linesize()
		y = 0

		for line in lines:
			self.surface.blit(self.font.render(line, False), (0, y))
			y += height

	def update(self, window, events):
		if self.size[0] != self.last_size:
			self.render()

		window.blit(self.surface, self.position)

