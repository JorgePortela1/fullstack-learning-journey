'''
REPITE LOS CARACTERES:
Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
duplicados. Si el input es 'sbcd56', el output debera ser 'ssbbcc5566'
'''

texto = input("Escribe una palabra: (solo 5 caracteres): ")

txt_modificado = (f"{texto[0]*2}{texto[1]*2}{texto[2]*2}{texto[3]*2}{texto[4]*2}")

print(txt_modificado)
