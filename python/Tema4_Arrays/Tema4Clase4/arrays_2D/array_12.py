# Cambia la forma del array para que tenga estructura filas columnas 

import numpy as np

user_size = int(input("Elige el tamano de las matrices: "))


if user_size > 0:
	array = np.ones([user_size,user_size])
	print(array)
	matriz_id = np.eye(user_size)
	print(matriz_id)

print("concatenar")

resultado1 = np.concatenate((array, matriz_id))
print("   ---  sin indicar axis  ")
print(resultado1)

resultado2 = np.concatenate((array, matriz_id), axis=0)
print("    --- con axis 0    ")
print(resultado2)

resultado3 = np.concatenate((array, matriz_id),axis=1)
print("    --- con axis 1    ")
print(resultado3)

print(" --- vstack() ---")
resultado4 = np.vstack((array, matriz_id))
print(resultado4)

print(" --- hstack() ---")
resultado5 = np.hstack((array, matriz_id))
print(resultado5)

print("Con este ejercicio, me doy cuenta que: ")
print(" concatenate with no axis or axis=0 ES IGUAL A vstack()")
print(" concatenate with axis=1 ES IGUAL A hstack()")
