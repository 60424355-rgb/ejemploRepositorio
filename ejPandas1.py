import pandas as pd
# CSV → DataFrame → [filtrar, agrupar, calcular] → resultado / nuevo CSV
# Leer CSV
df = pd.read_csv("ventas.csv")

# Ver las primeras filas
print(df.head())

# Información general: tipos de datos y nulos
print(df.info())

# Estadísticas descriptivas de columnas numéricas
print(df.describe())

# Dimensiones
print(df.shape)   # (10, 6)