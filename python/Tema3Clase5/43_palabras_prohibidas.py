"""Ejercicio 1: Palabras prohibidas.

Dada una lista de palabras y otra lista con letras prohibidas, crea una nueva
lista que contenga únicamente las palabras que no incluyan ninguna letra
prohibida. No importa si las letras están en mayúsculas o minúsculas.
"""

palabras = ["credo", "manzana", "araña", "piedra", "lechuga"]
letras_prohibidas = ["e","i"]
lista_filtrada = []

# - Bucle para recorrer la lista de palabras:
for palabra in palabras:
	# Crear condicion para comprobar
	incluir = True
	# - Bucle para recorrer la lista de las letras prohibidas
	for letra in letras_prohibidas:
		# y comprobar si se cambia la condicion
		if letra in palabra:
			incluir = False
	# si no cambia la condicion, se toma accion
	if incluir == True:
		lista_filtrada.append(palabra)

print(palabras)
print("----")
print(lista_filtrada)
