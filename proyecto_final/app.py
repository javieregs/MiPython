"""
Aplicación Principal
====================
Sistema de Gestión de Tareas - Interfaz de línea de comandos
"""

from datetime import datetime
from .database import GestorBaseDatos
from .models import Tarea, Usuario, Prioridad, Estado


class AplicacionTareas:
    """Clase principal de la aplicación"""
    
    def __init__(self):
        """Inicializa la aplicación"""
        self.db = GestorBaseDatos()
        self.usuario_actual = None
    
    def menu_principal(self):
        """Muestra el menú principal"""
        while True:
            print("\n" + "="*60)
            print("         SISTEMA DE GESTIÓN DE TAREAS")
            print("="*60)
            
            if not self.usuario_actual:
                print("\n1. Registrar nuevo usuario")
                print("2. Iniciar sesión")
                print("0. Salir")
            else:
                print(f"\n👤 Usuario: {self.usuario_actual.nombre}")
                print("\n1. Ver mis tareas")
                print("2. Crear nueva tarea")
                print("3. Actualizar tarea")
                print("4. Completar tarea")
                print("5. Eliminar tarea")
                print("6. Buscar tareas")
                print("7. Ver estadísticas")
                print("8. Cerrar sesión")
                print("0. Salir")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if not self.usuario_actual:
                if opcion == "1":
                    self.registrar_usuario()
                elif opcion == "2":
                    self.iniciar_sesion()
                elif opcion == "0":
                    print("\n¡Hasta luego!")
                    break
                else:
                    print("❌ Opción inválida")
            else:
                if opcion == "1":
                    self.ver_tareas()
                elif opcion == "2":
                    self.crear_tarea()
                elif opcion == "3":
                    self.actualizar_tarea()
                elif opcion == "4":
                    self.completar_tarea()
                elif opcion == "5":
                    self.eliminar_tarea()
                elif opcion == "6":
                    self.buscar_tareas()
                elif opcion == "7":
                    self.ver_estadisticas()
                elif opcion == "8":
                    self.usuario_actual = None
                    print("✅ Sesión cerrada")
                elif opcion == "0":
                    print("\n¡Hasta luego!")
                    break
                else:
                    print("❌ Opción inválida")
    
    def registrar_usuario(self):
        """Registra un nuevo usuario"""
        print("\n--- REGISTRAR NUEVO USUARIO ---")
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()
        
        if not nombre or not email:
            print("❌ El nombre y el email son requeridos")
            return
        
        usuario = self.db.crear_usuario(nombre, email)
        if usuario:
            print(f"✅ Usuario registrado exitosamente: {usuario}")
        else:
            print("❌ Error al registrar usuario")
    
    def iniciar_sesion(self):
        """Inicia sesión con un usuario existente"""
        print("\n--- INICIAR SESIÓN ---")
        email = input("Email: ").strip()
        
        # Buscar usuario por email (simplificado - en producción usar autenticación)
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        row = cursor.fetchone()
        
        if row:
            self.usuario_actual = Usuario.from_dict(dict(row))
            print(f"✅ Bienvenido, {self.usuario_actual.nombre}!")
        else:
            print("❌ Usuario no encontrado")
    
    def ver_tareas(self):
        """Muestra todas las tareas del usuario"""
        print("\n--- MIS TAREAS ---")
        tareas = self.db.obtener_tareas(usuario_id=self.usuario_actual.id)
        
        if not tareas:
            print("📋 No tienes tareas registradas")
            return
        
        print(f"\nTotal de tareas: {len(tareas)}\n")
        for tarea in tareas:
            print(f"{tarea.id}. {tarea}")
            if tarea.descripcion:
                print(f"   {tarea.descripcion}")
            print()
    
    def crear_tarea(self):
        """Crea una nueva tarea"""
        print("\n--- CREAR NUEVA TAREA ---")
        
        titulo = input("Título (requerido): ").strip()
        if not titulo:
            print("❌ El título es requerido")
            return
        
        descripcion = input("Descripción: ").strip()
        
        print("\nPrioridades disponibles:")
        for i, prioridad in enumerate(Prioridad, 1):
            print(f"{i}. {prioridad.value.capitalize()}")
        
        try:
            opcion_prioridad = int(input("Selecciona prioridad (1-4): ")) - 1
            prioridad = list(Prioridad)[opcion_prioridad]
        except (ValueError, IndexError):
            prioridad = Prioridad.MEDIA
            print("⚠️ Prioridad por defecto: Media")
        
        fecha_limite = input("Fecha límite (YYYY-MM-DD o vacío): ").strip()
        fecha_limite = fecha_limite if fecha_limite else None
        
        try:
            tarea = Tarea(
                titulo=titulo,
                descripcion=descripcion,
                prioridad=prioridad,
                fecha_limite=fecha_limite
            )
            
            tarea = self.db.crear_tarea(tarea, self.usuario_actual.id)
            if tarea:
                print(f"✅ Tarea creada exitosamente: {tarea.titulo}")
            else:
                print("❌ Error al crear la tarea")
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    def actualizar_tarea(self):
        """Actualiza una tarea existente"""
        print("\n--- ACTUALIZAR TAREA ---")
        tarea_id = input("ID de la tarea a actualizar: ").strip()
        
        try:
            tarea_id = int(tarea_id)
            tarea = self.db.obtener_tarea(tarea_id)
            
            if not tarea or tarea.id not in [t.id for t in self.db.obtener_tareas(self.usuario_actual.id)]:
                print("❌ Tarea no encontrada")
                return
            
            print(f"\nTarea actual: {tarea.titulo}")
            nuevo_titulo = input(f"Nuevo título (actual: {tarea.titulo}): ").strip()
            if nuevo_titulo:
                tarea.titulo = nuevo_titulo
            
            nueva_descripcion = input(f"Nueva descripción (actual: {tarea.descripcion}): ").strip()
            if nueva_descripcion:
                tarea.descripcion = nueva_descripcion
            
            print("\nEstados disponibles:")
            for i, estado in enumerate(Estado, 1):
                print(f"{i}. {estado.value.capitalize()}")
            
            nuevo_estado = input(f"Nuevo estado (1-4, vacío para mantener): ").strip()
            if nuevo_estado:
                try:
                    tarea.estado = list(Estado)[int(nuevo_estado) - 1]
                except (ValueError, IndexError):
                    print("⚠️ Estado no válido, se mantiene el actual")
            
            if self.db.actualizar_tarea(tarea):
                print("✅ Tarea actualizada exitosamente")
            else:
                print("❌ Error al actualizar la tarea")
        except ValueError:
            print("❌ ID inválido")
    
    def completar_tarea(self):
        """Marca una tarea como completada"""
        print("\n--- COMPLETAR TAREA ---")
        tarea_id = input("ID de la tarea a completar: ").strip()
        
        try:
            tarea_id = int(tarea_id)
            tarea = self.db.obtener_tarea(tarea_id)
            
            if not tarea or tarea.id not in [t.id for t in self.db.obtener_tareas(self.usuario_actual.id)]:
                print("❌ Tarea no encontrada")
                return
            
            tarea.marcar_completada()
            if self.db.actualizar_tarea(tarea):
                print(f"✅ Tarea '{tarea.titulo}' marcada como completada")
            else:
                print("❌ Error al actualizar la tarea")
        except ValueError:
            print("❌ ID inválido")
    
    def eliminar_tarea(self):
        """Elimina una tarea"""
        print("\n--- ELIMINAR TAREA ---")
        tarea_id = input("ID de la tarea a eliminar: ").strip()
        
        try:
            tarea_id = int(tarea_id)
            tarea = self.db.obtener_tarea(tarea_id)
            
            if not tarea or tarea.id not in [t.id for t in self.db.obtener_tareas(self.usuario_actual.id)]:
                print("❌ Tarea no encontrada")
                return
            
            confirmacion = input(f"¿Estás seguro de eliminar '{tarea.titulo}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                if self.db.eliminar_tarea(tarea_id):
                    print("✅ Tarea eliminada exitosamente")
                else:
                    print("❌ Error al eliminar la tarea")
            else:
                print("❌ Eliminación cancelada")
        except ValueError:
            print("❌ ID inválido")
    
    def buscar_tareas(self):
        """Busca tareas por filtros"""
        print("\n--- BUSCAR TAREAS ---")
        print("Filtros disponibles:")
        print("1. Por estado")
        print("2. Por prioridad")
        print("3. Tareas vencidas")
        
        opcion = input("Selecciona filtro (1-3): ").strip()
        
        if opcion == "1":
            print("\nEstados disponibles:")
            for i, estado in enumerate(Estado, 1):
                print(f"{i}. {estado.value.capitalize()}")
            
            try:
                estado_opcion = int(input("Selecciona estado (1-4): ")) - 1
                estado = list(Estado)[estado_opcion]
                tareas = self.db.obtener_tareas(usuario_id=self.usuario_actual.id, estado=estado)
            except (ValueError, IndexError):
                print("❌ Opción inválida")
                return
        
        elif opcion == "2":
            print("\nPrioridades disponibles:")
            for i, prioridad in enumerate(Prioridad, 1):
                print(f"{i}. {prioridad.value.capitalize()}")
            
            try:
                prioridad_opcion = int(input("Selecciona prioridad (1-4): ")) - 1
                prioridad = list(Prioridad)[prioridad_opcion]
                tareas = self.db.obtener_tareas(usuario_id=self.usuario_actual.id, prioridad=prioridad)
            except (ValueError, IndexError):
                print("❌ Opción inválida")
                return
        
        elif opcion == "3":
            todas_tareas = self.db.obtener_tareas(usuario_id=self.usuario_actual.id)
            tareas = [t for t in todas_tareas if t.esta_vencida()]
        
        else:
            print("❌ Opción inválida")
            return
        
        if tareas:
            print(f"\n📋 Tareas encontradas: {len(tareas)}\n")
            for tarea in tareas:
                print(f"{tarea.id}. {tarea}")
        else:
            print("📋 No se encontraron tareas con los filtros seleccionados")
    
    def ver_estadisticas(self):
        """Muestra estadísticas de las tareas"""
        print("\n--- ESTADÍSTICAS ---")
        stats = self.db.obtener_estadisticas(usuario_id=self.usuario_actual.id)
        
        if stats:
            print(f"\n📊 Resumen de tareas:")
            print(f"   Total: {stats['total']}")
            print(f"   ⏳ Pendientes: {stats['pendientes']}")
            print(f"   🔄 En progreso: {stats['en_progreso']}")
            print(f"   ✅ Completadas: {stats['completadas']}")
            print(f"   ❌ Canceladas: {stats['canceladas']}")
            
            if stats['total'] > 0:
                porcentaje = (stats['completadas'] / stats['total']) * 100
                print(f"\n   Porcentaje de completadas: {porcentaje:.1f}%")
        else:
            print("📊 No hay estadísticas disponibles")
    
    def cerrar(self):
        """Cierra la aplicación y la conexión a la BD"""
        if self.db:
            self.db.cerrar()


def main():
    """Función principal"""
    app = AplicacionTareas()
    try:
        app.menu_principal()
    except KeyboardInterrupt:
        print("\n\n¡Aplicación interrumpida!")
    finally:
        app.cerrar()


if __name__ == "__main__":
    main()

