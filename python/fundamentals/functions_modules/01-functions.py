"""
Escenario: TechStore — sistema de puntos de finalización.
Reglas:

Por cada $10.000 en compras, el cliente gana 1 punto
Si el cliente tiene membresía VIP, los puntos se duplican

Tu tarea: Escribe una función llamada calcular_puntos que reciba:

total_compra (número)
es_vip (True o False)

Y devuelva la cantidad de puntos ganados.
Antes de escribir código, responde esto:

¿Cuántos parámetros tiene la función?
¿Qué devuelve?
¿Cómo calcularías los puntos sin VIP?
¿Cómo los calcularías con VIP?

"""

def calcular_puntos (total_compra, es_vip):
    puntos = total_compra // 10000
    if es_vip:
        puntos *= 2
    return puntos

print(calcular_puntos(75000, False))  # ¿Cuánto da?
print(calcular_puntos(75000, True))   # ¿Cuánto da?
print(calcular_puntos(15000, False))  # ¿Cuánto da?
print(calcular_puntos(15000, True))   # ¿Cuánto da?

print("==============================")

def calcular_envio (total_pedido):
    if total_pedido < 100000:
        return 15000
    else:
        return 0
    
print(calcular_envio(80000))
print(calcular_envio(150000))
print(calcular_envio(100000))

def resumen_pedido(precio_unitario, cantidad):
    subtotal = precio_unitario * cantidad
    envio = calcular_envio(subtotal)
    total = subtotal + envio
    return total

print(resumen_pedido(30000, 2))
print(resumen_pedido(60000, 2))

print("==============================")


def calcular_envio (total_pedido):
    if total_pedido < 100000:
        return 15000
    else:
        return 0
    
print(calcular_envio(80000))
print(calcular_envio(150000))
print(calcular_envio(100000))

def resumen_pedido(precio_unitario, cantidad):
    subtotal = precio_unitario * cantidad
    envio = calcular_envio(subtotal)
    total = subtotal + envio
    return total

print(resumen_pedido(30000, 2))
print(resumen_pedido(60000, 2))

