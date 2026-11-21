#Crea otro array con 15 n�meros decimales aleatorios entre 0 y 1

import numpy as np

rng = np.random.default_rng(seed=42)

array1 = rng.integers(1,101,15)

array2 = rng.random(15)

print(array1)
print("----")
print(array2)
