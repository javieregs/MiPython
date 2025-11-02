"""
EJEMPLO 7: FUNCIONES
--------------------
Las funciones permiten organizar el código en bloques reutilizables.
"""

# FUNCIÓN SIMPLE
def saludar():
    """Función que imprime un saludo"""
    print("¡Hola! Bienvenido")

# Llamar a la función
saludar()

# FUNCIÓN CON PARÁMETROS
def saludar_persona(nombre):
    """Función que saluda a una persona específica"""
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Pedro")

# FUNCIÓN CON RETORNO
def sumar(a, b):
    """Suma dos números y devuelve el resultado"""
    resultado = a + b
    return resultado

suma = sumar(5, 3)
print(f"La suma de 5 + 3 = {suma}")

# FUNCIÓN CON MÚLTIPLES PARÁMETROS
def calcular_promedio(num1, num2, num3):
    """Calcula el promedio de tres números"""
    promedio = (num1 + num2 + num3) / 3
    return promedio

promedio = calcular_promedio(85, 90, 88)
print(f"El promedio es: {promedio:.2f}")

# FUNCIÓN CON PARÁMETROS POR DEFECTO
def saludar_con_titulo(nombre, titulo="Sr."):
    """Saluda con un título opcional"""
    print(f"¡Hola, {titulo} {nombre}!")

saludar_con_titulo("García")
saludar_con_titulo("López", "Dra.")

# FUNCIÓN QUE RETORNA MÚLTIPLES VALORES
def calcular_operaciones(a, b):
    """Calcula suma, resta, multiplicación y división"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

suma, resta, mult, div = calcular_operaciones(10, 2)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

# FUNCIÓN CON DOCUMENTACIÓN
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Parámetros:
    base (float): La base del rectángulo
    altura (float): La altura del rectángulo
    
    Retorna:
    float: El área del rectángulo
    """
    area = base * altura
    return area

area = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {area}")

