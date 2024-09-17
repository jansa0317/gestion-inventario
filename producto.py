# Clase para representar un Producto
class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad

    def valor_total_stock(self):
        return self.stock * self.precio

    def __str__(self):
        categoria = self.categoria.nombre if self.categoria else "Sin categoría"
        return f"Producto: {self.nombre} - {self.descripcion} | Precio: ${self.precio} | Stock: {self.stock} | Categoría: {categoria}"
