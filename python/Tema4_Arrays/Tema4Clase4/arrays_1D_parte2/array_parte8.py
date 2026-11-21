# Calcula la media, mediana y desviacion standar de los arrays

import numpy as np

rng = np.random.default_rng(seed=42)

array1 = rng.integers(1,101,15)

media_array1 = np.mean(array1)
desStandard_array1 = np.std(array1)
mediana_array1 = np.median(array1)

print(f"La media del array es: {media_array1}. La desviacion standar es: {desStandard_array1}. Y la mediana es : {mediana_array1}")

