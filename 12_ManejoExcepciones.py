"""
EJEMPLO 12: MANEJO DE EXCEPCIONES
-----------------------------------
Aprende a manejar errores de forma elegante para que tu programa sea más robusto.
"""

# EXCEPCIÓN BÁSICA
print("=== MANEJO BÁSICO DE EXCEPCIONES ===")

try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"10 dividido por {numero} = {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")

# TRY/EXCEPT/ELSE/FINALLY
print("\n=== TRY/EXCEPT/ELSE/FINALLY ===")

def dividir(a, b):
    """Divide dos números con manejo de excepciones"""
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: División por cero no permitida")
        return None
    except TypeError:
        print("Error: Debes ingresar números válidos")
        return None
    else:
        print("División realizada correctamente")
        return resultado
    finally:
        print("Esta línea siempre se ejecuta")

# Probar la función
print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "texto"))

# MANEJO DE MÚLTIPLES EXCEPCIONES
print("\n=== MÚLTIPLES EXCEPCIONES ===")

def procesar_archivo(nombre_archivo):
    """Intenta leer y procesar un archivo"""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            resultado = 100 / numero
            return resultado
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
    except ValueError:
        print(f"Error: El contenido del archivo no es un número válido")
    except ZeroDivisionError:
        print("Error: El archivo contiene el número 0")
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")
    return None

# Crear archivo de prueba
with open("numero.txt", "w") as f:
    f.write("5")

resultado = procesar_archivo("numero.txt")
print(f"Resultado: {resultado}")

# LEVANTAR EXCEPCIONES PERSONALIZADAS
print("\n=== EXCEPCIONES PERSONALIZADAS ===")

class EdadInvalidaError(Exception):
    """Excepción personalizada para edad inválida"""
    pass

class SalarioNegativoError(Exception):
    """Excepción personalizada para salario negativo"""
    pass

def validar_empleado(nombre, edad, salario):
    """Valida los datos de un empleado"""
    if not nombre or len(nombre) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres")
    
    if edad < 18 or edad > 65:
        raise EdadInvalidaError(f"La edad {edad} no es válida (debe estar entre 18 y 65)")
    
    if salario < 0:
        raise SalarioNegativoError("El salario no puede ser negativo")
    
    return f"Empleado {nombre} válido: {edad} años, ${salario}"

# Probar validaciones
try:
    print(validar_empleado("Ana", 25, 50000))
    print(validar_empleado("Jo", 15, 30000))  # Edad inválida
except EdadInvalidaError as e:
    print(f"Error de edad: {e}")
except SalarioNegativoError as e:
    print(f"Error de salario: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")

# ASSERT (afirmaciones)
print("\n=== ASSERT (AFIRMACIONES) ===")

def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas"""
    assert len(notas) > 0, "La lista de notas no puede estar vacía"
    assert all(0 <= nota <= 100 for nota in notas), "Las notas deben estar entre 0 y 100"
    
    return sum(notas) / len(notas)

try:
    promedio1 = calcular_promedio([85, 90, 88])
    print(f"Promedio 1: {promedio1:.2f}")
    
    promedio2 = calcular_promedio([])  # Esto lanzará un AssertionError
except AssertionError as e:
    print(f"Error de aserción: {e}")

# CONTEXTO Y LIMPIEZA
print("\n=== CONTEXTO Y LIMPIEZA ===")

class GestorRecurso:
    """Clase de ejemplo para manejo de recursos"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Recurso '{self.nombre}' inicializado")
    
    def __enter__(self):
        return self
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        print(f"Recurso '{self.nombre}' liberado")
        if tipo_excepcion:
            print(f"Se produjo una excepción: {tipo_excepcion.__name__}")
        return False  # No suprime la excepción
    
    def usar(self):
        print(f"Usando recurso '{self.nombre}'")

# Usar el gestor de contexto
with GestorRecurso("MiRecurso") as recurso:
    recurso.usar()
    # raise ValueError("Error de prueba")  # Descomenta para probar excepciones

