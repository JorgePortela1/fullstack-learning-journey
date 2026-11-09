'''
a. Crea un script en el que el usuario introduzca un numero de mas de una cifra. El script debe
imprimir los componentes del numero uno a uno por pantalla. Por ejemplo si el numero introducido
es el 4532 por pantalla debera imprimirse:
4
5
3
2
b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el numero que
resulta de leer el numero introducido 
'''

variable1 = input("Escribe los 4 numeros: ")
long_variable1 = len(variable1)

print("")
print("-------------------")
print("")

print(variable1[0])
print(variable1[1])
print(variable1[2])
print(variable1[3])

print("")
print("Ahora del Reves")
print(variable1[3] + variable1[2] + variable1[1] + variable1[0])

print("")
print("-------------------")
print("")
