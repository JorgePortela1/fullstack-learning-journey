"""Ejercicio 2: Números primos.

Dada una lista de números enteros, obtén los números primos. Después muestra
la lista de primos, cuántos hay y cuál es su suma total.

Dada una lista de números enteros, escribe un script en Python que devuelva una nueva lista con los números primos de la lista original.

Además, el script debe devolver el número total de números primos encontrados y la suma de los números primos encontrados.

"""

lista_enteros = [2,3,4,5,6,7,8,9,10]
lista_primos = []

# cuantos primos hay y cual es la suma de estos

# Recorro la lista 
for entero in lista_enteros:
	primo = True
	for i in range(2, entero):
		# si el numero encuentra divisores, no es primo
		if entero % i == 0:
			primo = False
	if primo == True:
		lista_primos.append(entero)

print(lista_primos)

num_primos = len(lista_primos)

print(f"La cantidad de primos en la lista es de {num_primos}.")
print(f"La suma de todos tus primos es {sum(lista_primos)}")
