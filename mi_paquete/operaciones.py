
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
