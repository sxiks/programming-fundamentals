"""
Ejercicio guiado — Paso 07: Listas
Learning Path: docs/learning-path.md

Enunciado:
Mantén una lista de estudiantes inscritos en un curso. Antes de
inscribir a un nuevo estudiante, verifica que no esté ya en la lista
para evitar inscripciones duplicadas.

Concepto reforzado: Listas — Paso 07.
Conceptos reutilizados: Condicionales — Paso 05.
"""

estudiantes_inscritos = ["Camila", "Andrés", "Laura"]

nuevo_estudiante = "Andrés"

if nuevo_estudiante in estudiantes_inscritos:
    print(nuevo_estudiante, "ya está inscrito. No se agregó de nuevo.")
else:
    estudiantes_inscritos.append(nuevo_estudiante)
    print(nuevo_estudiante, "fue inscrito correctamente.")

print("Lista actual de inscritos:", estudiantes_inscritos)