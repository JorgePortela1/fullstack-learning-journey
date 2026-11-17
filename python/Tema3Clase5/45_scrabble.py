"""Ejercicio 3: Puntuación de Scrabble.

Tienes una lista de fichas de Scrabble. Cada ficha está formada por una letra
seguida de uno o más dígitos que representan su puntuación. Calcula la
puntuación total de la mano.

Supongamos una lista de caracteres llamada "palabras" que representa una mano de Scrabble.

Cada string contiene dos caracteres:

El primer carácter es la letra de una ficha
El segundo el número que representa los puntos de la ficha

Por ejemplo, el string "A5" representa la ficha con la letra A y un valor de 5 puntos.

Crea un script que calcule el valor total de los puntos en una mano de Scrabble.
El valor total será la suma de los puntos de todas las fichas de la mano.

"""
puntos = []
mano_scrabble = ["A1","B2","C3","D4","E5"]
for mano in mano_scrabble:	
	puntos.append(int(mano[1:]))

print(f"Tu mano de Scrabble tiene un valor de {sum(puntos)}")
