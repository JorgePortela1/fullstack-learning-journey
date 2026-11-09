''' 
FOREX EXCHANGE
create a script where after a a cuantity input from user, give the simil in dollars
be aware of comision of 10%
at the end, print: money to transfer, money in comission, dollars that user will received
this last info in a receipt format

Casa de Cambio
Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario, de el resultante en dolares.
1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dolares (considera una tasa de cambio donde 1 EU = 1.2 $)
2. La casa de cambios se queda un 10% en concepto de tasas de gestion. Calcula el monto
recibido, el cambio en dolares, la cantidad que se queda la casa de cambios y la cantidad de
dolares restante que recibira el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario. 
'''

# Create the variable where the input of Euros the user want to transfer

euros = float(input("How many Euros do you want to transfer into a dollars: "))

exchange_rate = 1.2
comission_rate = 0.1

# I write the code, in terms of print in a receipt format

print("------ Calculating Invoice... -----")

print("Euros entered: -----> ", euros)
print("Exchange rate applied: -----> ", exchange_rate)

dollar_before_fee = euros * exchange_rate
print("Dollars before comission: -----> ", dollar_before_fee)

comission_fee = dollar_before_fee * comission_rate
print(f"Processing fee: -----> {comission_fee:.2f}")

total_received = dollar_before_fee - comission_fee
print("Total amount received: -----> ", total_received)

print("------------------------------------")
print("Thank you for using our services.")
