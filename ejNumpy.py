import numpy as np

# Crear arreglos
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Operaciones elemento a elemento (sin bucles)
print(a + b)          # [11 22 33 44]
print(a * 2)          # [ 2  4  6  8]
print(a ** 2)         # [ 1  4  9 16]

# Funciones matemáticas vectorizadas
print(np.sqrt(a))     # [1.  1.41 1.73 2. ]
print(np.sin(a))      # [0.84 0.91 0.14 -0.76]

# Estadísticas
print(a.mean())       # 2.5
print(a.sum())        # 10
print(a.max())        # 4

# Crear secuencias
print(np.arange(0, 10, 2))    # [0 2 4 6 8]
print(np.linspace(0, 1, 5))   # [0.   0.25 0.5  0.75 1.  ]

# Matrices
m = np.array([[1, 2], [3, 4]])
print(m @ m)          # Producto matricial
# [[ 7 10]
#  [15 22]]

# Matriz identidad
print(np.eye(3))