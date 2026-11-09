''' En un restaurante el menu consta de las siguientes opciones:
Ensalada mixta -- 12 EU
Sopa de pescado -- 10 EU
Dorada al horno -- 18 EU
Arroz al curry -- 14 EU
Lasana de carne -- 15 EU
Brownie de chocolate -- 8 EU
Helado -- 6 EU
Refrescos -- 5,5 EU
Cafe -- 3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta.
'''
print("----------------------------------------------------------------")
plato_ensalada = int(input("Cuanta ensalada mixta se ha ordenado?: "))
plato_sopa = int(input("Cuanta sopa de pescado se ha ordenado?: "))
plato_dorada = int(input("Cuanta dorada al horno se ha ordenado?: "))
plato_arroz = int(input("Cuanto arroz al curry se ha ordenado?: "))
plato_lasana = int(input("Cuanta lasana de carne se ha ordenado?: "))
plato_brownie = int(input("Cuanto brownie de chocolate se ha ordenado?: "))
plato_helado = int(input("Cuanto helado se ha ordenado?: "))
plato_refrescos = int(input("Cuanto refresco se ha ordenado?: "))
plato_cafe = int(input("Cuanto cafe se ha ordenado?: "))
print("----------------------------------------------------------------")

precio_ensalada = 12
precio_sopa = 10
precio_dorada = 18
precio_arroz = 14
precio_lasana = 15
precio_brownie = 8
precio_helado = 6
precio_refrescos = 5.5
precio_cafe = 3.5

total_ensalada = precio_ensalada * plato_ensalada
total_sopa = precio_sopa * plato_sopa
total_dorada = precio_dorada * plato_dorada
total_arroz = precio_arroz * plato_arroz
total_lasana = precio_lasana * plato_lasana
total_brownie = precio_brownie * plato_brownie
total_helado = precio_helado * plato_helado
total_refrescos = precio_refrescos * plato_refrescos
total_cafe = precio_cafe * plato_cafe

total_cuenta = total_ensalada + total_sopa + total_dorada + total_arroz + total_lasana + total_brownie + total_helado + total_refrescos + total_cafe


print("")
print(f"La cuenta total de tu mesa es de {total_cuenta:.2f} $")
print("")
print("----------------------------------------------------------------")


