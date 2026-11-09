# pide una contrasena
# el programa sabe cual es la contrasena correcta
# si es correcta, el script da bienvenida al usuario
# si no, debe indicar que es incorrecta y que vuelva a introducirla
# al segundo fallo, mostrar error y terminar el script

pswd = "abcd"

pswdUSER = input("Introduce la contrasena: ")

if pswd == pswdUSER:
	print ("Bienvenido usuario!")
else:
	print ("ERROR")
	print ("Tienes un intento mas: ")
	pswdUSER = input("Introduce la contrasena: ")
	if pswd != pswdUSER:
		print ("ERROR")
		print ("Se te ha bloqueado el acceso!")
	else:
		print ("Bienvenido usuario!!")
