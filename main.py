class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def registrar_producto(self, margen_de_venta, callback):
        self.precio_de_venta = self.costo / (1 - margen_de_venta)
        callback(self)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, " \
               f"Costo: {self.costo}, Cantidad: {self.cantidad}, Precio de venta: {self.precio_de_venta}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def imprimir_inventario(self):
        for producto in self.productos.values():
            print(producto)


def asignar_precio_de_venta(producto):
    print(f"El precio de venta del producto {producto.nombre} es: {producto.precio_de_venta}")


inventario = Inventario()

producto1 = Producto(1, "Producto 1", "Descripción del producto 1", 10, 5)
producto1.registrar_producto(0.2, asignar_precio_de_venta)
inventario.agregar_producto(producto1)

producto2 = Producto(2, "Producto 2", "Descripción del producto 2", 15, 3)
producto2.registrar_producto(0.3, asignar_precio_de_venta)
inventario.agregar_producto(producto2)

inventario.imprimir_inventario()
