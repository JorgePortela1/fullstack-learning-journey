"""Ejercicio: Encriptación de datos."""


# Encriptacion ROT13 es darle valor a la letra 13 posiciones 
## despues en el abecedario

orden_normal = "abcdefghijklmnopqrstuvwxyz"
orden_rot = "nopqrstuvwxyzabcdefghijklm"

long = len(orden_normal)

palabra = input("Introduce tu palabra para transfomar: ")
palabra = palabra.lower()

segunda_palabra = input("Introduce la supuesta codificacion: ")

translate = ""

# Nivel 1: recorre la frase carácter por carácter.
for caracter in palabra:
	# Nivel 2: comprueba si el carácter actual está en el abecedario.
	if caracter in orden_normal:
		# Nivel 3: recorre las posiciones de 0 a 25 para localizar la letra.
		for i in range(long):	
			# Nivel 4: comprueba si la letra de esta posición es el carácter actual.
			if orden_normal[i] == caracter:
				# Nivel 5: obtiene la letra ROT13 que ocupa la misma posición.
				letra_cifrada = orden_rot[i]
				# Nivel 5: añade la letra cifrada al resultado que se está formando.
				translate = translate + letra_cifrada
	# Nivel 2: se ejecuta si no es una letra: espacio, coma, signo, etc.
	else: 
		# Nivel 3: conserva ese carácter sin modificarlo en el resultado.
		translate = translate + caracter

if translate == segunda_palabra:
	print("tu segunda palabra esta codificada")
else:
	print("La segunda palabra no esta codificada")

print(f"La frase {palabra} en lenguaje rot13 se lee de la siguiente manera: {translate}")

			
