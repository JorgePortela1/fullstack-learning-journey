'''
Crea un array lleno de 1s con una longitud dada por el usuario

'''

import numpy as np

user_long = int(input("Decide la longitud de tu array: "))

user_array = np.ones(user_long, dtype=int)
print(user_array)
