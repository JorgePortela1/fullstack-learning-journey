# EJERCICIO 5 DE LA CLASE 3

## --- PROGRAMA QUE IMPRIME LOS NUMEROS PRIMOS DEL 2 AL 100 ---
#   (numero primo: positivo que solo tiene el 1 y si mismo como divisor)   #

# CREAMOS UN BUCLE QUE RECORRA LOS NUMEROS DEL 2 AL 100

for i in range (2, 101, 1):
	#([inicio],[fin],[salto])
	
	# Consideramos que variable esPrimo es True
	esPrimo = True
	# hasta que el programa averigue que no es true y lo pase a False

	# CON OTRO BUCLE, RECORREMOS DESDE EL NUMERO 2 HASTA EL NUMERO DE LA POSICION DEL PRIMER BUCLE
	for j in range(2,i):
		# SI EL NUMERO DEL PRIMER BUCLE, AL DIVIDIRLO POR EL NUM DEL SEGUNDO BUCLE, ES = A 0:
		# aqui averiguamos si el numero i es divisible por otro numero que no sea el 1 y si mismo, al serlo, lo cambiamos a False
		if i % j == 0:
			esPrimo = False
			# al saber que es false por encontrar un numero que lo divida, no necesitamos encontrar otro
			break 

	# si no es asi, la variable esPrimo sigue siendo True, e imprimmos su valor, que esta en i
	if esPrimo:
		print(i)
