"""
EJEMPLO 6: ESTRUCTURAS DE CONTROL
----------------------------------
Aprende a usar if/else y bucles (for, while) para controlar el flujo del programa.
"""

# ESTRUCTURAS CONDICIONALES (if/elif/else)
print("=== ESTRUCTURAS CONDICIONALES ===")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Múltiples condiciones
nota = 85

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Operadores lógicos en condiciones
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# BUCLE FOR (iterar sobre elementos)
print("\n=== BUCLE FOR ===")

# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja"]
print("Frutas disponibles:")
for fruta in frutas:
    print(f"- {fruta}")

# Iterar con range
print("\nNúmeros del 1 al 5:")
for i in range(1, 6):
    print(i)

# Bucle for con índices
print("\nFrutas con índice:")
for indice, fruta in enumerate(frutas):
    print(f"{indice + 1}. {fruta}")

# BUCLE WHILE (mientras se cumpla una condición)
print("\n=== BUCLE WHILE ===")

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Bucle while con validación
print("\nIngresa un número positivo:")
while True:
    numero = int(input("Número: "))
    if numero > 0:
        print(f"¡Correcto! Ingresaste {numero}")
        break
    else:
        print("Por favor, ingresa un número positivo")

# BUCLES ANIDADOS
print("\n=== BUCLES ANIDADOS ===")
print("Tabla de multiplicar del 5:")
for i in range(1, 6):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")

