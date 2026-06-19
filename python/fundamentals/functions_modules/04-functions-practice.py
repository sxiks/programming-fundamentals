# Construir una función que calcule el nuevo saldo de caja después de una venta, sin usar variables globales dentro de la función.

def actualizar_caja(saldo_actual, monto_venta):
    # Calcular adentro, con una variable local:
    nuevo_saldo = saldo_actual + monto_venta
    return nuevo_saldo

# Usarla desde afuera, actualizando la variable explícitamente:

caja = 500000
caja = actualizar_caja(caja, 120000)
print(caja)  # 620000

caja = actualizar_caja(caja, 80000)
print(caja)  # 700000