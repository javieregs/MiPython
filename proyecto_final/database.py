"""
Módulo de Base de Datos
=======================
Gestiona todas las operaciones de base de datos SQLite.
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Optional
from .models import Tarea, Usuario, Estado, Prioridad


class GestorBaseDatos:
    """Clase para gestionar la base de datos SQLite"""
    
    def __init__(self, db_name="tareas.db"):
        """
        Inicializa el gestor de base de datos.
        
        Args:
            db_name: Nombre del archivo de base de datos
        """
        self.db_name = db_name
        self.conn = None
        self._conectar()
        self._crear_tablas()
    
    def _conectar(self):
        """Establece conexión con la base de datos"""
        try:
            self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row  # Permite acceso por nombre de columna
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            raise
    
    def _crear_tablas(self):
        """Crea las tablas necesarias si no existen"""
        try:
            cursor = self.conn.cursor()
            
            # Tabla de usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    fecha_registro TEXT NOT NULL
                )
            """)
            
            # Tabla de tareas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    descripcion TEXT,
                    prioridad TEXT NOT NULL,
                    estado TEXT NOT NULL DEFAULT 'pendiente',
                    fecha_creacion TEXT NOT NULL,
                    fecha_limite TEXT,
                    fecha_completada TEXT,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                )
            """)
            
            # Índices para mejorar el rendimiento
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_estado ON tareas(estado)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_prioridad ON tareas(prioridad)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_usuario ON tareas(usuario_id)
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")
            raise
    
    # MÉTODOS PARA USUARIOS
    def crear_usuario(self, nombre: str, email: str) -> Optional[Usuario]:
        """Crea un nuevo usuario"""
        try:
            cursor = self.conn.cursor()
            fecha_registro = datetime.now().isoformat()
            
            cursor.execute("""
                INSERT INTO usuarios (nombre, email, fecha_registro)
                VALUES (?, ?, ?)
            """, (nombre, email, fecha_registro))
            
            self.conn.commit()
            usuario_id = cursor.lastrowid
            
            usuario = Usuario(nombre, email)
            usuario.id = usuario_id
            usuario.fecha_registro = datetime.fromisoformat(fecha_registro)
            
            return usuario
        except sqlite3.IntegrityError:
            print(f"Error: El email {email} ya está registrado")
            return None
        except sqlite3.Error as e:
            print(f"Error al crear usuario: {e}")
            return None
    
    def obtener_usuario(self, usuario_id: int) -> Optional[Usuario]:
        """Obtiene un usuario por ID"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
            row = cursor.fetchone()
            
            if row:
                return Usuario.from_dict(dict(row))
            return None
        except sqlite3.Error as e:
            print(f"Error al obtener usuario: {e}")
            return None
    
    # MÉTODOS PARA TAREAS
    def crear_tarea(self, tarea: Tarea, usuario_id: Optional[int] = None) -> Optional[Tarea]:
        """Crea una nueva tarea"""
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                INSERT INTO tareas (titulo, descripcion, prioridad, estado, 
                                   fecha_creacion, fecha_limite, fecha_completada, usuario_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                tarea.titulo,
                tarea.descripcion,
                tarea.prioridad.value,
                tarea.estado.value,
                tarea.fecha_creacion.isoformat(),
                tarea.fecha_limite.isoformat() if tarea.fecha_limite else None,
                tarea.fecha_completada.isoformat() if tarea.fecha_completada else None,
                usuario_id
            ))
            
            self.conn.commit()
            tarea.id = cursor.lastrowid
            return tarea
        except sqlite3.Error as e:
            print(f"Error al crear tarea: {e}")
            return None
    
    def obtener_tarea(self, tarea_id: int) -> Optional[Tarea]:
        """Obtiene una tarea por ID"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,))
            row = cursor.fetchone()
            
            if row:
                return self._row_a_tarea(row)
            return None
        except sqlite3.Error as e:
            print(f"Error al obtener tarea: {e}")
            return None
    
    def obtener_tareas(self, usuario_id: Optional[int] = None, 
                      estado: Optional[Estado] = None,
                      prioridad: Optional[Prioridad] = None) -> List[Tarea]:
        """Obtiene todas las tareas con filtros opcionales"""
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM tareas WHERE 1=1"
            params = []
            
            if usuario_id:
                query += " AND usuario_id = ?"
                params.append(usuario_id)
            
            if estado:
                query += " AND estado = ?"
                params.append(estado.value)
            
            if prioridad:
                query += " AND prioridad = ?"
                params.append(prioridad.value)
            
            query += " ORDER BY fecha_creacion DESC"
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            return [self._row_a_tarea(row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error al obtener tareas: {e}")
            return []
    
    def actualizar_tarea(self, tarea: Tarea) -> bool:
        """Actualiza una tarea existente"""
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                UPDATE tareas 
                SET titulo = ?, descripcion = ?, prioridad = ?, estado = ?,
                    fecha_limite = ?, fecha_completada = ?
                WHERE id = ?
            """, (
                tarea.titulo,
                tarea.descripcion,
                tarea.prioridad.value,
                tarea.estado.value,
                tarea.fecha_limite.isoformat() if tarea.fecha_limite else None,
                tarea.fecha_completada.isoformat() if tarea.fecha_completada else None,
                tarea.id
            ))
            
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al actualizar tarea: {e}")
            return False
    
    def eliminar_tarea(self, tarea_id: int) -> bool:
        """Elimina una tarea"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al eliminar tarea: {e}")
            return False
    
    def _row_a_tarea(self, row) -> Tarea:
        """Convierte una fila de la BD a un objeto Tarea"""
        datos = dict(row)
        tarea = Tarea(
            titulo=datos["titulo"],
            descripcion=datos.get("descripcion", ""),
            prioridad=Prioridad(datos["prioridad"]),
            fecha_limite=datos.get("fecha_limite")
        )
        tarea.id = datos["id"]
        tarea.estado = Estado(datos["estado"])
        
        if datos.get("fecha_creacion"):
            tarea.fecha_creacion = datetime.fromisoformat(datos["fecha_creacion"])
        if datos.get("fecha_limite"):
            tarea.fecha_limite = datetime.fromisoformat(datos["fecha_limite"])
        if datos.get("fecha_completada"):
            tarea.fecha_completada = datetime.fromisoformat(datos["fecha_completada"])
        
        return tarea
    
    def obtener_estadisticas(self, usuario_id: Optional[int] = None) -> dict:
        """Obtiene estadísticas de las tareas"""
        try:
            cursor = self.conn.cursor()
            query = "SELECT estado, COUNT(*) as cantidad FROM tareas"
            params = []
            
            if usuario_id:
                query += " WHERE usuario_id = ?"
                params.append(usuario_id)
            
            query += " GROUP BY estado"
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            estadisticas = {
                "total": 0,
                "pendientes": 0,
                "en_progreso": 0,
                "completadas": 0,
                "canceladas": 0
            }
            
            for row in rows:
                estado = row["estado"]
                cantidad = row["cantidad"]
                estadisticas["total"] += cantidad
                
                if estado == "pendiente":
                    estadisticas["pendientes"] = cantidad
                elif estado == "en_progreso":
                    estadisticas["en_progreso"] = cantidad
                elif estado == "completada":
                    estadisticas["completadas"] = cantidad
                elif estado == "cancelada":
                    estadisticas["canceladas"] = cantidad
            
            return estadisticas
        except sqlite3.Error as e:
            print(f"Error al obtener estadísticas: {e}")
            return {}
    
    def cerrar(self):
        """Cierra la conexión con la base de datos"""
        if self.conn:
            self.conn.close()

