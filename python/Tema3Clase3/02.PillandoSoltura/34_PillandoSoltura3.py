

print("Pillando Soltura - Ejercicio 3")
'''
Escribe un script que encuentre el segundo numero mas grande de una lista. 
'''
#importamos la biblioteca de random
import random

#creamos la variable donde almacenaremos el tamano de la lista
size_list = int(input("What are gonna be the size of the list?: "))

#inicializamos las listas
random_list = []
unique_list = []

#hacemos uso de la biblioteca y generamos un numero aleatorio
for i in range(size_list):
    random_number = random.randint(1,size_list)
    #para anadirlo a la lista
    random_list.append(random_number)

#aqui podemos ver todos los numeros aleatorios que se han generado
print(random_list)
#los ordenamos de menor a mayor
random_list.sort() 
print(random_list)

#creamos otra lista en la que no se repiten los numeros
for i in random_list:
    if i not in unique_list:
        unique_list.append(i)

#aqui vemos la lista sin repetidos
print(unique_list)
#y aqui la solucion que nos pide el ejercicio: obtener el segundo numero mas alto
print(unique_list[-2])
