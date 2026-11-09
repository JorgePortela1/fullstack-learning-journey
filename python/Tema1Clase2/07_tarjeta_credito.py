'''
TARJETA DE CREDITO:
Crea un script que reciba como input un numero de tarjeta de credito e imprima por pantalla todos
los caracteres en forma de asterisco salvo los ultimos cuatro. Si por ejemplo el numero de tarjeta
es 1234 2345 3456 5678, el output debera ser **** **** **** 5678.
'''

numTarjeta = input("Introduzca su numero de tarjeta (xxxx xxxx xxxx xxxx)")

print(f"**** **** **** {numTarjeta[-4:]}")
