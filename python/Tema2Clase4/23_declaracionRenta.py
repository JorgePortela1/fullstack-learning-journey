# saber si al usuario se le aplica el impuesto

# si se le aplica el impuesto, que impuesto se le aplica


user = input("Cual es tu nombre?: ")
age = int(input("Cuantos años tienes?: "))
salary = int(input("Cuanto es tu sueldo mensual?: "))
anualRent = salary * 12
print("Bienvenido ", user)

if age >= 18:
	print("Cumples la edad para que se te aplique el impuesto")
	if anualRent >= 1000 and anualRent < 15000:
		print("Tu tipo impositivo es del 5%")
	elif anualRent >= 15000 and anualRent < 25000:
		print("tu tipo impositivo es del 15%")	
	elif anualRent >= 25000 and anualRent < 35000:
		print("tu tipo impositivo es del 20%")
	elif anualRent >= 35000 and anualRent < 60000:
		print("tu tipo impositivo es del 30%")
	elif anualRent >= 60000:
		print("Tu tipo impositivo es del 45%")
else:
 	print("No te corresponde pagar ningun impuesto.")
