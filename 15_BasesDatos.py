"""
EJEMPLO 15: BASES DE DATOS
---------------------------
Aprende a trabajar con bases de datos SQLite en Python.
"""

import sqlite3
import os

# CREAR Y CONECTAR A UNA BASE DE DATOS
print("=== CREAR BASE DE DATOS SQLITE ===")

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# CREAR TABLA
print("\n1. Crear tabla:")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        carrera TEXT,
        nota REAL
    )
""")
conn.commit()
print("Tabla 'estudiantes' creada correctamente")

# INSERTAR DATOS
print("\n2. Insertar datos:")
estudiantes = [
    ("Ana García", 20, "Informática", 85.5),
    ("Carlos López", 22, "Ingeniería", 90.0),
    ("María Rodríguez", 21, "Medicina", 88.5),
    ("Juan Pérez", 23, "Informática", 92.0),
    ("Laura Martín", 20, "Derecho", 87.0)
]

cursor.executemany("""
    INSERT INTO estudiantes (nombre, edad, carrera, nota)
    VALUES (?, ?, ?, ?)
""", estudiantes)
conn.commit()
print(f"{len(estudiantes)} estudiantes insertados")

# CONSULTAR DATOS
print("\n3. Consultar todos los datos:")
cursor.execute("SELECT * FROM estudiantes")
estudiantes = cursor.fetchall()

print(f"{'ID':<5} {'Nombre':<20} {'Edad':<6} {'Carrera':<15} {'Nota':<6}")
print("-" * 60)
for estudiante in estudiantes:
    print(f"{estudiante[0]:<5} {estudiante[1]:<20} {estudiante[2]:<6} {estudiante[3]:<15} {estudiante[4]:<6}")

# CONSULTAS CON FILTROS
print("\n4. Consultas con filtros:")
print("\nEstudiantes de Informática:")
cursor.execute("""
    SELECT nombre, nota FROM estudiantes 
    WHERE carrera = ? 
    ORDER BY nota DESC
""", ("Informática",))

for row in cursor.fetchall():
    print(f"- {row[0]}: {row[1]}")

print("\nEstudiantes con nota mayor a 88:")
cursor.execute("""
    SELECT nombre, carrera, nota FROM estudiantes 
    WHERE nota > ? 
    ORDER BY nota DESC
""", (88,))

for row in cursor.fetchall():
    print(f"- {row[0]} ({row[1]}): {row[2]}")

# FUNCIONES AGREGADAS
print("\n5. Funciones agregadas:")
cursor.execute("SELECT COUNT(*) FROM estudiantes")
total = cursor.fetchone()[0]
print(f"Total de estudiantes: {total}")

cursor.execute("SELECT AVG(nota) FROM estudiantes")
promedio = cursor.fetchone()[0]
print(f"Promedio de notas: {promedio:.2f}")

cursor.execute("SELECT MAX(nota) FROM estudiantes")
max_nota = cursor.fetchone()[0]
print(f"Nota máxima: {max_nota}")

cursor.execute("SELECT carrera, COUNT(*) FROM estudiantes GROUP BY carrera")
print("\nEstudiantes por carrera:")
for row in cursor.fetchall():
    print(f"- {row[0]}: {row[1]} estudiantes")

# ACTUALIZAR DATOS
print("\n6. Actualizar datos:")
cursor.execute("""
    UPDATE estudiantes 
    SET nota = nota + 1 
    WHERE carrera = 'Informática'
""")
conn.commit()

cursor.execute("SELECT nombre, nota FROM estudiantes WHERE carrera = 'Informática'")
print("Notas actualizadas (Informática):")
for row in cursor.fetchall():
    print(f"- {row[0]}: {row[1]}")

# ELIMINAR DATOS
print("\n7. Eliminar datos:")
cursor.execute("DELETE FROM estudiantes WHERE nota < 85")
conn.commit()
deleted = cursor.rowcount
print(f"Estudiantes eliminados: {deleted}")

cursor.execute("SELECT COUNT(*) FROM estudiantes")
total_actualizado = cursor.fetchone()[0]
print(f"Estudiantes restantes: {total_actualizado}")

# CLASE PARA GESTIÓN DE BASE DE DATOS
print("\n8. Clase para gestión de base de datos:")

class GestorEstudiantes:
    """Clase para gestionar estudiantes en la base de datos"""
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tabla()
    
    def _crear_tabla(self):
        """Crea la tabla si no existe"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                carrera TEXT,
                nota REAL
            )
        """)
        self.conn.commit()
    
    def agregar_estudiante(self, nombre, edad, carrera, nota):
        """Agrega un nuevo estudiante"""
        try:
            self.cursor.execute("""
                INSERT INTO estudiantes (nombre, edad, carrera, nota)
                VALUES (?, ?, ?, ?)
            """, (nombre, edad, carrera, nota))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al agregar estudiante: {e}")
            return None
    
    def obtener_estudiantes(self, carrera=None):
        """Obtiene todos los estudiantes o filtrados por carrera"""
        if carrera:
            self.cursor.execute("""
                SELECT * FROM estudiantes WHERE carrera = ?
            """, (carrera,))
        else:
            self.cursor.execute("SELECT * FROM estudiantes")
        return self.cursor.fetchall()
    
    def actualizar_nota(self, id_estudiante, nueva_nota):
        """Actualiza la nota de un estudiante"""
        try:
            self.cursor.execute("""
                UPDATE estudiantes SET nota = ? WHERE id = ?
            """, (nueva_nota, id_estudiante))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al actualizar nota: {e}")
            return False
    
    def eliminar_estudiante(self, id_estudiante):
        """Elimina un estudiante"""
        try:
            self.cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al eliminar estudiante: {e}")
            return False
    
    def cerrar(self):
        """Cierra la conexión"""
        self.conn.close()

# Usar la clase
gestor = GestorEstudiantes("gestor_estudiantes.db")

id1 = gestor.agregar_estudiante("Pedro Sánchez", 24, "Ingeniería", 91.0)
id2 = gestor.agregar_estudiante("Elena Ruiz", 21, "Medicina", 89.5)

print("\nEstudiantes agregados usando la clase:")
for estudiante in gestor.obtener_estudiantes():
    print(f"- {estudiante[1]} ({estudiante[3]}): {estudiante[4]}")

gestor.cerrar()

# Cerrar conexión principal
conn.close()

print("\n=== Base de datos cerrada ===")
print("\nBases de datos creadas:")
if os.path.exists("ejemplo.db"):
    print("- ejemplo.db")
if os.path.exists("gestor_estudiantes.db"):
    print("- gestor_estudiantes.db")

