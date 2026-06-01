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

