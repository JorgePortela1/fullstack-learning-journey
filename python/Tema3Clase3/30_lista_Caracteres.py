# SERIE DE EJERCICIOS 6 DE LA CLASE 3

#Creamos la lista de frutas
list_Fruits = ["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]

#Averiguamos la longitud de la lista de frutas
longLista = len(list_Fruits)

#Accedemos al objeto numero 3 de la lista. 
for i in range(0,longLista):
    if i == 3:
        print(list_Fruits[i])

#Modificar el objeto 2 de la lista a "mora"
list_Fruits[2] = "mora"
print(list_Fruits)

#Anade "Mango" a la lista
list_Fruits.append("mango")
print(list_Fruits)



#Insertar uva al principio de la lista
list_Fruits.insert(0, "uva")
list_Fruits.insert(3, "cereza")
print(list_Fruits)

#Recorre la lista e imprime cada fruta
longLista = len(list_Fruits)
for i in range(0,longLista):
    print(list_Fruits[i])


#Usar pop() para eliminar el ultimo elemento y guardarlo en otra variable(ultima_fruta)
ultima_fruta = list_Fruits.pop(-1)
print(ultima_fruta)

#Recorre la lista con un bucle e imprime todas las frutas.
longLista = len(list_Fruits)
for i in range(0, longLista):
    print(list_Fruits[i])

#Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
longLista = len(list_Fruits)
for i in range(0, longLista):
    long_palabra = len(list_Fruits[i])
    print("La palabra: ", list_Fruits[i], "tiene el siguiente numero de letras: ", long_palabra)


#11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que tengan más de 5 caracteres
longLista = len(list_Fruits)
for i in range(0, longLista):
    long_palabra = len(list_Fruits[i])
    if long_palabra >= 5:
        print("Palabra con mas o igual a 5 letras: ", list_Fruits[i])

#Usa remove() para borrar cereza de la lista
longLista = len(list_Fruits)
j = ""
for i in range(0, longLista-1):
    if list_Fruits[i] == "cereza":
        list_Fruits[i] = j
        list_Fruits.remove(j)

print(list_Fruits)

#13. Usa el método clear() para vaciar la lista.
list_Fruits.clear()
print(list_Fruits)
