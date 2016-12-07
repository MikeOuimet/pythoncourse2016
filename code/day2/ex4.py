import numpy as np

size = 5
A = np.random.rand(size,size)

print A,   '\n'


b = np.fromfunction(lambda i,j: i != j, (5,5))

for spot in range(size):
	A[spot, spot] = np.sum(A[spot, b[spot, :]])/(size-1)

print A,   '\n'


B = A.copy()
for spot in range(size):
	B[spot, spot] = np.sum(B[spot, np.fromfunction(lambda i: i !=spot , (5,))])/(size-1)

print B,   '\n'


C = np.array([[1, 2], [3, 4], [5,6]])

print C

D = np.c_[C, C[:,0]**3]

print D
