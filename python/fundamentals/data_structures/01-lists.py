"""
Paso 07 — Estructuras de Datos: Listas
Learning Path: docs/learning-path.md

Concepto principal: las listas son colecciones ordenadas de elementos
que pueden crecer o reducirse durante la ejecución del programa.
"""

# Crear una lista
colores = ["rojo", "verde", "azul"]
print("Lista completa:", colores)

# Acceder a un elemento por su posición (índice). En Python,
# la primera posición es el índice 0, no el 1.
print("Primer color:", colores[0])
print("Último color:", colores[2])

# Agregar un elemento al final de la lista
colores.append("amarillo")
print("Lista después de agregar un color:", colores)

# Modificar un elemento existente
colores[1] = "verde oscuro"
print("Lista después de modificar un color:", colores)

# Eliminar un elemento por su valor
colores.remove("rojo")
print("Lista después de eliminar un color:", colores)

# Conocer cuántos elementos tiene la lista
print("Cantidad de colores:", len(colores))

# Recorrer todos los elementos de la lista (bucle for del Paso 05)
print("Recorriendo la lista:")
for color in colores:
    print("-", color)