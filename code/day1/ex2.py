keys = range(6)
values = [i**2 for i in keys]
#d = dict(zip(keys, values))

d = { i: i**2 for i in range(6) }

print d

#print d
rd = dict(zip(values, keys))


square = 25


for key in keys:
	if d[key] == square:
		print 'Success, the key is {}'.format(key)
		break
else:
	print 'Not in dictionary'

try:
	print rd[square]
except:
	print 'not in dict'
