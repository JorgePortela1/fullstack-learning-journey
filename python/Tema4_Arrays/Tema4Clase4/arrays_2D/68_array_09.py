# Crea un array lleno de 1s con una longitud dada por el usuario

import numpy as np

user_long = int(input("Introduce la longitud del array: "))

array = np.ones(user_long, dtype=int)

print(array)
