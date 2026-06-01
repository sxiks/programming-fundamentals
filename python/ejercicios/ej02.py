"""
Escenario: TechStore — sistema de puntos de fidelización.
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

def calcular_puntos (total_compra):
    if total_compra >= 10000:
        return 1
    else:
        if total_compra < 10000:
            return 0
    
def vip (es_vip, puntos):
    if es_vip = True:
        puntos = es_vip * 2
    else:
        es_vip = False
        return 0

