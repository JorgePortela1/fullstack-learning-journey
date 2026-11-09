#crea un script que dado un numero y una potencia compruebe si ese
#numero elevado a la potencia es par o impar
#pista: los numeros pares tienen resto = 0 al dividirlos por 2

numero = float(input("Introduce un numero: "))
potencia = float(input("Ahora, introduce una potencia: "))

num_pote = numero ** potencia

if num_pote % 2 == 0:
	print ("Tu numero es par")
elif num_pote % 2 != 0:
	print ("Tu numero es impar")

print ("EXPLICACION")
print ("tu numero, ", numero, "al elevarlo al", potencia, "es: ", num_pote)



