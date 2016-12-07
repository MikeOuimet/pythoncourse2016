class Rectangle:
	def __init__(self, width = 10, height = 20):
		self.width = width
		self.height = height

	def get_area(self):
		return self.width*self.height


class Square(Rectangle):
	def __init__(self, width = 10, height = 10):
		try: 
			assert width == height
		except:
			height = width
			print 'I set height equal to width'
		self.width = width
		self.height = height


s = Square(11, 10)

print 'The width is {}, {} , {}'.format(s.width)
print 'The height is {}'.format(s.height)
print 'The area is {}'.format(s.get_area())