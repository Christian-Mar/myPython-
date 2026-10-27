import math
import timeit

import numpy as np

x = np.linspace(0, 10, 1_000_000)

n = 5  # aantal herhalingen per methode


def numpy_sin():
    return np.sin(x)


def listcomp_tolist():
    return [math.sin(v) for v in x.tolist()]


def listcomp_array():
    return [math.sin(v) for v in x]


for naam, f in [
    ("np.sin(x)", numpy_sin),
    ("math.sin over x.tolist()", listcomp_tolist),
    ("math.sin over x (array)", listcomp_array),
]:
    t = timeit.timeit(f, number=n) / n
    print(f"{naam:28s} {t * 1000:10.2f} ms")

# Uitleg van de ranking (snelst -> langzaamst):
# 1. np.sin(x): de lus draait in gecompileerde C-code over een aaneengesloten
#    blok float64's, zonder Python-objecten of interpreter-overhead per element
#    (en vaak met SIMD-instructies).
# 2. math.sin over x.tolist(): .tolist() zet de array in één keer om naar gewone
#    Python floats. Daarna doet de list comprehension per element nog een
#    Python-functieaanroep, maar het itereren is goedkoop.
# 3. math.sin over x (de array zelf): bij het itereren over een array maakt NumPy
#    voor elk element een nieuw np.float64-object (een "scalar") aan, en
#    math.sin moet dat weer omzetten naar een C double. Dat is per element
#    duurder dan bij een gewone Python float.
