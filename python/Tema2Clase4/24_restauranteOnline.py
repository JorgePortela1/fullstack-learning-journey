# hamburgueseria online
# 2 tipos de hamburgesa

print("Bienvenid@ a la hamburgueseria del momento!")
burger = input("Elige entre la clasica o la vegana: ")
if burger == ("clasica"):
	print("La clasica hamburguesa que nunca pasa de moda!")
	extras = input("¿Que ingredientes extras quieres?(Queso, Bacon y/o huevo)")
	print("Los ingredientes adicionales elegidos han sido: ", extras)

elif burger == ("vegana"):
	print("La opcion vegetal, nada mal!")
	extras = input("¿Que ingredientes extras quieres?(Tofu y/o cebolla)")
	print("Los ingredientes adicionales elegidos han sido: ", extras)
else:
	print("La hamburguesa seleccionada no esta disponible!")
