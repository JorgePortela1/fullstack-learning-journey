'''
conjunto de calificaciones de una clase de un curso
cada estudiante, 4 calificaciones: 2 examenes, 1 trabajo final, 1 participacion en clase
calcular nota final: examen 30%, trabajo final: 30%, participacion 10%.
usa numpy, crea 4 columnas y n filas, donde n es el numero de estudiantes
crear nuevo array con una columna donde se almacenan las notas

8,7,9,10
6,8,7,9
9,9,8,8
7,6,6,7
10,9,10,10



'''
# importar numpy

import numpy as np

# Crear la matriz con las calificacions

calificaciones = np.array([
	[8,7,9,10],
	[6,8,7,9],
	[9,9,8,8],
	[7,6,6,7],
	[10,9,10,10]
])

print(f"{calificaciones}\n")

# nota final: 30%,30%,30%,10%

porcentajes = np.array([
	0.3,0.3,0.3,0.1
])

notas_finales = calificaciones * porcentajes

print(f"{notas_finales}\n")

total = notas_finales.sum(axis=1)

print(f"{total}\n")
