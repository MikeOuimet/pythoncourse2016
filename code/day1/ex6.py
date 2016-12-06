def IsInt(thing):
	try:
		int(thing)
		if type(thing) ==int:
			return 'True, {} is an Int'.format(thing)
		else:
			return 'False, {} is a {}'.format(thing, type(thing))
	except:
		return 'False, {} is a {}'.format(thing, type(thing))


print IsInt(10)

print IsInt(1.0)

print IsInt('banana')
