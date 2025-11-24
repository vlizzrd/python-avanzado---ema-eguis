class Componente:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"venta realizada: {cantidad} unidades de {self.nombre}.")
            return True
        else:
            print(f"error: No hay suficiente stock para vender {cantidad} unidades de {self.nombre}.")
            return False

    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"precio: ${self.precio:.2f}")
        print(f"stock: {self.stock} unidades")

