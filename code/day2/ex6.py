import numpy as np

a = np.arange(8).reshape(4, -1)


print a, '\n'

sub = a - a[:, None]

times = sub**2

vec =  np.sum(times, axis=2)
print vec, '\n'

print np.sum((a - a[:, None])**2, axis = 2), '\n'


#not elegant way
'''
final = []
for i in range(4):
	minn = 100
	idx = 100
	for j in range(4):
		if vec[i, j] < minn and i != j:
			minn = vec[i,j]
			idx = j
	final.append(idx)

print final
'''


### or 
i, j = np.where(vec ==0)
vec[i,j] = 10000

print np.argmin(vec, axis = 1)