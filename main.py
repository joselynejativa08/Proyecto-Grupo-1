# Integrantes del Grupo#1 : Joselyne Paulette Játiva Vera
#                           Joselin Mariuxi Rodriguez Saldaña
#                           Jemina Victoria Suárez Veintimilla
#                           Rosa Angelica Bustamante Moreira

from src.libro import Libro
from src.revista import Revista
from src.material_escolar import MaterialEscolar


def main():
    """
     Este es el punto de entrada del programa. Aquí creomos varios productos
    (libros, revistas y materiales escolares), les cambiamos algunos atributos
    usando setters, aplicando descuentos, y calculo totales.
    """
    print("--- Sistema de Gestión de Inventario para Librería ---")
    print("\nCreando productos de ejemplo:")

    # Crear instancias de las subclases
    libro1 = Libro("L001", "Cien años de soledad", 25.00, 10, "Gabriel García Márquez", "Pasta blanda",
                   "978-3-16-148410-0")
    libro2 = Libro("L002", "El Señor de los Anillos", 35.00, 5, "J.R.R. Tolkien", "Edición de bolsillo",
                   "978-0-618-05326-7")

    revista1 = Revista("R001", "National Geographic", 8.50, 20, "National Geographic Society", 250, "Mensual")
    revista2 = Revista("R002", "Hola!", 5.00, 15, "Publicaciones de Revistas", 1234, "Semanal")

    material1 = MaterialEscolar("M001", "Cuaderno A4", 3.00, 50, "Cuaderno", "Norma")
    material2 = MaterialEscolar("M002", "Lápices de Colores", 12.00, 30, "Lápices", "Genérico")

    # --- Demostración de Encapsulamiento (Getters y Setters) ---
    print("\n--- Demostración de Encapsulamiento ---")
    print(f"Nombre original del libro1: {libro1.nombre}")
    libro1.nombre = "Cien años de soledad (Edición Aniversario)"
    print(f"Nuevo nombre del libro1: {libro1.nombre}")
    print(f"Precio original del libro2: {libro2.precio}")
    libro2.precio = 30.00  # Usando el setter para cambiar el precio
    print(f"Nuevo precio del libro2: {libro2.precio}")

    # Intentando asignar un valor inválido (mostrará el mensaje de error del setter)
    print("\nIntentando asignar precio negativo a revista1:")
    revista1.precio = -10.00
    print(f"Precio de revista1 después del intento: {revista1.precio}")

    # --- Demostración de Polimorfismo y Cálculo de Totales ---
    print("\n--- Demostración de Polimorfismo y Cálculo de Totales ---")

    # Lista de productos para iterar y mostrar el polimorfismo
    productos = [libro1, libro2, revista1, revista2, material1, material2]

    for producto in productos:
        print(f"\n--- Detalles de {producto.nombre} (Código: {producto.codigo}) ---")
        print(f"Precio original: ${producto.precio:.2f}")

        # Aplicar descuento polimórficamente
        precio_con_descuento = producto.aplicar_descuento()
        print(f"Precio con descuento: ${precio_con_descuento:.2f}")

        # Calcular total a comprar polimórficamente
        cantidad_a_comprar = 2
        total_a_pagar = producto.calcular_total(cantidad_a_comprar)
        if total_a_pagar > 0:
            print(f"Total a pagar por {cantidad_a_comprar} unidades: ${total_a_pagar:.2f}")
        else:
            print(f"No se pudo calcular el total para {producto.nombre}.")

        # Demostrar la gestión de cantidad
        if isinstance(producto, Libro):  # Ejemplo de atributo específico
            print(f"Autor: {producto.autor}, Edición: {producto.edicion}")
        elif isinstance(producto, Revista):
            print(f"Editorial: {producto.editorial}, Número: {producto.numero}")
        elif isinstance(producto, MaterialEscolar):
            print(f"Tipo: {producto.tipo}, Marca: {producto.marca}")

        print(f"Cantidad disponible: {producto.cantidad}")
        producto.cantidad -= cantidad_a_comprar  # Actualizar cantidad después de la "compra"
        print(f"Cantidad restante: {producto.cantidad}")


if __name__ == "__main__":
  main()