import sympy as sp

# Definir símbolos
x, y = sp.symbols('x y')

# Simplificar expresiones
expr = (x**2 - 1) / (x - 1)
print(sp.simplify(expr))        # x + 1

# Expandir
print(sp.expand((x + 1)**3))    # x**3 + 3*x**2 + 3*x + 1

# Factorizar
print(sp.factor(x**2 - 4))      # (x - 2)*(x + 2)

# Resolver ecuaciones
print(sp.solve(x**2 - 4, x))    # [-2, 2]
print(sp.solve(x + y - 3, x))   # [3 - y]

# Derivadas
print(sp.diff(x**3, x))         # 3*x**2
print(sp.diff(sp.sin(x), x))    # cos(x)

# Integrales
print(sp.integrate(x**2, x))          # x**3/3
print(sp.integrate(sp.exp(-x), (x, 0, sp.oo)))  # 1

# Límites
print(sp.limit(sp.sin(x)/x, x, 0))    # 1

# Valores exactos (no decimales)
print(sp.sqrt(8))               # 2*sqrt(2)
print(sp.pi)                    # pi
print(sp.E)                     # E

# Convertir a decimal
print(sp.N(sp.sqrt(8)))         # 2.82842712474619

# Evaluar numéricamente una expresión
f = sp.lambdify(x, x**2 + 1, 'numpy')
print(f(3))                     # 10