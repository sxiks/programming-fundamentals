"""

Si alguien agregó:
"Manzana", "Pera" y "Leche" usando agregar_item.

¿Cómo escribirías tú las dos líneas de código exactas del bucle for dentro de mostrar_ticket para imprimir cada producto usando un F-String? (Ejemplo de impresión deseada: "Compraste: Manzana").

"""

"""
class CarritoCompras:
    def __init__(self, nombre_producto):
        # Asiganomos el parametro del nombre del producto
        self.nombre_producto = nombre_producto
        self.productos = [] # Crear una mochila vacia
        # La cual va contener los productos a agregar

    def agregar_item(self, item):
        self.productos.append(item)
        # Se llama la mochila, y usando el append agregamos a la mochila los items

    def mostrar_ticket(self):
        # Primero validamos si no hay nada en la mochila
        if not self.productos:
            print("No compraste nada.")
        else:
            # Creamos un bucle de si hay producto en la mochila lo imprima
            for producto in self.productos:
                print(f"\nCompraste: Manzana {producto.nombre_producto}")

if __name__ == "__main__":
    # Creamos el cliente (Se podira a futuro para mejorar crear otra clase para cliente con sus atributos y metodos)
    cliente1 = "Jean"

    # Agreamos los productos al cliente
    cliente1.agregar_item("Manzana", "Pera", "Leche")

    # Mostramos el ticket
    cliente1.mostrar_ticket()

"""

class CarritoCompras:
    # CORRECCIÓN 1: Quitamos 'nombre_producto'. El carrito nace vacío.
    def __init__(self):
        self.productos = [] 

    def agregar_item(self, item):
        self.productos.append(item)

    def mostrar_ticket(self):
        if not self.productos:
            print("No compraste nada.")
        else:
            print("\n--- TICKET DE COMPRA ---")
            for producto in self.productos:
                # CORRECCIÓN 2: Imprimimos la variable directamente, ya que guardamos textos (strings).
                print(f"Compraste: {producto}")

if __name__ == "__main__":
    # CORRECCIÓN 3: Usamos el molde (Clase) para fabricar el objeto carrito.
    cliente1 = CarritoCompras()

    # CORRECCIÓN 4: Agregamos los productos uno por uno, porque la función recibe un solo 'item' a la vez.
    cliente1.agregar_item("Manzana")
    cliente1.agregar_item("Pera")
    cliente1.agregar_item("Leche")

    # Mostramos el ticket
    cliente1.mostrar_ticket()