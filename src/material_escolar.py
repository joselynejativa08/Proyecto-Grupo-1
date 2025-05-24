# Integrantes del Grupo#1 : Joselyne Paulette Játiva Vera
#                           Joselin Mariuxi Rodriguez Saldaña
#                           Jemina Victoria Suárez Veintimilla
#                           Rosa Angelica Bustamante Moreira

from src.producto import Producto

class MaterialEscolar(Producto):
    """
    En esta clase representamos los productos de papelería o útiles escolares,
    y le agregamos cosas como el tipo y la marca.
    """
    def __init__(self, codigo, nombre, precio, cantidad, tipo, marca):
        """
        Constructor de la clase MaterialEscolar.

        Args:
            codigo (str): Código único del material escolar.
            nombre (str): Nombre del material escolar.
            precio (float): Precio unitario del material escolar.
            cantidad (int): Cantidad disponible en inventario.
            tipo (str): Tipo de material escolar (ej: cuaderno, lápiz).
            marca (str): Marca del material escolar.
        """
        super().__init__(codigo, nombre, precio, cantidad)
        self._tipo = tipo
        self._marca = marca

    # Getters y setters como propiedades
    @property
    def tipo(self):
        """Getter para el tipo de material escolar."""
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        """Setter para el tipo de material escolar."""
        self._tipo = nuevo_tipo

    @property
    def marca(self):
        """Getter para la marca del material escolar."""
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        """Setter para la marca del material escolar."""
        self._marca = nueva_marca

    def aplicar_descuento(self):
        """
        Aplica un descuento del 15% si la marca es "Genérico".
        """
        if self._marca.lower() == "genérico":
            return self._precio * 0.85
        return self._precio

if __name__ == "__main__":
    print("\n--- MATERIAL ESCOLAR ---")
    material1 = MaterialEscolar("M001", "Cuaderno A4", 3.00, 50, "Cuaderno", "Norma")
    material2 = MaterialEscolar("M002", "Lápices de Colores", 12.00, 30, "Lápices", "Genérico")

    print(f"Material: {material1.nombre}, Precio original: ${material1.precio}")
    print(f"Precio con descuento: ${material1.aplicar_descuento():.2f}")
    print(f"Total por 2 unidades: ${material1.calcular_total(2):.2f}")
