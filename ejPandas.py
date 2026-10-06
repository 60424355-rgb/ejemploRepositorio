# ============================================================
# EJEMPLO COMPLETO: crear un CSV y analizarlo con pandas
# ============================================================
# CSV → DataFrame → [filtrar, agrupar, calcular] → resultado / nuevo CSV
import csv
import pandas as pd

# ------------------------------------------------------------
# PASO 1: Crear el archivo ventas.csv
# ------------------------------------------------------------
datos = [
    ["fecha", "producto", "categoria", "cantidad", "precio", "ciudad"],
    ["2024-01-05", "Laptop",     "Tecnología", 2,  1200.00, "Lima"],
    ["2024-01-06", "Mouse",      "Tecnología", 10,   25.50, "Lima"],
    ["2024-01-07", "Silla",      "Muebles",    4,   150.00, "Bogotá"],
    ["2024-01-08", "Monitor",    "Tecnología", 3,   300.00, "Lima"],
    ["2024-01-09", "Escritorio", "Muebles",    2,   450.00, "Bogotá"],
    ["2024-01-10", "Teclado",    "Tecnología", 8,    45.00, "Santiago"],
    ["2024-01-11", "Lámpara",    "Hogar",      6,    35.00, "Santiago"],
    ["2024-01-12", "Laptop",     "Tecnología", 1,  1200.00, "Bogotá"],
    ["2024-01-13", "Mouse",      "Tecnología", 15,   25.50, "Lima"],
    ["2024-01-14", "Silla",      "Muebles",    3,   150.00, "Santiago"],
]

with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(datos)

print("=" * 60)
print("Archivo 'ventas.csv' creado correctamente ✅")
print("=" * 60)


# ------------------------------------------------------------
# PASO 2: Leer el CSV con pandas
# ------------------------------------------------------------
df = pd.read_csv("ventas.csv")

print("\n>>> Primeras 5 filas (head):")
print(df.head())

print("\n>>> Dimensiones (filas, columnas):")
print(df.shape)

print("\n>>> Tipos de datos e información general:")
df.info()

print("\n>>> Estadísticas descriptivas:")
print(df.describe())


# ------------------------------------------------------------
# PASO 3: Crear columna calculada (total por venta)
# ------------------------------------------------------------
df["total"] = df["cantidad"] * df["precio"]

print("\n>>> DataFrame con la columna 'total':")
print(df[["producto", "cantidad", "precio", "total"]])


# ------------------------------------------------------------
# PASO 4: Filtrar filas
# ------------------------------------------------------------
print("\n>>> Solo ventas de la categoría 'Tecnología':")
tec = df[df["categoria"] == "Tecnología"]
print(tec[["producto", "ciudad", "total"]])

print("\n>>> Ventas con total mayor a 500:")
grandes = df[df["total"] > 500]
print(grandes[["producto", "ciudad", "total"]])

print("\n>>> Ventas en Lima con total mayor a 100:")
filtro = df[(df["ciudad"] == "Lima") & (df["total"] > 100)]
print(filtro[["producto", "total"]])


# ------------------------------------------------------------
# PASO 5: Agrupaciones y resúmenes
# ------------------------------------------------------------
print("\n>>> Total vendido por categoría:")
print(df.groupby("categoria")["total"].sum())

print("\n>>> Resumen por ciudad:")
resumen = df.groupby("ciudad").agg(
    total_ventas=("total", "sum"),
    unidades=("cantidad", "sum"),
    operaciones=("producto", "count"),
    ticket_promedio=("total", "mean")
)
print(resumen)


# ------------------------------------------------------------
# PASO 6: Ordenar y obtener los Top N
# ------------------------------------------------------------
print("\n>>> Top 3 ventas más altas:")
print(df.nlargest(3, "total")[["producto", "ciudad", "total"]])

print("\n>>> Ordenado por ciudad (asc) y total (desc):")
print(df.sort_values(["ciudad", "total"], ascending=[True, False])
        [["ciudad", "producto", "total"]])


# ------------------------------------------------------------
# PASO 7: Valores únicos y conteos
# ------------------------------------------------------------
print("\n>>> Ciudades únicas:")
print(df["ciudad"].unique())

print("\n>>> Frecuencia de productos vendidos:")
print(df["producto"].value_counts())


# ------------------------------------------------------------
# PASO 8: Manejo de fechas
# ------------------------------------------------------------
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")

print("\n>>> Total vendido por mes:")
print(df.groupby("mes")["total"].sum())


# ------------------------------------------------------------
# PASO 9: Guardar resultados
# ------------------------------------------------------------
df.to_csv("ventas_con_total.csv", index=False)
print("\nArchivo 'ventas_con_total.csv' guardado correctamente ✅")

# Si tienes openpyxl instalado, también puedes exportar a Excel:
# df.to_excel("ventas_con_total.xlsx", index=False)


# ------------------------------------------------------------
# PASO 10: Resumen final (extra)
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("RESUMEN FINAL")
print("=" * 60)
print(f"Total de ventas (ingresos): ${df['total'].sum():,.2f}")
print(f"Unidades vendidas:          {df['cantidad'].sum()}")
print(f"Número de operaciones:      {len(df)}")
print(f"Ticket promedio:            ${df['total'].mean():,.2f}")
print(f"Categoría más rentable:     {df.groupby('categoria')['total'].sum().idxmax()}")
print(f"Ciudad con más ventas:      {df.groupby('ciudad')['total'].sum().idxmax()}")
print(f"Producto más vendido:       {df['producto'].value_counts().idxmax()}")
print("=" * 60)