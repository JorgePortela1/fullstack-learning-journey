# Cambia la forma del array para que tenga estructura filas columnas 

import numpy as np

user_long = int(input("Introduce la longitud del array: "))

if user_long%2 == 0 and user_long > 0:

	print("Bien hecho, el numero debe ser par. ")
	array = np.ones(user_long, dtype=int)
	columnas = user_long // 2
	array = array.reshape(2,columnas)
	print(array)
	
else:
	print("No, el numero debe ser par")



# print(user_long)

