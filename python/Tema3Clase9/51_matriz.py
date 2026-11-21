# Recorrido de una matriz, y el calculo de sus filas y columnas

M = [[1,2,3],
	[4,5,6],
	[10,11,12],
	[7,8,9]]

# tamano de las filas, para crear variable y poder recorrerla
tamaño_filas = len(M)

# tamano de las columnas(numero de elementos por fila), para poder recorrerla tambien
tamaño_columnas = len(M[0])

# variables que necesitan estar inicializadas

sumas_de_filas = [] # para ir almacenando las sumas de cada una de las filas
suma_f_mayor = 0 # para guardar la fila mas alta

for fila in range(tamaño_filas): # empezamos a recorrer la Matriz de izq a derecha y arriba a abajo
	suma_fila = sum(M[fila]) # guardamos en una variable la suma de los elementos de la fila
	# print(suma_fila) # comprobamos si suman los elementos de cada fila
	sumas_de_filas.append(suma_fila) # anadimos esos resultados en una nueva lista
	for suma in sumas_de_filas:
		if suma > suma_f_mayor:
			suma_f_mayor = suma # se guarda en una variable la suma mas alta
			indice_fila_mayor = fila # se guarda la posicion de donde esta la fila mas alta

'''			
print(sumas_de_filas) # lista de las sumas de cada fila
print(suma_f_mayor) # suma total de la fila mas alta
print(indice_fila_mayor) # indice en la M donde esta la fila mas larga
'''
lista_columnas = [] # inicializamos esta lista, para ir anadiendo las columnas en forma de listas
sumas_de_columnas = [] # inicializamos la lista donde estan las sumas de cada columna
suma_c_mayor = 0
indice_c_mayor = 0

for columna in range(tamaño_columnas): # empezamos a recorrer las columnas de la M
	lista_columna = [] # inicializamos la lista provisional con los elementos de la columna
	for fila in range(tamaño_filas): # recorremos la M entera
		lista_columna.append(M[fila][columna]) # creamos la lista de una columna
		suma_de_columna = sum(lista_columna) # averiguamos la suma de la columna
		if suma_de_columna > suma_c_mayor: # comprabamos si la suma es la mas alta
			suma_c_mayor = suma_de_columna # al ser la mas alta, la guardamos en una variable
			indice_c_mayor = columna # y averiguamos cual es el indice de donde esta la columna mas alta
	sumas_de_columnas.append(suma_de_columna) # la anadimos a una lista donde estan las sumas de cada columna
	
'''
print(sumas_de_columnas) # lista de las sumas de cada columnas de la M
print(indice_c_mayor) # el indice donde se encuentra la columna mas alta
'''

print(f"La matriz tiene {tamaño_filas} filas y {tamaño_columnas} columnas")
print(f"La fila mas alta esta en la posicion M[{indice_fila_mayor}] y es {suma_f_mayor}")
print(f"La columna mas alta esta en la posicion M[x][{indice_c_mayor}] y es {suma_c_mayor}]")
	
		
