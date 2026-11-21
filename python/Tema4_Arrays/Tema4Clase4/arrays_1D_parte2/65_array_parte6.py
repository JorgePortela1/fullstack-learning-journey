#Multiplica los elementos de ambos arrays, elemento por elemento.
# resuelvelo usando un operador y despues con un funcion numpy


import numpy as np

rng = np.random.default_rng(seed=42)

array1 = rng.integers(1,101,15)

array2 = rng.random(15)

print(array1)
print("----")
print(array2)

multiplica = array1 * array2

print(multiplica)
print("-----")

multiplica_numpy = np.multiply(array1, array2)
print(multiplica_numpy)
