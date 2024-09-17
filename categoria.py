class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Categoria: {self.nombre}, Descripción: {self.descripcion}"
