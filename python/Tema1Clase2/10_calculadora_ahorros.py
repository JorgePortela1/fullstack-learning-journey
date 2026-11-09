'''
CALCULADORA DE AHORROS:
El objetivo es crear un programa con el que puedas calcular tus ahorros anuales.
El programa debera calcular cuanto puede ahorrar una persona dado sus ingresos por hora, sus horas trabajadas y su gasto de vida semanal.

Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus
gastos a 3/4 de lo que gastaba antes, tendra suficiente dinero para sus gastos?
(Pista: tan solo necesitas cambiar los valores de las variables de horas trabajadas por semana y
gastos semanales)
'''

# 1. Primero haremos que el programa nos pida nuestro nombre y despues imprima un saludo por pantalla de tipo: "Hola <Nombre>"

print("----Sistema de ahorro----")
user_name = input("Antes de empezar, Como te llamas?: ")
print(f"Bienvenido a tu calculadora personal de ahorros, es un placer {user_name.title()}. ")
print("")

# 2. Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables diferentes

time_worked = float(input("Cuantas horas a la semana ha trabajado?: "))
pay_worked = float(input("Y cuanto le pagan por hora?: "))

# 3. Multiplica ambas variables para obtener el salario semanal

week_worked = time_worked * pay_worked

# 4. Ahora calcula las ganancias anuales. Guarda el valor en una variable.

year_worked = week_worked * 53

# 5. Ahora imprime por pantalla un mensaje del tipo: "<Nombre> tiene unas ganancias anuales de: <cantidad> euros"

print(f"Querido/a {user_name.title()}, usted genera por ano un total de {year_worked}$. ")
print("")

# 6. Pide los gastos semanales por pantalla y guardalos en una variable.

exp_week = float(input(f"{user_name.title()}, generalmente, cuanto se gasta por semana?:  "))

# 7. Calcula el gasto anual

exp_year = exp_week * 53

# 8. Recuerda anadir comentarios sobre lo que esta haciendo cada parte del codigo
# 9. Los ahorros anuales seran la resta entre lo ganado durante el ano menos los gastos anuales.

ahorros = year_worked - exp_year
# 10. Imprime los resultados por pantalla

print("-----------------")
print(f"El ahorro que consigue obtener es de {ahorros}$. ")
