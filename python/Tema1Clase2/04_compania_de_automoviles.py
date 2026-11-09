'''
Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.
'''

# tres tipos de coches

coche1 = ("RBM Serie 1")
coche2 = ("RMB Serie Plus")
coche3 = ("RMB Todoterreno")

# Precio de cada tipo de coche y la comision por cada coche vendido

coche1_precio = 20000
coche1_comision = 0.03 * coche1_precio

coche2_precio = 35000
coche2_comision = 0.05 * coche2_precio

coche3_precio = 60000
coche3_comision = 0.07 * coche3_precio

# Se pide al usuario introducir los datos

coche1_vendidos = int(input(f"Cuantos {coche1} se han vendido:"))
coche2_vendidos = int(input(f"Cuantos {coche2} se han vendido:"))
coche3_vendidos = int(input(f"Cuantos {coche3} se han vendido:"))

print("")
print("---------------------------------------------------------------")
print("")

# calculo del total ventas de cada uno de los coches y sus comisiones correspondientes

coche1_generados = coche1_vendidos * coche1_precio
coche1_comision_ganada = coche1_comision * coche1_vendidos

coche2_generados = coche2_vendidos * coche2_precio
coche2_comision_ganada = coche2_comision * coche2_vendidos

coche3_generados = coche3_vendidos * coche3_precio
coche3_comision_ganada = coche3_comision * coche3_vendidos

# resumen de las ventas en detalle

print(f"Al vender {coche1_vendidos} {coche1}, has generado al concesionario {coche1_generados} Euros. Por lo tanto, te llevas de comision {coche1_comision_ganada} Euros")
print(f"Al vender {coche2_vendidos} {coche2}, has generado al concesionario {coche2_generados} Euros. Por lo tanto, te llevas de comision {coche2_comision_ganada} Euros")
print(f"Al vender {coche3_vendidos} {coche3}, has generado al concesionario {coche3_generados} Euros. Por lo tanto, te llevas de comision {coche3_comision_ganada} Euros")

print("")
print("---------------------------------------------------------------")
print("")

total_ventas =  coche1_generados + coche2_generados + coche3_generados
total_com_ganadas = coche1_comision_ganada + coche2_comision_ganada + coche3_comision_ganada

# resumen de las ventas en general

print(f"Generando un total de {total_ventas} Euros, has conseguido un total de {total_com_ganadas} Euros. Enhorabuena!")
