''' 
MENSAJE DE BIENVENIDA:
Crear un script que pregunte el nombre, y despues le de la bienvenida 
con su nombre en el formato correcto, es decir, con la primera 
letra en mayuscula y el resto en minuscula.

Create a scrip where ask for name, and then, the script give a welcome
message with a proper format, capital letter and then minus
'''
# First, I create the variable where ask to user:

name_user = input("Hey, Whats your name? ")

# -----  NOTES  -----
# .capitalize() is just for the first word, and
# .title() is for every word in a sentence.
# .replace() can be used for possible mistakes from user, like
# 	in the middle of the name, misstype a dot. for example:
#	name_user.replace(".","")

name_user = name_user.replace(".","")
name_user = name_user.capitalize()

# Create a variable that print "You are using Python

txt = str("You are using Python.")

# Now, print all together

print("Welcome ", name_user, ", ", txt)
