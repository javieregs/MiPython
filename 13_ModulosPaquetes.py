"""
EJEMPLO 13: MÓDULOS Y PAQUETES
-------------------------------
Aprende a organizar tu código en módulos y paquetes reutilizables.
"""

# IMPORTAR MÓDULOS ESTÁNDAR
print("=== IMPORTAR MÓDULOS ESTÁNDAR ===")

import math
import random
import datetime
from collections import Counter

# Usar funciones del módulo math
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Sen de 90 grados: {math.sin(math.radians(90))}")

# Usar funciones del módulo random
print(f"\nNúmero aleatorio entre 1 y 10: {random.randint(1, 10)}")
print(f"Número decimal aleatorio: {random.random()}")

lista = [1, 2, 3, 4, 5]
print(f"Elemento aleatorio de la lista: {random.choice(lista)}")

# Usar el módulo datetime
print(f"\nFecha y hora actual: {datetime.datetime.now()}")
print(f"Fecha actual: {datetime.date.today()}")

# Usar Counter
texto = "programación en python"
contador = Counter(texto)
print(f"\nConteo de letras en '{texto}':")
for letra, cantidad in contador.most_common(5):
    print(f"{letra}: {cantidad}")

# CREAR Y USAR MÚDULOS PROPIOS
print("\n=== CREAR MÓDULOS PROPIOS ===")

# Crear un módulo de utilidades
utilidades_contenido = '''
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
'''

# Escribir el módulo
with open("utilidades.py", "w", encoding="utf-8") as f:
    f.write(utilidades_contenido)

# Importar y usar el módulo
import utilidades

print(f"Suma: {utilidades.suma(5, 3)}")
print(f"Resta: {utilidades.resta(5, 3)}")
print(f"Multiplicación: {utilidades.multiplicacion(5, 3)}")
print(f"División: {utilidades.division(10, 2)}")
print(f"¿Es par 8? {utilidades.es_par(8)}")
print(f"Factorial de 5: {utilidades.factorial(5)}")

# IMPORTAR FUNCIONES ESPECÍFICAS
from utilidades import suma, es_par

print(f"\nUsando importación directa:")
print(f"Suma: {suma(10, 20)}")
print(f"¿Es par 7? {es_par(7)}")

# ALIAS EN IMPORTACIONES
import utilidades as util

print(f"\nUsando alias:")
print(f"Factorial de 4: {util.factorial(4)}")

# PAQUETES
print("\n=== CREAR PAQUETES ===")

import os

# Crear estructura de paquete
os.makedirs("mi_paquete", exist_ok=True)

# Crear __init__.py
init_contenido = '''
"""
Paquete de ejemplo para formación
"""

__version__ = "1.0.0"
__author__ = "Estudiante de Python"

from .operaciones import OperacionesMatematicas
from .validacion import ValidarDatos

__all__ = ['OperacionesMatematicas', 'ValidarDatos']
'''

# Crear módulo de operaciones
operaciones_contenido = '''
"""
Módulo de operaciones matemáticas
"""

class OperacionesMatematicas:
    """Clase para realizar operaciones matemáticas"""
    
    @staticmethod
    def potencia(base, exponente):
        """Calcula la potencia"""
        return base ** exponente
    
    @staticmethod
    def raiz_cuadrada(numero):
        """Calcula la raíz cuadrada"""
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return numero ** 0.5
    
    @staticmethod
    def porcentaje(parte, total):
        """Calcula el porcentaje"""
        if total == 0:
            raise ValueError("El total no puede ser cero")
        return (parte / total) * 100
'''

# Crear módulo de validación
validacion_contenido = '''
"""
Módulo de validación de datos
"""

class ValidarDatos:
    """Clase para validar diferentes tipos de datos"""
    
    @staticmethod
    def es_email(email):
        """Valida formato de email básico"""
        return "@" in email and "." in email.split("@")[1]
    
    @staticmethod
    def es_telefono(telefono):
        """Valida formato de teléfono básico"""
        return telefono.isdigit() and len(telefono) >= 10
    
    @staticmethod
    def es_edad_valida(edad):
        """Valida que la edad esté en un rango válido"""
        return isinstance(edad, int) and 0 <= edad <= 120
'''

# Escribir archivos del paquete
with open("mi_paquete/__init__.py", "w", encoding="utf-8") as f:
    f.write(init_contenido)

with open("mi_paquete/operaciones.py", "w", encoding="utf-8") as f:
    f.write(operaciones_contenido)

with open("mi_paquete/validacion.py", "w", encoding="utf-8") as f:
    f.write(validacion_contenido)

# Usar el paquete
from mi_paquete import OperacionesMatematicas, ValidarDatos

print(f"\nUsando el paquete:")
print(f"Potencia 2^8: {OperacionesMatematicas.potencia(2, 8)}")
print(f"Raíz cuadrada de 25: {OperacionesMatematicas.raiz_cuadrada(25)}")
print(f"Porcentaje: {OperacionesMatematicas.porcentaje(25, 100):.0f}%")

print(f"\nValidaciones:")
print(f"¿Es email válido? {ValidarDatos.es_email('test@example.com')}")
print(f"¿Es teléfono válido? {ValidarDatos.es_telefono('1234567890')}")
print(f"¿Es edad válida? {ValidarDatos.es_edad_valida(25)}")

