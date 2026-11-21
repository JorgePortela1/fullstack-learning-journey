#Suma los elementos de ambos arrays, elemento por elemento.
# resuelvelo usando un operador y despues con un funcion numpy


import numpy as np

rng = np.random.default_rng(seed=42)

array1 = rng.integers(1,101,15)

array2 = rng.random(15)

print(array1)
print("----")
print(array2)

suma = array1 + array2

print(suma)
print("-----")

suma_numpy = np.add(array1, array2)
print(suma_numpy)
