"""
EJEMPLO 10: PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
---------------------------------------------------
Aprende a crear clases y objetos para organizar mejor tu código.
"""

# CLASE SIMPLE
class Perro:
    """Clase que representa un perro"""
    
    def __init__(self, nombre, raza):
        """Constructor - se ejecuta al crear un objeto"""
        self.nombre = nombre
        self.raza = raza
        self.edad = 0
    
    def ladrar(self):
        """Método que hace ladrar al perro"""
        return f"{self.nombre} dice: ¡Guau, guau!"
    
    def cumplir_anios(self):
        """Método que aumenta la edad del perro"""
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años"
    
    def info(self):
        """Método que muestra información del perro"""
        return f"{self.nombre} es un {self.raza} de {self.edad} años"

# Crear objetos (instancias)
print("=== CLASE Y OBJETOS ===")
perro1 = Perro("Max", "Labrador")
perro2 = Perro("Luna", "Pastor Alemán")

print(perro1.ladrar())
print(perro2.info())

perro1.cumplir_anios()
print(perro1.info())

# CLASE CON ATRIBUTOS DE CLASE
class Estudiante:
    """Clase que representa un estudiante"""
    
    # Atributo de clase (compartido por todas las instancias)
    total_estudiantes = 0
    
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []
        Estudiante.total_estudiantes += 1
    
    def agregar_nota(self, nota):
        """Agrega una nota al estudiante"""
        if 0 <= nota <= 100:
            self.notas.append(nota)
            return f"Nota {nota} agregada"
        return "Nota inválida (debe estar entre 0 y 100)"
    
    def calcular_promedio(self):
        """Calcula el promedio de notas"""
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def info(self):
        """Muestra información del estudiante"""
        promedio = self.calcular_promedio()
        return (f"{self.nombre}, {self.edad} años, {self.carrera}. "
                f"Promedio: {promedio:.2f}")
    
    @classmethod
    def obtener_total(cls):
        """Método de clase"""
        return cls.total_estudiantes

print("\n=== CLASE CON ATRIBUTOS DE CLASE ===")
est1 = Estudiante("Ana", 20, "Informática")
est2 = Estudiante("Carlos", 22, "Ingeniería")

est1.agregar_nota(85)
est1.agregar_nota(90)
est1.agregar_nota(88)

est2.agregar_nota(75)
est2.agregar_nota(80)

print(est1.info())
print(est2.info())
print(f"Total de estudiantes: {Estudiante.obtener_total()}")

# HERENCIA
class Animal:
    """Clase base para animales"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        """Método que puede ser sobrescrito"""
        return f"{self.nombre} hace un sonido"

class Gato(Animal):
    """Clase que hereda de Animal"""
    
    def hacer_sonido(self):
        """Sobrescribe el método de la clase base"""
        return f"{self.nombre} dice: ¡Miau!"

class Vaca(Animal):
    """Otra clase que hereda de Animal"""
    
    def hacer_sonido(self):
        """Sobrescribe el método de la clase base"""
        return f"{self.nombre} dice: ¡Muuu!"

print("\n=== HERENCIA ===")
gato = Gato("Whiskers")
vaca = Vaca("Bessie")

print(gato.hacer_sonido())
print(vaca.hacer_sonido())

# ENCAPSULACIÓN (atributos privados)
class CuentaBancaria:
    """Clase que representa una cuenta bancaria"""
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (__saldo)
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta"""
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito de ${cantidad} realizado. Saldo: ${self.__saldo}"
        return "Cantidad inválida"
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta"""
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro de ${cantidad} realizado. Saldo: ${self.__saldo}"
        return "Fondos insuficientes o cantidad inválida"
    
    def consultar_saldo(self):
        """Consulta el saldo de la cuenta"""
        return f"Saldo actual: ${self.__saldo}"

print("\n=== ENCAPSULACIÓN ===")
cuenta = CuentaBancaria("Juan Pérez", 1000)
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.consultar_saldo())

