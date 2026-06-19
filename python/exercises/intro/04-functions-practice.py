"""
Ejercicio guiado — Paso 06: Listas
Learning Path: docs/learning-path.md

Enunciado:

Escenario: TechStore — sistema de alertas de stock bajo.
Regla de negocio:

Cada producto tiene un stock actual.
Si el stock es menor a 10 unidades, se debe generar una alerta.
Si el producto está marcado como es_temporada_alta (True), el umbral de alerta sube a 20 unidades en vez de 10 (porque se vende más rápido).

Tu tarea: Escribe una función llamada necesita_reabastecer que reciba:

stock_actual (número)
es_temporada_alta (True o False)

Y devuelva True si hay que reabastecer, o False si no.

"""

def acumular_descuento(descuento_actual, monto_compra):
    nuevo_descuento = descuento_actual
    if monto_compra > 200000:
        nuevo_descuento = nuevo_descuento + 5
    if nuevo_descuento > 30:
        nuevo_descuento = 30
    return nuevo_descuento

