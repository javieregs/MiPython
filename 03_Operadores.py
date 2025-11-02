"""
EJEMPLO 3: OPERADORES
---------------------
Los operadores permiten realizar operaciones con variables y valores.
"""

# OPERADORES ARITMÉTICOS
a = 10
b = 3

print("=== OPERADORES ARITMÉTICOS ===")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo (resto): {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

# OPERADORES DE COMPARACIÓN
print("\n=== OPERADORES DE COMPARACIÓN ===")
x = 5
y = 8

print(f"{x} == {y}: {x == y}")  # Igual
print(f"{x} != {y}: {x != y}")  # Diferente
print(f"{x} < {y}: {x < y}")    # Menor que
print(f"{x} > {y}: {x > y}")    # Mayor que
print(f"{x} <= {y}: {x <= y}")  # Menor o igual
print(f"{x} >= {y}: {x >= y}")  # Mayor o igual

# OPERADORES LÓGICOS
print("\n=== OPERADORES LÓGICOS ===")
p = True
q = False

print(f"p and q: {p and q}")  # Y (ambos deben ser True)
print(f"p or q: {p or q}")    # O (al menos uno True)
print(f"not p: {not p}")      # NO (invierte el valor)

# OPERADORES DE ASIGNACIÓN
print("\n=== OPERADORES DE ASIGNACIÓN ===")
numero = 10
print(f"Valor inicial: {numero}")

numero += 5  # Equivale a: numero = numero + 5
print(f"Después de += 5: {numero}")

numero -= 3  # Equivale a: numero = numero - 3
print(f"Después de -= 3: {numero}")

numero *= 2  # Equivale a: numero = numero * 2
print(f"Después de *= 2: {numero}")

