import mysql.connector

# conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost", user="root", password="admin", database="facturacion_db"
)
cursor = conn.cursor()
criterio = input("Ingresa e criterio de busqueda: ")
query=f"SELECT * FROM articulos WHERE descripcion like \'%{criterio}\';"
print(f"CONSULTA: {query}")

#Ejecutar el SELECT
cursor.execute(query)
resultado = cursor.fetchall()

# Mostrar ñps datos
for fila in resultado:
    print(f"El codigo {fila[1]} corresponde a {fila[2]} y vale {fila[4]}")

#cerrar conexion
conn.close()