# Crea un array lleno de 1s con una longitud dada por el usuario

import numpy as np

user_size = int(input("Elige el tamano de la matriz identidad: "))

matriz_id = np.eye(user_size)

print(matriz_id)
