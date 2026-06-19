# Sistema de inventario TechStore — manejo correcto de estado

def descontar_stock(stock_actual, cantidad_vendida):
    """Calcula el nuevo stock sin modificar nada por fuera."""
    if cantidad_vendida > stock_actual:
        raise ValueError("Stock insuficiente")
    return stock_actual - cantidad_vendida


def calcular_ingreso_total(ventas):
    """
    Recibe una lista de montos vendidos.
    No depende de ninguna variable externa: 100% predecible.
    """
    total = 0
    for venta in ventas:
        total += venta  # 'total' es local, nace y muere aquí
    return total


# Uso — el "estado" se maneja explícitamente desde afuera
stock_laptops = 20
stock_laptops = descontar_stock(stock_laptops, 3)
print(stock_laptops)  # 17

ventas_del_dia = [150000, 200000, 75000]
ingreso = calcular_ingreso_total(ventas_del_dia)
print(ingreso)  # 425000