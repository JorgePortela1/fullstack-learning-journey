'''

LISTAS NUMERICAS:
1. Crea una lista llamada numeros que contenga los siguientes numeros enteros:
[1,2,3,4,5,6,7,8,9,10].
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
3. Escribe un bucle que recorra la lista numeros e imprima el cuadrado de cada numero por
consola.
4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
compresión).
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
6. Haz lo mismo con el número más alto
7. Suma todos los elementos de la lista con y sin un bucle.
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
el punto 2.

'''
#CREA UNA LISTA DE NUMEROS ENTEROS DEL 1 AL 10
## hay dos formas:
### (1)
numeros = []
for i in range(1,11):
	numeros.append(i)
print(numeros) 
### (2)
numeros = list(range(1,11))
print(numeros)


#Crea otra lista con los pares de la lista anterior pero en orden inverso
numeros_inverso = []
for i in range(10,0,-2):
	numeros_inverso.append(i)

print(numeros_inverso)

#Bucle que recorra la primera lista e imprima los cuadrados de cada numero
longitud_lista1 = len(numeros)
for i in range(1, longitud_lista1):
	print("El cuadrado del numero: ",i, "es: ",i*i)
	
#Hacer los pasos 2 y 3 en el menor de lineas posibles. 
print("----------")

#Devuelve el numero mas pequeno
numeros.sort()
print("El numero mas pequeno de la primera lista es: ",numeros[0])

numeros_inverso.sort()
print("El numero mas pequeño de la segunda lista es: ",numeros_inverso[0])

#Devuelve ahora el mas grande
print("-----------")
print("El numero mas grande de la primera lista es: ", numeros[-1])
print("El numero mas grande de la segunda lista es: ", numeros_inverso[-1])

#Suma los elementos de las listas, uno sin bucle, otro con bucle.

total = 0
for i in range(0, longitud_lista1):
	total = total + numeros[i] 
print("La suma total de todos los numeros de la primera lista es: ", total)

print("La suma de todos los numeros de la segunda lista es:",sum(numeros_inverso))

#Encuentra la posicion del numero 8 en ambas listas.

posicion1 = numeros.index(8)
posicion2 = numeros_inverso.index(8)

print(f"La posicion del numero 8 es {posicion1}")
print(f"La posicion del numero 8 es {posicion2}")
