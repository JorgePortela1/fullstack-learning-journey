'''
-Crea script que muestre por pantalla el resultado de una operacion aritmetica
-luego, crea otro programa que tras un numero dado por usuario resuelva una funcion
-escribe un programa que tras dos numeros dados por el usuario imprima los numeros,
el cociente y el resto

'''
print("--------------")
print("Parte primera: ")
resuelto = ((3+2)/(2*5))**2
print(resuelto)
print("--------------")
print("Parte segunda")
num_usuario = int(input("Introduzca un numero del 1 al 9: "))
resuelto1 = (num_usuario*(num_usuario+1))/2
print(resuelto1)
print("--------------")
print("Parte tercera")
num_user1 = int(input("Introduzca un primer digito: "))
num_user2 = int(input("Introduzca un segundo digito: "))
print(f"Los dos digitos introducidos son {num_user1} y {num_user2}.")
print(f"Si estos dos numeros se dividen entre si, el resultado seria: {num_user1/num_user2}, y el resto seria {num_user1%num_user2}")
