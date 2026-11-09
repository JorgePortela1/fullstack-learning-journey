# pedir 4 numeros 
# devolverlos en orden ascendente
# usa listas y bucles fo


# ---- hay que inicializar una lista
numeros = []

# ---- crear el bucle que pide numero (la lista debe contener 
## enteros y no strings) y los introduce en la lista
for i in range(4):
	numeros.append(int(input("Introduce un numero: ")))
	
# ---- imprimir el mayor de la lista por pantalla
print("El numero mas alto de la secuencia es: ", max(numeros))

# ---- imprimir la lista en orden ascendente
print("La lista ordenadar de menor a mayor es: ", sorted(numeros))

print(numeros)


