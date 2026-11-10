print("Pillando Soltura - Ejercicio 8")

import random

veces = int(input("Cuantos numeros quieres en tu lista: "))

lista_numerica = []


for i in range(0,veces,1):
	numeroRandom = random.randint(0,100)
	lista_numerica.append(numeroRandom)

print(lista_numerica)

enBusca = int(input("Que numero estas buscando en la lista"))

apariciones = 0

for numero in lista_numerica:
	if enBusca == numero:
		apariciones = apariciones + 1
		
print(f"tu numero aparece en la lista {apariciones} veces")
