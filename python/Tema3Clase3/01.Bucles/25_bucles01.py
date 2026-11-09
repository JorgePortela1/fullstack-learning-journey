##EJERCICIO 1 DE LA CLASE 3##


# --- PEDIR AL USUARIO UN NUMERO ENTERO
num = int(input("De que tamano quieres que sea tu arco?: "))

# --- BUCLE ASCENDENTE
for i in range(num):
	print((1+i) * "*")

# --- BUCLE DESCENDENTE	
for i in range(num-1, 0, -1):
	print(i * "*")

