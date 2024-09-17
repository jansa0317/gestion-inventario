# Clase para representar un Proveedor
class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_suministrados = []

    def agregar_producto(self, producto):
        self.productos_suministrados.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos_suministrados:
            self.productos_suministrados.remove(producto)

    def __str__(self):
        productos = ', '.join([p.nombre for p in self.productos_suministrados])
        return f"Proveedor: {self.nombre} | Dirección: {self.direccion} | Teléfono: {self.telefono} | Productos: {productos}"
