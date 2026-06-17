"""
Paso 07 — Estructuras de Datos: Diccionarios
Learning Path: docs/learning-path.md

Concepto principal: los diccionarios almacenan pares clave-valor,
donde cada clave es única y permite acceder directamente a su valor
sin tener que recorrer toda la colección.
"""

# Crear un diccionario
estudiante = {
    "nombre": "Camila",
    "edad": 22,
    "programa": "Análisis y Desarrollo de Software"
}
print("Diccionario completo:", estudiante)

# Acceder a un valor usando su clave
print("Nombre:", estudiante["nombre"])
print("Programa:", estudiante["programa"])

# Agregar una nueva clave-valor
estudiante["ciudad"] = "Palmira"
print("Diccionario después de agregar una clave:", estudiante)

# Modificar el valor de una clave existente
estudiante["edad"] = 23
print("Diccionario después de modificar la edad:", estudiante)

# Verificar si una clave existe antes de usarla
if "ciudad" in estudiante:
    print("El estudiante tiene una ciudad registrada:", estudiante["ciudad"])

# Eliminar una clave-valor
del estudiante["edad"]
print("Diccionario después de eliminar la edad:", estudiante)

# Recorrer todas las claves y valores (bucle for del Paso 05)
print("Recorriendo el diccionario:")
for clave, valor in estudiante.items():
    print("-", clave, ":", valor)