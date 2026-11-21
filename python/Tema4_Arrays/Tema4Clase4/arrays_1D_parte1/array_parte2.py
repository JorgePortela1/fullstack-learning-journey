'''
haz que todos los elementos de este array sean igual a 2
'''

import numpy as np

array_1 = np.zeros([8])

array_1.fill(2)

print(array_1)

print("   ---   ")

# Esta es la forma que la profesora explica:

array_1[:] = 2
print(array_1)
