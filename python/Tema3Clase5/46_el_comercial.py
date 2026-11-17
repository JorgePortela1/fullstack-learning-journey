


productos = [1,2,3,4,5,6,7,8,9,10]
precios = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_vendidas = [3,1,0,0,7,2,0,0,4,0]

total_unidades_vendidas = 0
total_facturado = 0

datos = zip(productos, precios, unidades_vendidas)
for producto, precio, unidades in datos:
	print(f"El producto nº {producto}, tiene un precio de: {precio}, y se han vendido {unidades}")
	facturacion = precio * unidades
	print(f"El producto {producto} ha generado un total de {facturacion}")
	
	total_unidades_vendidas = total_unidades_vendidas + unidades
	total_facturado = total_facturado + facturacion

print(f"Se han vendido un total de {total_unidades_vendidas} productos")
print(f"Generando un total de {total_facturado} euros.")
