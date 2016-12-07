import numpy as np


size = 10

A = np.fromfunction(lambda i,j: (i<=j), (size,size)).astype(int)

print A.dtype
print A

B = np.fromfunction(lambda i,j: 1*(i<=j), (size,size), dtype = int)

print B.dtype

pop_vec = range(1, size**2)
for i in range(size):
	for j in range(size):
		if B[i,j] == 1:
			B[i,j] = pop_vec.pop(0)
print B


