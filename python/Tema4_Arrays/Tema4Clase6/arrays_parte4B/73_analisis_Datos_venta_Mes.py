'''
Ventas de un año: cada fila es una venta, con 3 columnas: fecha, monto y categoria. calcular monto total de cada mes
'''
import numpy as np
ventas = np.array([
	['2022-01-01', 100, 'ropa'],
	['2022-01-02', 200, 'alimentos'],
	['2022-01-03', 150, 'ropa'],
	['2022-02-01', 120, 'alimentos'],
	['2022-02-02', 180, 'electronicos'],
	['2022-02-03', 200, 'alimentos'],
	['2022-03-01', 90, 'ropa'],
	['2022-03-02', 110, 'electronicos'],
	['2022-03-03', 100, 'alimentos']
])
# extraer las fechas en una variable
fechas = np.array([venta[0] for venta in ventas])

# extraer los meses de las fechas
# cambiamos a entero el string de los meses para facilitar 
meses = np.array([int(mes[5:7]) for mes in fechas])

# extraemos montos
monto = np.array([int(venta[1]) for venta in ventas])

# Prueba de la creacion de dos listas que comparten informacion mediante la posicion
print(meses, monto)

# Creamos una lista con los nombres de los meses
nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# inicializamos la lista de los resultados para usarla en la suma de los montos por meses
resultado = []

for i in range(1,13):
	# separamos de la lista monto, los mismos elementos que comparte con la lista meses
	filtro = (meses == i)
	monto_por_mes = np.array(monto[filtro])
	# sumamos los montos del mes y la almacenamos en una lista
	total_monto_mes = np.sum(monto_por_mes)
	# y los añadimos a la lista de resultados
	resultado.append(int(total_monto_mes))
	
# Recorremos las listas e imprimimos los resultados deseados
for i in range(12):
	print("Las ventas del 2022: ", nombre_meses[i], resultado[i])
