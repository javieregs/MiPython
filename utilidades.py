
"""
Módulo de utilidades matemáticas
"""

def suma(a, b):
    """Suma dos números"""
    return a + b

def resta(a, b):
    """Resta dos números"""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos números"""
    return a * b

def division(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
