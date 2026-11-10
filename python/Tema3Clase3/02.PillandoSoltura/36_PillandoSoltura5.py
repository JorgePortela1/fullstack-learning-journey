print("Pillando Soltura - Ejercicio 5")

#Script donde tras un numero dado por el usuario, sume los divisi-
## bles por este

#Pedir al usuario un numero
user_num = int(input("Introduce un numero: "))

#Inicializar listas
random_numbers = []
divisibles_numbers = []

#Crear una lista con numeros randoms
## importar random
import random
## Bucle que cree un numero random y lo anada a la lista
for i in range(1,19,1):
	random_number = random.randint(1,20)
	random_numbers.append(random_number)

##Comprobar
print(random_numbers)

#Crear lista donde se almacenen los numeros divisibles
## empezamos recorriendo la lista:
for i in random_numbers:
	#si i es divisible por el user_num
	if i % user_num == 0:
		divisibles_numbers.append(i)
		## comprobamos

print(divisibles_numbers)
#Sumar todos los elementos de la lista
total = sum(divisibles_numbers)

#finalizar el ejercicio
print("La suma de los numero divisibles por el numero introducido es de: ", total)
