# 1 clase dividida en 2 grupos. 
# grupo A: chicas cuyo nombre empieze por E hasta la M. 
# grupo A: chicos: A --- H y R --Z
# grupo B los restantes.


# Creo una variable donde situo el abecedario
check = (" abcdefghijklmnñopqrstuvwxyz")

# pido al usuario su genero y su nombre
gender = input("Indica tu genero(h ó m): ")
name = input("Introduce tu nombre: ")

# creo la variable donde se almacena la inicial del nombre
inicial = name[0]

# creo la variable donde se almacena la posicion de la inicial en el abecedario
id = check.find(inicial)

if gender == ("m"):
	if id >= 5 and id <= 13:
		print("Perteneces al grupo A.")
	else:
		print("Perteneces al grupo B.") 

if gender == ("h"):
	if ((id >= 1) and (id <=8)) or ((id >= 19) and (id <=27)):
		print("Perteneces al grupo A.")
	else:
		print("Perteneces al grupo B.") 


#print(inicial)
#print(check[id]) 
#print(id)
