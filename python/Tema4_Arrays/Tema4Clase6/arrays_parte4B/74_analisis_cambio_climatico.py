'''
Conjunto de datos --> temperatura, humedad y presion atmosferica y mes del año
calcular temperatura promedio por cada mes / humedad promedio / presion atmosferica promedio por año
'''

import numpy as np

clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

# extraer los meses

meses = clima[:,3]


# extraer las columnas de temperatura, humedad y presion atmosferica
temperatura = clima[:,0]
humedad = clima[:,1]
presion_atmosferica = clima[:,2]

# calcular las medias de cada columna, para eso, tener un array donde se guardaran las medias
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# recorrer los arrays, con el mismo codigo-mes y calcular la media
for i in range(12):
	temp_mes[i] = np.mean(temperatura[meses == i+1])
	humedad_mes[i] = np.mean(humedad[meses == i +1])
	presion_mes[i] = np.mean(presion_atmosferica[meses == i+1])
	
	print("----------")
	print(f"La temperatura del mes {i+1} es {temp_mes[i]}")
	print(f"La humedad media del mes {i+1} es {humedad_mes[i]}")
	print(f"La presion media del mes {i+1} es {presion_mes[i]}")
	print("----------")
	
	
temp_anual = np.mean(temperatura)
humedad_anual = np.mean(humedad)
presion_anual =	np.mean(presion_atmosferica)

print(f"Las medias anuales de las temperaturas es {temp_anual}")
print(f"Las medias anuales de la humendad es {humedad_anual}")
print(f"Las medias anuales de la presion atmosferica es {presion_anual}")
