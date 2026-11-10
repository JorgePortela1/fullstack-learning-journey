print("Pillando Soltura - Ejercicio 6")

#Scrip que dado un numero dado por el usuario
## se encuentre el numero mas alto antes del numero introducido

#inicializar listas
random_numbers = []
small_numbers = []

#Crear la lista de numeros aleatorios 
list_size = int(input("Tamaño de la lista de aleatorios: "))
## importar randoms
import random
for i in range(1,list_size):
	number_random = random.randint(1,list_size)
	random_numbers.append(number_random)
	#comprobar
print(random_numbers)

#Pedir al usuario el numero
user_num = int(input("Introduce un numero: "))

#Crear lista con los numeros mas pequenos que el del usuarioi
for i in random_numbers:
	if user_num > i:
		small_numbers.append(i)
		#comprobar
print(small_numbers)

#Ordernar la lista y luego imprimir la solucion
small_numbers.sort()
print(small_numbers)
print(small_numbers[-1])

