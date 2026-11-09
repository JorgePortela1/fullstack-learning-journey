# ordenador con 3 usuarios (Alejandro, Naomi y Sergio) mas el usuario invitado

user1 = "alejandro"
user2 = "naomi"
user3 = "sergio"
user4 = ""

userX = input("Cual es tu nombre?")
userX = userX.lower()
if userX == user1:
	print(f"Bienvenido {user1}. ")
elif userX == user2:
	print(f"Bienvenida {user2}. ")
elif userX == user3:
	print(f"Bienvenido {user2}")
else:
	print(f"Bienvenido/a, {userX}. Disfruta de tu nueva sesion. ")
