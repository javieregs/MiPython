"""
EJEMPLO 9: DICCIONARIOS
------------------------
Los diccionarios almacenan pares clave-valor. Son muy útiles para datos estructurados.
"""

# CREAR DICCIONARIOS
print("=== CREAR Y ACCEDER A DICCIONARIOS ===")

# Diccionario de información personal
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}

print(f"Diccionario: {persona}")

# Acceder a valores
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")

# OPERACIONES CON DICCIONARIOS
print("\n=== OPERACIONES CON DICCIONARIOS ===")

# Agregar/modificar elementos
persona["email"] = "ana@example.com"
persona["edad"] = 26
print(f"Después de agregar email y actualizar edad: {persona}")

# Eliminar elementos
del persona["ciudad"]
print(f"Después de eliminar 'ciudad': {persona}")

# Verificar si existe una clave
if "nombre" in persona:
    print(f"Nombre encontrado: {persona['nombre']}")

# MÉTODOS ÚTILES
print("\n=== MÉTODOS ÚTILES ===")

estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "carrera": "Informática",
    "notas": [85, 90, 88]
}

print(f"Diccionario: {estudiante}")

# Obtener todas las claves
print(f"Claves: {estudiante.keys()}")

# Obtener todos los valores
print(f"Valores: {estudiante.values()}")

# Obtener pares clave-valor
print(f"Items: {estudiante.items()}")

# Iterar sobre diccionarios
print("\n=== ITERAR SOBRE DICCIONARIOS ===")

print("Iteración por claves:")
for clave in estudiante:
    print(f"{clave}: {estudiante[clave]}")

print("\nIteración por items:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# DICCIONARIOS ANIDADOS
print("\n=== DICCIONARIOS ANIDADOS ===")

empresa = {
    "nombre": "Tech Corp",
    "empleados": {
        "101": {
            "nombre": "Juan",
            "departamento": "Desarrollo",
            "salario": 50000
        },
        "102": {
            "nombre": "María",
            "departamento": "Marketing",
            "salario": 45000
        }
    }
}

print(f"Empresa: {empresa['nombre']}")
print(f"Empleado 101: {empresa['empleados']['101']}")
print(f"Salario de Juan: ${empresa['empleados']['101']['salario']}")

# COMPRENSIÓN DE DICCIONARIOS
print("\n=== COMPRENSIÓN DE DICCIONARIOS ===")

# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Diccionario con condición
pares = {x: x*2 for x in range(1, 6) if x % 2 == 0}
print(f"Números pares: {pares}")

# EJEMPLO PRÁCTICO: Gestión de inventario
print("\n=== EJEMPLO PRÁCTICO: INVENTARIO ===")

inventario = {
    "laptop": {"cantidad": 10, "precio": 800},
    "mouse": {"cantidad": 25, "precio": 15},
    "teclado": {"cantidad": 20, "precio": 50}
}

print("Inventario actual:")
for producto, info in inventario.items():
    print(f"{producto.capitalize()}: {info['cantidad']} unidades - ${info['precio']} c/u")

