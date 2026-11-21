# Multiplica todos los numeros del array usando un bucle y 
# despues usando un metodo numpy. Compara los resultados.

# importar libreria numpy

import numpy as np

array1 = np.random.randint(1,101,size=15)

print(array1)

total = 1

for i in array1:
	total = total * i

mult_array1 = array1.prod()

print(mult_array1)
print(total)

if mult_array1 == total:
	print("Los dos metodos dan el mismo resultado")
else:
	print("Los dos metodos no dan el mismo resultado")
