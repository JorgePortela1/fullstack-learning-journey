# El usuario introduce 3 longitudes
# La suma de 2 longitudes debe ser mayor que la restante

long1 = float(input("Introduce una primera longitud: "))
long2 = float(input("Introduce una segunda longitud: "))
long3 = float(input("Introduce una tercera longitud: "))

if (long1 + long2 > long3) or (long2 + long3 > long1) or (long1 + long3 > long2):
	print("Las longitudes son adecuadas para realizar el triangulo")	
else:
	print("Las longitudes no son adecuadas.")
