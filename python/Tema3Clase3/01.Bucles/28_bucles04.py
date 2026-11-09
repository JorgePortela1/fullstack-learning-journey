#EJERCICIO 4 DE LA CLASE 3

# ---- PROGRAMA QUE PREGUNTE UNA FRASE, UNA LETRA Y CUENTE EL NUMERO DE VECES QUE LA LETRA APARECE EN LA FRASE ----

# PEDIR AL USUARIO LA FRASE Y LA LETRA Y ALAMACENARLA
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

# VARIABLE QUE VAYA CONTANDO LAS VECES QUE LA LETRA APARECE
veces = 0

# FORMA DE EMBELLECER EL CODIGO
print("Calculando...")

# ALMACENAR EL TAMAÑO DE LA FRASE
fraseLong = len(frase)

# USAR EL TAMAÑO DE LA FRASE PARA RECORRERLA
for i in range(fraseLong):
	### si la letra coincide con la letra que esta en la posicion donde esta la i, se añade 1 al contador
	if letra == frase[i]:
		veces = veces + 1

# IMPRIMIR EL RESULTADO
print("El numero de veces que se repite: ", letra, " en la palabra/frase : ",frase,  "es de: ", veces)
