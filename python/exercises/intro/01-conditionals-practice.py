"""
Ejercicio guiado — Paso 05: Condicionales
Learning Path: docs/learning-path.md

Enunciado:
Dado el precio de una compra, determina si aplica envío gratis. La
tienda ofrece envío gratis para compras de 50.000 o más. Si la compra
es menor, debe informarse cuánto falta para alcanzar el envío gratis.

Concepto reforzado: Condicionales (if / else) — Paso 05.
"""

precio_compra = 35000
monto_minimo_envio_gratis = 50000

if precio_compra >= monto_minimo_envio_gratis:
    print("¡Felicidades! Tu compra tiene envío gratis.")
else:
    monto_faltante = monto_minimo_envio_gratis - precio_compra
    print("Te faltan", monto_faltante, "para obtener envío gratis.")