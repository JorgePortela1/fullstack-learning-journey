# soy propietario de una tienda en linea
# tengo una lista de ventas de los ultimos 30 dias
# analiza las ventas por dia de la semana para saber que dias se venden mas

dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
ventas_totales = [0, 0, 0, 0, 0, 0, 0]
import random

ventas = []
for i in range(30):
	venta = random.randint(10,1000)
	ventas.append(venta)

dia_venta = 0
for venta in ventas:
	ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
	dia_venta = dia_venta + 1
	if dia_venta == 7:
		dia_venta = 0

resumen = zip(dias_semana, ventas_totales)

for dias, ventas in resumen:
	print(f"Las ventas hechas los {dias}, alcanzan un total de: {ventas}")



