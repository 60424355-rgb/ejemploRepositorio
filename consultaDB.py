import sqlite3
import sys

def buscar_persona_por_nombre():
    """
    Busca personas en la base de datos 'contactos.db' por un nombre
    ingresado como argumento desde la línea de comandos.
    """
    if len(sys.argv) < 2:
        print("Uso: python tu_script.py <nombre_a_buscar>")
        print("Ejemplo: python tu_script.py Juan")
        sys.exit(1)

    nombre_a_buscar = sys.argv[1]
    
    try:
        # Conectar a la base de datos (se creará si no existe)
        conn = sqlite3.connect('contactos.db')
        cursor = conn.cursor()

        # Crear la tabla 'personas' si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Apellido TEXT,
                Email TEXT
            )
        ''')
        conn.commit()

        # Insertar algunos datos de ejemplo si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM personas")
        if cursor.fetchone()[0] == 0:
            print("La base de datos está vacía. Insertando datos de ejemplo...")
            cursor.execute("INSERT INTO personas (Nombre, Apellido, Email) VALUES ('Juan', 'Pérez', 'juan.perez@example.com')")
            cursor.execute("INSERT INTO personas (Nombre, Apellido, Email) VALUES ('María', 'González', 'maria.gonzalez@example.com')")
            cursor.execute("INSERT INTO personas (Nombre, Apellido, Email) VALUES ('Pedro', 'Rodríguez', 'pedro.rodriguez@example.com')")
            conn.commit()
            print("Datos de ejemplo insertados.")

        # Realizar la consulta SELECT
        # Usamos LIKE para búsquedas parciales y ? para evitar inyección SQL
        cursor.execute("SELECT id, Nombre, Apellido, Email FROM personas WHERE Nombre LIKE ?", ('%' + nombre_a_buscar + '%',))

        resultados = cursor.fetchall()

        if resultados:
            print(f"\nResultados de la búsqueda para '{nombre_a_buscar}':")
            print("-" * 40)
            for persona in resultados:
                print(f"ID: {persona[0]}, Nombre: {persona[1]}, Apellido: {persona[2]}, Email: {persona[3]}")
            print("-" * 40)
        else:
            print(f"\nNo se encontraron personas con el nombre '{nombre_a_buscar}'.")

    except sqlite3.Error as e:
        print(f"Error de SQLite: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    buscar_persona_por_nombre()