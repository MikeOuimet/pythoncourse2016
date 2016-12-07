class Rectangle:
	def __init__(self, width = 10, height = 20):
		self.width = width
		self.height = height

	def get_area(self):
		return self.width*self.height


class Square(Rectangle):
	def __init__(self, *args, **kwds):
		Rectangle.__init__(self, *args, **kwds)
		try: 
			assert self.width == self.height
		except:
			self.height = self.width
			print 'I set height equal to width'
		#self.width = width
		


s = Square(width =11, height = 11)

print 'The width is {}'.format(s.width)
print 'The height is {}'.format(s.height)
print 'The area is {}'.format(s.get_area())