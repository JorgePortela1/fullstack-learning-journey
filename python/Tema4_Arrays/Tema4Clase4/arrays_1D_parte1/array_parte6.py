'''
Encuentra los elementos comunes entre array1 y array2 
y entre array2 y array2_invertido
(investiga el uiso de itersect1d de numpy)
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

interseccion_a1y2 = np.intersect1d(array_1, array_2)
print(f"Los elementos comunes entre array1 y array2 son: {interseccion_a1y2}")

interseccion_a2y2inv = np.intersect1d(array_2,array2_invertido )
print(f"Los elementos comunes entre array2 y array2 invertido es: {interseccion_a2y2inv}")
