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

# Creamos listas con los meses
meses = np.array(clima[:,3])
print(meses)
# creamos las listas con los demas datos
temperatura = np.array(int(clima[:,0]))
humedad = np.array(int(clima[:,1]))
presion = np.array(int(clima[:,2]))

# Creamos la lista con los nombres de los meses
nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Inicializamos una lista para agrupar datos:
conjunto_datos_mes = []
# Creamos el filtro, para agrupar los datos en meses
for i in range(1,13):
	filtro = clima[:,3] == i
	datos_por_mes = np.array(clima[filtro])
	suma_temperatura = np.sum(temperatura)
	suma_humedad = np.sum(humedad)
	suma_presion = np.sum(presion)
	
	
	conjunto_datos_mes.append(datos_por_mes)
	conjunto_datos_mes.append(suma_temperatura)
	conjunto_datos_mes.append(suma_humedad)
	conjunto_datos_mes.append(suma_presion)	
	
	print("----------")

print(conjunto_datos_mes)
