print("Pillando Soltura - Ejercicio 4")

# script que cuente el numero de elementos mas grande que un numero
#  dado por el usuario

# inicializar listas
random_numbers = []
bigger_numbers = []

# importar random
import random

# pedir al usuario el tamano de la lista
size_list = int(input("De que tamaño quieres la lista?: "))
# pedir al usuario cualquier numero
user_num = int(input("Introduce un numero cualquiera: "))

# Crear la lista de numeros aleatorios
	# con un bucle, vamos creando numeros aleatorios con .randint
	#  y lo añadimos a la lista con .append
for i in range(1,size_list+1,1):
	random_number = random.randint(1,size_list)
	random_numbers.append(random_number)

# recorrer la lista y separando en otra nueva los elementos 
#  mas grande que el numero proporcionado por el usuario
for i in random_numbers:
	if i > user_num:
		bigger_numbers.append(i)

# Comprobamos imprimiendo las listas

print(random_numbers)
print(bigger_numbers)

# Dar con la solucion: contar numeros mas grande
print("Hay ", len(bigger_numbers), "numeros mas grande que tu numero.")
