# pedir al usuario una contrasena
# debe tener 1. una vocal en minuscula
# 2. tener dos simbolos * o #
# indicar si es segura o no

user = input("Introduce tu nombre de usuario: ")
pswd = input("Introduce tu contraseña: ")

if ("a" in pswd or "e" in pswd or "i" in pswd or "o" in pswd or "u" in pswd) and ("*" in pswd or "#" in pswd):
	print("Tu contraseña es segura.")
	print("Bienvenido", user.title())
else:
	print("Tu contraseña no es segura. Recuerda que debe tener al menos una vocal minuscula, y un caracter especia (* o #)")


