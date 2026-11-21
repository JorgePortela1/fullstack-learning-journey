"""Ejercicio: Base de datos de colegio."""


# Seguimientos de notas
# lista con nombres de estudiantes
# en otra sus notas de deberes, examenes y proyectos
# calcular la nota media del alumno y de la clase

alumnos = ["Paola","Kari","Alejo","Aitana","Jorge"]
notas_deberes = ["6.8","9.6","2.9","6.2","7.2"]
notas_examenes = ["8","9","5","8","4"]
notas_proyectos = ["5","5","7","4","8"]

medias_alumnos = []

datos = zip(alumnos, notas_deberes, notas_examenes, notas_proyectos)

print("Presentacion de Notas ")

for alumno, deberes, examenes,proyectos in datos:
	print(f"{alumno}: {deberes},{examenes},{proyectos}")
	total_notas = float(deberes) + float(examenes) + float(proyectos)
	media = total_notas / 3
	print(f"La nota media de {alumno} es de {media:.2f}")
	medias_alumnos.append(media)
	print("------------")


total_clase = sum(medias_alumnos)
media_clase = total_clase / 5

print(f"La media de la clase es de {media_clase:.2f}")
