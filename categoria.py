# Clase para representar una Categoría
class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        producto.categoria = self

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            producto.categoria = None

    def __str__(self):
        productos = ', '.join([p.nombre for p in self.productos])
        return f"Categoría: {self.nombre} - {self.descripcion} | Productos: {productos}"
