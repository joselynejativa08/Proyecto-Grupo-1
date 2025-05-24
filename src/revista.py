# Integrantes del Grupo#1 : Joselyne Paulette Játiva Vera
#                           Joselin Mariuxi Rodriguez Saldaña
#                           Jemina Victoria Suárez Veintimilla
#                           Rosa Angelica Bustamante Moreira

from src.producto import Producto

class Revista(Producto):
    """
    Esta clase representa una revista. Le agregamos atributos propios como la editorial,
    el número de edición y la periodicidad.
    """
    def __init__(self, codigo, nombre, precio, cantidad, editorial, numero, periodicidad):
        """
        Constructor de la clase Revista.

        Args:
            codigo (str): Código único de la revista.
            nombre (str): Nombre de la revista.
            precio (float): Precio unitario de la revista.
            cantidad (int): Cantidad disponible en inventario.
            editorial (str): Editorial de la revista.
            numero (int): Número de la revista.
            periodicidad (str): Periodicidad de la revista.
        """
        super().__init__(codigo, nombre, precio, cantidad)
        self._editorial = editorial
        self._numero = numero
        self._periodicidad = periodicidad

    # Getters y setters como propiedades
    @property
    def editorial(self):
        """Getter para la editorial de la revista."""
        return self._editorial

    @editorial.setter
    def editorial(self, nueva_editorial):
        """Setter para la editorial de la revista."""
        self._editorial = nueva_editorial

    @property
    def numero(self):
        """Getter para el número de la revista."""
        return self._numero

    @numero.setter
    def numero(self, nuevo_numero):
        """Setter para el número de la revista."""
        self._numero = nuevo_numero

    @property
    def periodicidad(self):
        """Getter para la periodicidad de la revista."""
        return self._periodicidad

    @periodicidad.setter
    def periodicidad(self, nueva_periodicidad):
        """Setter para la periodicidad de la revista."""
        self._periodicidad = nueva_periodicidad

    def aplicar_descuento(self):
        """
        Si la revista es mensual, se le aplica un 5% de descuento.
        """
        if self._periodicidad.lower() == "mensual":
            return self._precio * 0.95
        return self._precio