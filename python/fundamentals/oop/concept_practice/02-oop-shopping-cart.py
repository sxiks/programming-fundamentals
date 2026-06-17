class CarritoCompras:
    # Iniciamos el carrito de compras el cual va contener los productos a agregar
    def __init__(self):
        self.productos = [] 

    def agregar_item(self, item):
        # Se llama la mochila, y usando el método append agregamos los items a la mochila
        self.productos.append(item)

    def mostrar_ticket(self):
        # Primero validamos si no hay nada en la mochila
        if not self.productos:
            print("No compraste nada.")
        else:
            # Creamos un bucle de si hay producto en la mochila lo imprima 
            print("\n--- TICKET DE COMPRA ---")
            for producto in self.productos:
                print(f"Compraste: {producto}")


# Programa Principal
if __name__ == "__main__":
    # Creamos el cliente
    cliente1 = CarritoCompras()

    # Le agregamos los items al cliente
    cliente1.agregar_item("Manzana")
    cliente1.agregar_item("Pera")
    cliente1.agregar_item("Leche")

    # Mostramos el ticket
    cliente1.mostrar_ticket()