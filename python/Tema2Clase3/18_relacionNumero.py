# el usuario debe introducir 3 numeros distintos 
# el programa debe mirar si alguno de esos numeros es la suma de los otros 2

num1 = int(input("Escribe un primer numero: "))
num2 = int(input("Escribe un segundo numero: "))
num3 = int(input("Escribe un tercer numero: "))

print("--------Calculando-------")

if num1 == num2 + num3:
	print("La suma de los dos ultimos numeros es el primer numero.")
elif num2 == num1 + num3:
	print("La suma del primer y tercer numero es el segundo.")
elif num3 == num1 + num2:
	print("La suma de los dos primeros numeros es el tercero")
else:
	print("Ningun numero es la suma de los otros dos.")
	
