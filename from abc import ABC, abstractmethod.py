from abc import ABC, abstractmethod
from datetime import date

# Clase abstracta Producto
class Producto(ABC):
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar_detalles(self):
        pass

# Subclase Electrónico
class Electronico(Producto):
    def __init__(self, id, nombre, precio, marca, garantia):
        super().__init__(id, nombre, precio)
        self.marca = marca
        self.garantia = garantia

    def mostrar_detalles(self):
        print(f"[Electrónico] {self.nombre} - Marca: {self.marca}, Precio: ${self.precio}, Garantía: {self.garantia} meses")

# Subclase Alimento
class Alimento(Producto):
    def __init__(self, id, nombre, precio, fecha_caducidad, perecedero):
        super().__init__(id, nombre, precio)
        self.fecha_caducidad = fecha_caducidad
        self.perecedero = perecedero

    def mostrar_detalles(self):
        print(f"[Alimento] {self.nombre} - Precio: ${self.precio}, Caduca: {self.fecha_caducidad}, Perecedero: {self.perecedero}")

# Subclase Ropa
class Ropa(Producto):
    def __init__(self, id, nombre, precio, talla, material):
        super().__init__(id, nombre, precio)
        self.talla = talla
        self.material = material

    def mostrar_detalles(self):
        print(f"[Ropa] {self.nombre} - Precio: ${self.precio}, Talla: {self.talla}, Material: {self.material}")

# Función principal
def main():
    inventario = [
        Electronico(1, "Laptop", 15000, "HP", 24),
        Ropa(2, "Camisa", 350, "M", "Algodón"),
        Alimento(3, "Leche", 25, date(2025, 8, 15), True)
    ]

    print("=== Inventario de Productos ===")
    for producto in inventario:
        producto.mostrar_detalles()

if __name__ == "__main__":
    main()
