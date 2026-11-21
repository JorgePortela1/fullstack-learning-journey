'''
Suma todos los elementos del array 2 usando un bucle y despues
usando un metodo de numpy. compara los resultados

'''

import numpy as np

array_1 = np.zeros([8])

array_1.fill(2)

print(array_1)


array_2 = np.zeros(5)
array_2 = np.arange(2,11,2)

print(array_2)


# suma del array2 con metodo bucle
total = 0

for i in range(5):
	total = total + array_2[i]

print(f"La suma del array 2 usando un bucle es {total}")

suma = array_2.sum()
print(f"La suma del array 2 usando .sum() es {suma}")
