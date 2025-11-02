"""
EJEMPLO 5: FORMATEO DE TEXTO
-----------------------------
Diferentes formas de formatear y trabajar con cadenas de texto.
"""

# Diferentes formas de formatear texto
nombre = "Carlos"
edad = 30
salario = 3500.50

print("=== MÉTODOS DE FORMATEO ===")

# 1. Concatenación con +
print("1. Hola, " + nombre + " tienes " + str(edad) + " años")

# 2. Método .format()
print("2. Hola, {} tienes {} años".format(nombre, edad))

# 3. f-strings (Python 3.6+) - RECOMENDADO
print(f"3. Hola, {nombre} tienes {edad} años")
print(f"4. Salario: ${salario:,.2f}")  # Formato con comas y 2 decimales

# MÉTODOS DE STRING
texto = "  Python es genial  "

print("\n=== MÉTODOS ÚTILES DE STRING ===")
print(f"Original: '{texto}'")
print(f"Mayúsculas: '{texto.upper()}'")
print(f"Minúsculas: '{texto.lower()}'")
print(f"Sin espacios: '{texto.strip()}'")
print(f"Capitalizar: '{texto.strip().capitalize()}'")
print(f"Título: '{texto.strip().title()}'")
print(f"Longitud: {len(texto)}")

# Operaciones con strings
frase = "Python es un lenguaje de programación"

print("\n=== OPERACIONES CON STRINGS ===")
print(f"Frase: '{frase}'")
print(f"¿Contiene 'Python'? {frase.__contains__('Python')}")  # O simplemente: 'Python' in frase
print(f"Reemplazar: {frase.replace('Python', 'JavaScript')}")
print(f"Dividir en palabras: {frase.split()}")
print(f"Unir palabras: {'-'.join(['Python', 'es', 'genial'])}")

