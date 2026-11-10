
print("Pillando Soltura, Tema 3, clase 3")


print("----Ejercicio 1----")
#-escribe un programa que encuentre elementos duplicados en una lista
#-los añada en una nueva lista y los borre de la anterior
#-despues imprime la lista con solo los elementos unicos

import random

random_numbers = []
duplicate_numbers = []
unique_numbers = []

list_size = int(input("Cuantos elementos quieres que tenga la lista? "))

for i in range(1,list_size+1,1):
	#random.randint(a,b) --> devuelve entero entre a y b. se pueden repetir
	random_number = random.randint(1,list_size)
	random_numbers.append(random_number)
	#print(i,random_number)

print("List of random numbers: ",random_numbers)

for i in random_numbers:
	repetidos = random_numbers.count(i)
	if repetidos > 1:
		if i not in duplicate_numbers:
			duplicate_numbers.append(i)	

print("List of duplicate numbers: ", duplicate_numbers)

for i in random_numbers:
	if i not in unique_numbers:
		unique_numbers.append(i)

print("list of unique numbers: ", unique_numbers)



	
	#print(i, "--> ",repetidos)
		
