## EJERCICIO 2 DE LA CLASE 3##

# --- Programa que almacene una contraseña en una variable, preguntarle al usuario hasta que introduzca la correcta ---

# GUARDAR LA CONTRASENA 
pswd = ("lujoso")

# VARIABLE PARA VERIFICAR QUE LO INTRODUCIDO ES LA CONTRASENA:
opcion = input("Introduces tu contrasena: ")

	# SI OPCION ES DIFERENTE A PSWD, LA CONTRASEÑA ES INCORRECTA Y VUELVE A PREGUNTAR
while opcion != pswd:
	print("Contraseña incorrecta, vuelva a intentarlo! ")
	opcion = input("Introduce la contraseña: ")		
	# HASTA QUE OPCION SEA IGUAL QUE PSWD, Y DAR LA BIENVENIDA AL USUARIO
else:
	print("Contrasena correcta. Bienvenido!")

