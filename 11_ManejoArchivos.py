"""
EJEMPLO 11: MANEJO DE ARCHIVOS
------------------------------
Aprende a leer y escribir archivos en Python.
"""

import os

# ESCRIBIR EN UN ARCHIVO
print("=== ESCRIBIR EN UN ARCHIVO ===")

# Modo 'w' (write) - sobrescribe el archivo
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, este es un archivo de ejemplo.\n")
    archivo.write("Esta es la segunda línea.\n")
    archivo.write("Y esta es la tercera línea.\n")

print("Archivo 'ejemplo.txt' creado correctamente")

# Modo 'a' (append) - agrega al final del archivo
with open("ejemplo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Esta línea se agregó después.\n")

# LEER DE UN ARCHIVO
print("\n=== LEER DE UN ARCHIVO ===")

# Leer todo el contenido
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("Contenido completo:")
    print(contenido)

# Leer línea por línea
print("\nLeer línea por línea:")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(f"Línea: {linea.strip()}")

# Leer todas las líneas como lista
print("\nLeer todas las líneas como lista:")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for i, linea in enumerate(lineas, 1):
        print(f"Línea {i}: {linea.strip()}")

# TRABAJAR CON ARCHIVOS JSON
print("\n=== TRABAJAR CON ARCHIVOS JSON ===")
import json

# Crear un diccionario
datos = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["lectura", "programación", "música"],
    "activo": True
}

# Escribir JSON
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print("Archivo JSON 'datos.json' creado")

# Leer JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos_leidos = json.load(archivo)
    print("\nDatos leídos del JSON:")
    print(json.dumps(datos_leidos, indent=2, ensure_ascii=False))

# TRABAJAR CON ARCHIVOS CSV
print("\n=== TRABAJAR CON ARCHIVOS CSV ===")
import csv

# Escribir CSV
datos_estudiantes = [
    ["Nombre", "Edad", "Carrera", "Nota"],
    ["Ana", 20, "Informática", 85],
    ["Carlos", 22, "Ingeniería", 90],
    ["María", 21, "Medicina", 88]
]

with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos_estudiantes)

print("Archivo CSV 'estudiantes.csv' creado")

# Leer CSV
print("\nDatos del CSV:")
with open("estudiantes.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

# OPERACIONES CON ARCHIVOS
print("\n=== OPERACIONES CON ARCHIVOS ===")

# Verificar si un archivo existe
if os.path.exists("ejemplo.txt"):
    print("El archivo 'ejemplo.txt' existe")
    
    # Obtener información del archivo
    tamaño = os.path.getsize("ejemplo.txt")
    print(f"Tamaño del archivo: {tamaño} bytes")

# Listar archivos en el directorio actual
print("\nArchivos .txt en el directorio:")
for archivo in os.listdir("."):
    if archivo.endswith(".txt"):
        print(f"- {archivo}")

