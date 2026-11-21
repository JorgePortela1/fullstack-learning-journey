'''
Revierte array_2 y guardalo en una variable independiente

'''

import numpy as np

array_1 = np.zeros([8])

array_1.fill(2)

print(array_1)

array_2 = np.arange(2,11,2)

print(array_2)

# invertir array 2

array2_invertido = array_2[::-1]

print(array2_invertido)
