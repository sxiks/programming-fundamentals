"""
Ejercicio guiado — Paso 05: Bucles
Learning Path: docs/learning-path.md

Enunciado:
Una tienda registró sus ventas diarias durante una semana. Calcula el
total de ventas usando un bucle for, sin usar la función incorporada
sum().

Concepto reforzado: Bucles (for) — Paso 05.
Conceptos reutilizados: Listas — Paso 07.
"""

ventas_de_la_semana = [120000, 95000, 150000, 80000, 200000, 175000, 60000]

total_ventas = 0

for venta in ventas_de_la_semana:
    total_ventas = total_ventas + venta

print("Ventas de la semana:", ventas_de_la_semana)
print("Total de ventas:", total_ventas)