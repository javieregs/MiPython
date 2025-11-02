
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
