# Clase para representar una Bodega
class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = []

    def agregar_producto(self, producto):
        if len(self.productos_almacenados) < self.capacidad_maxima:
            self.productos_almacenados.append(producto)

    def retirar_producto(self, producto, cantidad):
        if producto in self.productos_almacenados and producto.stock >= cantidad:
            producto.retirar_stock(cantidad)

    def consultar_disponibilidad(self, producto):
        if producto in self.productos_almacenados:
            return f"El producto '{producto.nombre}' está disponible en la bodega '{self.nombre}'. Stock: {producto.stock}"
        return f"El producto '{producto.nombre}' no está en la bodega '{self.nombre}'."

    def __str__(self):
        productos = ', '.join([p.nombre for p in self.productos_almacenados])
        return f"Bodega: {self.nombre} | Ubicación: {self.ubicacion} | Capacidad: {self.capacidad_maxima} | Productos: {productos}"
