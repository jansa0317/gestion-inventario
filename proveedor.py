class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_suministrados = []

    def agregar_producto(self, producto):
        self.productos_suministrados.append(producto)

    def __str__(self):
        return f"Proveedor: {self.nombre}, Teléfono: {self.telefono}, Productos: {[p.nombre for p in self.productos_suministrados]}"
