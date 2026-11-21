# Encuentra el valor mas alto del primer array creado

import numpy as np

rng = np.random.default_rng()

array1 = rng.integers(1,101,15)

mayor = array1.max()

print(mayor)
