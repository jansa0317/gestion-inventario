class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = []

    def agregar_producto(self, producto):
        if len(self.productos_almacenados) < self.capacidad_maxima:
            self.productos_almacenados.append(producto)
        else:
            raise ValueError("No hay suficiente espacio en la bodega")

    def __str__(self):
        return f"Bodega: {self.nombre}, Ubicación: {self.ubicacion}, Capacidad: {self.capacidad_maxima}, Productos almacenados: {[p.nombre for p in self.productos_almacenados]}"
