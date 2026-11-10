print("Pillando Soltura - Ejercicio 7")

# Crea un script que extraiga los elementos comunes entre dos listas. 

# Crear dos distintas listas de numeros aleatorios
## importamos random
import random

##inicializar las listas
random_list1 = []
random_list2 = []
total_list = []

#Pedir al usuario el tamano de la lista de aleatorios
list_size = int(input("Introduce el tamano de las listas: "))

#Ahora, a rellenar las listas con numeros aleatorios
for i in range(1,list_size):
    random_number = random.randint(1,list_size)
    random_list1.append(random_number)
    random_number = random.randint(1,list_size)
    random_list2.append(random_number)
    #Comprobamos

print(random_list1)
print(random_list2)

#Recorremos cada numero de una lista para compararlo con 
## cada uno de los elementos de la segunda lista
for i in random_list1:
    for j in random_list2:
        #si coinciden, se anade a la lista de comunes
        if i == j:
            #y solo anadirlo cuando no este, para que no se repitan
            if i not in total_list:
                total_list.append(i)

#ordenamos e imprimimos la solucion del ejercicio
total_list.sort()
print(total_list)
