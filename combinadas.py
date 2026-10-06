import math, numpy as np, sympy as sp

print(math.sqrt(2))          # 1.4142135623730951  (float)
print(np.sqrt(2))            # 1.4142135623730951  (float)
print(sp.sqrt(2))            # sqrt(2)             (exacto)
print(sp.N(sp.sqrt(2), 20))  # 1.4142135623730950488 (20 decimales)