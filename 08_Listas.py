"""
EJEMPLO 8: LISTAS
-----------------
Las listas son colecciones ordenadas y mutables de elementos.
"""

# CREAR LISTAS
print("=== CREAR Y ACCEDER A LISTAS ===")

# Lista de números
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Lista de strings
frutas = ["manzana", "banana", "naranja"]
print(f"Lista de frutas: {frutas}")

# Lista mixta
mixta = [1, "texto", 3.14, True]
print(f"Lista mixta: {mixta}")

# Acceder a elementos
print(f"\nPrimer elemento: {frutas[0]}")
print(f"Último elemento: {frutas[-1]}")
print(f"Segundo elemento: {frutas[1]}")

# OPERACIONES CON LISTAS
print("\n=== OPERACIONES CON LISTAS ===")

# Agregar elementos
frutas.append("uva")
print(f"Después de append('uva'): {frutas}")

# Insertar en posición específica
frutas.insert(1, "mango")
print(f"Después de insert(1, 'mango'): {frutas}")

# Eliminar elementos
frutas.remove("banana")
print(f"Después de remove('banana'): {frutas}")

# Eliminar por índice
elemento_eliminado = frutas.pop(0)
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Lista después de pop(0): {frutas}")

# MÉTODOS ÚTILES
print("\n=== MÉTODOS ÚTILES ===")

numeros = [3, 1, 4, 1, 5, 9, 2]
print(f"Lista original: {numeros}")

# Longitud
print(f"Longitud: {len(numeros)}")

# Ordenar
numeros.sort()
print(f"Ordenada: {numeros}")

# Invertir
numeros.reverse()
print(f"Invertida: {numeros}")

# Contar ocurrencias
print(f"Cantidad de 1: {numeros.count(1)}")

# Buscar índice
print(f"Índice del 5: {numeros.index(5)}")

# REBANADAS (Slicing)
print("\n=== REBANADAS ===")

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista completa: {lista}")
print(f"Primeros 3: {lista[:3]}")
print(f"Últimos 3: {lista[-3:]}")
print(f"Del índice 2 al 5: {lista[2:6]}")
print(f"Cada segundo elemento: {lista[::2]}")

# COMPRENSIÓN DE LISTAS (List Comprehension)
print("\n=== COMPRENSIÓN DE LISTAS ===")

# Crear lista de cuadrados
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# Crear lista con condición
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares: {pares}")

# ITERAR SOBRE LISTAS
print("\n=== ITERAR SOBRE LISTAS ===")

colores = ["rojo", "verde", "azul"]

print("Iteración simple:")
for color in colores:
    print(f"- {color}")

print("\nIteración con índice:")
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")

