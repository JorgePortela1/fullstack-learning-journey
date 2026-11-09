#pide al usuario dos numeros
#muestra por pantalla su division
# si el divisor es 0, el programa debe mostrar error

dividendo = int(input("Escribe un numero: "))
divisor = int(input("Escribe un segundo numero: "))

if divisor == 0:
	print ("¡¡ERROR!!")
	print ("Tu segundo numero no puede ser 0")
	divisor = int(input("Entonces, que numero decides ahora?: "))


resultado = dividendo / divisor
print (resultado)

