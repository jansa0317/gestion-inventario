class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock")
        self.stock -= cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria.nombre}"
