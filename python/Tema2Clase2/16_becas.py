# requisitos becas:
# nota minimo 8
# edad entre 17 y 21
# pide nombre, edad, y nota media
# devuelve si recibe la beca o no


userName = input("Cual es tu nombre? ")
ageUser = int(input("Cual es tu edad?: "))
notaUser = int(input("Cual es tu nota media?: "))

if ageUser >= 17 and ageUser <= 21:
	if notaUser >= 8:
		print (userName, ", Cumples los requisitos para la beca!")
		print ("ENHORABUENA!")
	else:
		print (userName, "Tu nota media no alcanza el target requerido.")
		print ("Desafortunadamente, no se te puede dar beca")
else:
	print (userName, "Tu edad no entra dentro de los requisitos")
	print ("Desafortunadamente, no se te puede dar beca")
