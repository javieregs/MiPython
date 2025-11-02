"""
EJEMPLO 4: ENTRADA Y SALIDAS 
----------------------------
Aprende a recibir datos del usuario y mostrar información...
"""

# SALIDA DE DATOS (ya visto anteriormente)
print("=== SALIDA DE DATOS ===")
nombre = "María"
edad = 20

# Diferentes formas de imprimir
print("Hola, me llamo", nombre, "y tengo", edad, "años")
print("Hola, me llamo " + nombre + " y tengo " + str(edad) + " años")
print(f"Hola, me llamo {nombre} y tengo {edad} años")  # f-string (recomendado)

# ENTRADA DE DATOS
print("\n=== ENTRADA DE DATOS ===")

# Solicitar datos al usuario
nombre_usuario = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {nombre_usuario}!")

# Solicitar números (importante: convertir a int o float)
edad_usuario = input("¿Cuántos años tienes? ")
edad_usuario = int(edad_usuario)  # Convertir string a entero

print(f"Tienes {edad_usuario} años")
print(f"En 10 años tendrás {edad_usuario + 10} años")

# Ejemplo completo: Calculadora simple
print("\n=== CALCULADORA SIMPLE ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

