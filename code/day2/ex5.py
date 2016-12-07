import numpy as np

'''
a = np.array([1, 2])

b = np.array([3, 4, 5])

A, B = np.meshgrid(a, b)


print A, '\n',  B, '\n'


print A * B, '\n'


print a* b[:, None], '\n'
'''

n_d = np.arange(3)
n_n = np.arange(6)
n_p = np.arange(26)

all_combos =  10*n_d + 5*n_n[:, None] + 1*n_p[:, None, None]

print np.sum(all_combos == 25)
