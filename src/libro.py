# Integrantes del Grupo#1 : Joselyne Paulette Játiva Vera
#                           Joselin Mariuxi Rodriguez Saldaña
#                           Jemina Victoria Suárez Veintimilla
#                           Rosa Angelica Bustamante Moreira

from src.producto import Producto

class Libro(Producto):
    """
    Esta clase representa un libro. Hereda de Producto y le agregamos detalles propios,
    como el autor, la edición y el ISBN
    """
    def __init__(self, codigo, nombre, precio, cantidad, autor, edicion, isbn):
        """
        Constructor de la clase Libro.

        Args:
            codigo (str): Código único del libro.
            nombre (str): Nombre del libro.
            precio (float): Precio unitario del libro.
            cantidad (int): Cantidad disponible en inventario.
            autor (str): Autor del libro.
            edicion (str): Edición del libro.
            isbn (str): ISBN del libro.
        """
        super().__init__(codigo, nombre, precio, cantidad)
        self._autor = autor
        self._edicion = edicion
        self._isbn = isbn

    # Getters y setters como propiedades
    @property
    def autor(self):
        """Getter para el autor del libro."""
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        """Setter para el autor del libro."""
        self._autor = nuevo_autor

    @property
    def edicion(self):
        """Getter para la edición del libro."""
        return self._edicion

    @edicion.setter
    def edicion(self, nueva_edicion):
        """Setter para la edición del libro."""
        self._edicion = nueva_edicion

    @property
    def isbn(self):
        """Getter para el ISBN del libro."""
        return self._isbn

    @isbn.setter
    def isbn(self, nuevo_isbn):
        """Setter para el ISBN del libro."""
        self._isbn = nuevo_isbn

    def aplicar_descuento(self):
        """
         Si el libro es una 'edición de bolsillo', le aplico un 10% de descuento.
        """
        if "bolsillo" in self._edicion.lower():
            return self._precio * 0.9
        return self._precio

if __name__ == "__main__":
    print("\n---LIBRO ---")
    libro1 = Libro("L001", "Cien años de soledad", 25.00, 10, "Gabriel García Márquez", "Pasta blanda",
                   "978-3-16-148410-0")
    libro2 = Libro("L002", "El Señor de los Anillos", 35.00, 5, "J.R.R. Tolkien", "Edición de bolsillo",
                   "978-0-618-05326-7")

    print(f"Nombre original del libro1: {libro1.nombre}")
    libro1.nombre = "Cien años de soledad (Edición Aniversario)"
    print(f"Nuevo nombre del libro1: {libro1.nombre}")

    print(f"Precio original del libro2: {libro2.precio}")
    libro2.precio = 30.00
    print(f"Nuevo precio del libro2: {libro2.precio}")

    print("\nAplicando descuento y cálculo de total para libro1:")
    print(f"Precio con descuento: ${libro1.aplicar_descuento():.2f}")
    print(f"Total por 2 unidades: ${libro1.calcular_total(2):.2f}")
