from categoria import Categoria
from producto import Producto
from proveedor import Proveedor
from bodega import Bodega

# Funciones para consultas y reportes
def consultar_producto(producto):
    proveedor = next((p.nombre for p in proveedores if producto in p.productos_suministrados), "Sin proveedor")
    return (f"Nombre: {producto.nombre}\n"
            f"Descripción: {producto.descripcion}\n"
            f"Precio: ${producto.precio}\n"
            f"Stock actual: {producto.stock}\n"
            f"Categoría: {producto.categoria.nombre if producto.categoria else 'Sin categoría'}\n"
            f"Proveedor: {proveedor}")

def consultar_categoria(categoria):
    productos = ', '.join([p.nombre for p in categoria.productos])
    return f"Nombre: {categoria.nombre}\nDescripción: {categoria.descripcion}\nProductos asociados: {productos}"

def consultar_proveedor(proveedor):
    productos = ', '.join([p.nombre for p in proveedor.productos_suministrados])
    return f"Nombre: {proveedor.nombre}\nDirección: {proveedor.direccion}\nTeléfono: {proveedor.telefono}\nProductos suministrados: {productos}"

def consultar_bodega(bodega):
    productos = ', '.join([p.nombre for p in bodega.productos_almacenados])
    return f"Nombre: {bodega.nombre}\nUbicación: {bodega.ubicacion}\nCapacidad máxima: {bodega.capacidad_maxima}\nProductos almacenados: {productos}"

def informe_stock_total(productos):
    stock_total = sum([p.stock for p in productos])
    return f"Stock total en el sistema: {stock_total}"

def informe_stock_por_categoria(categorias):
    informe = "Stock por categoría:\n"
    for categoria in categorias:
        stock_categoria = sum([p.stock for p in categoria.productos])
        informe += f"{categoria.nombre}: {stock_categoria} unidades\n"
    return informe

def informe_stock_por_proveedor(proveedores):
    informe = "Stock por proveedor:\n"
    for proveedor in proveedores:
        stock_proveedor = sum([p.stock for p in proveedor.productos_suministrados])
        informe += f"{proveedor.nombre}: {stock_proveedor} unidades\n"
    return informe

def informe_stock_por_bodega(bodegas):
    informe = "Stock por bodega:\n"
    for bodega in bodegas:
        stock_bodega = sum([p.stock for p in bodega.productos_almacenados])
        informe += f"{bodega.nombre}: {stock_bodega} unidades\n"
    return informe

# Datos de ejemplo
categoria1 = Categoria("Electrónica", "Dispositivos electrónicos")
categoria2 = Categoria("Muebles", "Productos para el hogar")

producto1 = Producto("Laptop", "Laptop de última generación", 1500, 10, categoria1,)
producto2 = Producto("Smartphone", "Teléfono inteligente", 800, 20, categoria1,)
producto3 = Producto("Sillon", "Sillon xl", 1200, 20, categoria2)

proveedor1 = Proveedor("Proveedor ABC", "123 Calle Principal", "555-1234")
proveedor1.agregar_producto(producto1)
proveedor1.agregar_producto(producto3)

bodega1 = Bodega("Bodega Central", "Cali", 50)
bodega2 = Bodega("Chipichape", "Cali", 60)
bodega1.agregar_producto(producto1)
bodega1.agregar_producto(producto2)
bodega2.agregar_producto(producto3)

productos = [producto1, producto2, producto3]
categorias = [categoria1, categoria2]
proveedores = [proveedor1]
bodegas = [bodega1,bodega2]


# Ejecución de consultas y reportes
print("Consulta de un producto:")
print(consultar_producto(producto1))

print("\nConsulta de una categoría:")
print(consultar_categoria(categoria1))

print("\nConsulta de un proveedor:")
print(consultar_proveedor(proveedor1))

print("\nConsulta de una bodega:")
print(consultar_bodega(bodega2))

#Reporte

print("\nInforme de stock total:")
print(informe_stock_total(productos))

print("\nInforme de stock por categoría:")
print(informe_stock_por_categoria(categorias))

print("\nInforme de stock por proveedor:")
print(informe_stock_por_proveedor(proveedores))

print("\nInforme de stock por bodega:")
print(informe_stock_por_bodega(bodegas))
