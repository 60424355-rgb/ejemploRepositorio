import mysql.connector

# conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost", user="root", password="admin", database="facturacion_db"
)
cursor = conn.cursor()

#Ejecutar el SELECT
cursor.execute("SELECT * FROM articulos")
resultado = cursor.fetchall()

# Mostrar ñps datos
for fila in resultado:
    print(fila)

#cerrar conexion
conn.close()