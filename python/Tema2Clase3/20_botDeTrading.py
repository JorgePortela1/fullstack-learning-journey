# trading bot: segun el precio de un producto financiero:
# si es inferior a 100, el bot ordenara comprar
# si esta entre 100 y 150 el bot ordenara holdear
# y si el precio es superior a 150, el bot ordenara vender.

precio = float(input("Cual es el precio del Oro? "))

if precio < 100:
	print("Debes comprar este producto ASAP.")
elif precio >= 100 and precio <=150:
	print("Debes holdear hasta un nuevo cambio en el precio.")
else:
	print("Debes vender!")
