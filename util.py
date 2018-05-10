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

	def pos(self, pos, offset=(0, 0)):
		x, y = pos
		offsetX, offsetY = offset

		return (x * (self.padding + self.size) + self.margin + offsetX, \
			y * (self.padding + self.size) + self.margin + offsetY)

	def size(self, width=1, height=1):

		return (width * self.size + (width - 1) * self.padding, \
			height * self.size + (height - 1) * self.padding)