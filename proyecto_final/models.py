"""
Módulo de Modelos
=================
Define las clases para representar tareas y usuarios.
"""

from datetime import datetime
from enum import Enum


class Prioridad(Enum):
    """Enum para representar las prioridades de las tareas"""
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"
    URGENTE = "urgente"


class Estado(Enum):
    """Enum para representar los estados de las tareas"""
    PENDIENTE = "pendiente"
    EN_PROGRESO = "en_progreso"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"


class Tarea:
    """Clase que representa una tarea"""
    
    def __init__(self, titulo, descripcion="", prioridad=Prioridad.MEDIA, fecha_limite=None):
        """
        Inicializa una nueva tarea.
        
        Args:
            titulo: Título de la tarea (requerido)
            descripcion: Descripción detallada de la tarea
            prioridad: Prioridad de la tarea (Prioridad enum)
            fecha_limite: Fecha límite (datetime o string)
        """
        if not titulo or len(titulo.strip()) == 0:
            raise ValueError("El título de la tarea no puede estar vacío")
        
        self.id = None  # Se asignará al guardar en la base de datos
        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.prioridad = prioridad if isinstance(prioridad, Prioridad) else Prioridad[prioridad.upper()]
        self.estado = Estado.PENDIENTE
        self.fecha_creacion = datetime.now()
        self.fecha_limite = self._parsear_fecha(fecha_limite) if fecha_limite else None
        self.fecha_completada = None
    
    def _parsear_fecha(self, fecha):
        """Convierte una fecha string a datetime"""
        if isinstance(fecha, datetime):
            return fecha
        try:
            # Intentar diferentes formatos
            formatos = ["%Y-%m-%d", "%d/%m/%Y", "%Y-%m-%d %H:%M:%S"]
            for formato in formatos:
                try:
                    return datetime.strptime(fecha, formato)
                except ValueError:
                    continue
            raise ValueError(f"Formato de fecha no reconocido: {fecha}")
        except Exception as e:
            raise ValueError(f"Error al parsear fecha: {e}")
    
    def marcar_completada(self):
        """Marca la tarea como completada"""
        self.estado = Estado.COMPLETADA
        self.fecha_completada = datetime.now()
    
    def marcar_en_progreso(self):
        """Marca la tarea como en progreso"""
        self.estado = Estado.EN_PROGRESO
    
    def cancelar(self):
        """Cancela la tarea"""
        self.estado = Estado.CANCELADA
    
    def esta_vencida(self):
        """Verifica si la tarea está vencida"""
        if self.fecha_limite and self.estado != Estado.COMPLETADA:
            return datetime.now() > self.fecha_limite
        return False
    
    def to_dict(self):
        """Convierte la tarea a un diccionario"""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad.value,
            "estado": self.estado.value,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "fecha_limite": self.fecha_limite.isoformat() if self.fecha_limite else None,
            "fecha_completada": self.fecha_completada.isoformat() if self.fecha_completada else None
        }
    
    @classmethod
    def from_dict(cls, datos):
        """Crea una tarea desde un diccionario"""
        tarea = cls(
            titulo=datos["titulo"],
            descripcion=datos.get("descripcion", ""),
            prioridad=Prioridad(datos.get("prioridad", "media")),
            fecha_limite=datos.get("fecha_limite")
        )
        tarea.id = datos.get("id")
        tarea.estado = Estado(datos.get("estado", "pendiente"))
        if datos.get("fecha_creacion"):
            tarea.fecha_creacion = datetime.fromisoformat(datos["fecha_creacion"])
        if datos.get("fecha_limite"):
            tarea.fecha_limite = datetime.fromisoformat(datos["fecha_limite"])
        if datos.get("fecha_completada"):
            tarea.fecha_completada = datetime.fromisoformat(datos["fecha_completada"])
        return tarea
    
    def __str__(self):
        """Representación en string de la tarea"""
        estado_icono = {
            Estado.PENDIENTE: "⏳",
            Estado.EN_PROGRESO: "🔄",
            Estado.COMPLETADA: "✅",
            Estado.CANCELADA: "❌"
        }
        
        prioridad_icono = {
            Prioridad.BAJA: "🟢",
            Prioridad.MEDIA: "🟡",
            Prioridad.ALTA: "🟠",
            Prioridad.URGENTE: "🔴"
        }
        
        icono_estado = estado_icono.get(self.estado, "")
        icono_prioridad = prioridad_icono.get(self.prioridad, "")
        vencida = "⚠️" if self.esta_vencida() else ""
        
        fecha_str = self.fecha_limite.strftime("%d/%m/%Y") if self.fecha_limite else "Sin fecha límite"
        
        return f"{icono_estado} {icono_prioridad} {self.titulo} [{self.estado.value}] - {fecha_str} {vencida}"


class Usuario:
    """Clase que representa un usuario del sistema"""
    
    def __init__(self, nombre, email):
        """
        Inicializa un nuevo usuario.
        
        Args:
            nombre: Nombre del usuario
            email: Email del usuario
        """
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")
        if not email or "@" not in email:
            raise ValueError("El email no es válido")
        
        self.id = None
        self.nombre = nombre.strip()
        self.email = email.strip()
        self.fecha_registro = datetime.now()
    
    def to_dict(self):
        """Convierte el usuario a un diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "fecha_registro": self.fecha_registro.isoformat()
        }
    
    @classmethod
    def from_dict(cls, datos):
        """Crea un usuario desde un diccionario"""
        usuario = cls(
            nombre=datos["nombre"],
            email=datos["email"]
        )
        usuario.id = datos.get("id")
        if datos.get("fecha_registro"):
            usuario.fecha_registro = datetime.fromisoformat(datos["fecha_registro"])
        return usuario
    
    def __str__(self):
        """Representación en string del usuario"""
        return f"{self.nombre} ({self.email})"

