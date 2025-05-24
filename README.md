Sistema de Gestión de Inventario para Librería.

Integrantes Gupo#1 : Joselyne Paulette Játiva Vera
                     Joselin Mariuxi Rodriguez Saldaña
                     Jemina Victoria Suárez Veintimilla
                     Rosa Angelica Bustamante Moreira

Descripción del proyecto:

Nuestro proyecto es un sistema básico para gestionar el inventario de una librería. Está implementado en Python utilizando programación orientada a objetos. Se definen clases que representan productos generales y tres tipos específicos de productos: libros, revistas y materiales escolares.
Cada tipo de producto tiene atributos específicos y puede aplicar descuentos particulares mediante polimorfismo. El sistema permite crear productos, modificar sus atributos, aplicar descuentos y calcular el total a pagar por una cantidad determinada de productos, verificando el stock disponible.

Clase Producto
Descripción:
La clase Producto es la clase base o padre de todas las demás. Define los atributos comunes a todos los productos que se venden en la librería: código, nombre, precio y cantidad disponible. También contiene métodos para modificar y obtener esos atributos de forma controlada, y un método para calcular el total de una compra.

Atributos principales:

codigo: identificador único del producto.

nombre: nombre del producto.

precio: precio unitario.

cantidad: unidades disponibles en inventario.

Métodos utilizados:

aplicar_descuento(): devuelve el precio sin descuento. Este método es sobrescrito por las clases hijas.

calcular_total(cantidad): valida si hay suficiente stock y, si es así, aplica el descuento y calcula el total.

![image](https://github.com/user-attachments/assets/c5919686-32cd-4d0c-b4d7-c8c5f308e2fd)

Clase Libro
La clase Libro hereda de Producto y se especializa en representar libros. Se añaden atributos específicos como el autor, la edición y el ISBN. Si el libro es una “edición de bolsillo”, se aplica un 10% de descuento.

Atributos:
autor: nombre del autor del libro.

edicion: tipo de edición (por ejemplo, edición de bolsillo, pasta dura).

isbn: número ISBN que identifica el libro.

Métodos:
aplicar_descuento(): si la edición contiene la palabra “bolsillo”, aplica un 10% de descuento.

Getters y setters para acceder y modificar los atributos.

Ejemplo:
Se muestran dos libros. A uno se le cambia el nombre y al otro se le aplica descuento por ser edición de bolsillo. Luego se calcula el total por 2 unidades.

![image](https://github.com/user-attachments/assets/e912e7c4-778c-4f9c-9114-2dfeaa9cb437) 

Clase Revista
La clase Revista hereda de Producto y representa revistas en el sistema. Tiene atributos específicos como la editorial, el número de edición y la periodicidad (mensual, semanal, etc.). Si la revista es mensual, se le aplica automáticamente un 5% de descuento en el precio.

Atributos:
editorial: nombre de la editorial.

numero: número o edición de la revista.

periodicidad: frecuencia de publicación.

Métodos:
aplicar_descuento(): si la revista es mensual, aplica 5% de descuento.

Getters y setters para modificar y acceder a sus atributos.

Ejemplo:
Se crean revistas, se intenta cambiar el precio a uno inválido (y el sistema lo evita), se aplica descuento y se calcula el total para 2 unidades.

![image](https://github.com/user-attachments/assets/7ca22d58-a83a-4f51-ba13-202473614844)

Clase MaterialEscolar
La clase MaterialEscolar también hereda de Producto. Representa artículos como cuadernos, lápices, reglas, etc. Se le agregan dos atributos: el tipo de material y la marca. Si la marca es "Genérico", se aplica un 15% de descuento al precio.

Atributos:
tipo: describe qué tipo de producto es (cuaderno, lápiz, etc.).

marca: marca del producto (Norma, Genérico, etc.).

Métodos:
aplicar_descuento(): si la marca es "Genérico", aplica un 15% de descuento.

Getters y setters para acceder o modificar los atributos.

Ejemplo:
Se muestran dos materiales escolares. Uno con marca Genérico recibe descuento. Se calcula el total a pagar por 2 unidades.

![image](https://github.com/user-attachments/assets/cc9e96b4-4f47-4984-9f72-68590cbfd750)

En nuestro archivo:

Creamos tres tipos de productos: Libros, Revistas y Material Escolar.

Cada producto tiene su propio precio, cantidad y características especiales.

Usamos setters para cambiar valores (como el nombre o el precio).

Aplicamos descuentos si el producto cumple ciertas condiciones (como una edición de bolsillo).

Calculamos el total a pagar por varios productos.

Actualizamos el inventario después de una compra.

Todo esto se ejecuta en el archivo main.py, donde se crean los productos y se prueban todas las funciones.

Este proyecto muestra de forma sencilla cómo funciona la herencia, los cambios de atributos y cómo se pueden aplicar diferentes métodos a distintos tipos de productos.

![image](https://github.com/user-attachments/assets/c123a90a-8128-4ae7-9ad0-336679583c64)

![image](https://github.com/user-attachments/assets/735fc3b2-a1d0-4592-acfa-d8bb9845d0fb)

![image](https://github.com/user-attachments/assets/c1c3b0d0-b4c2-4dc0-91f6-1b0edca73cf8)

![image](https://github.com/user-attachments/assets/16b1b982-1088-425b-8b25-9158614ce651)






















