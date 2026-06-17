"""
Reto de integración — Notas del curso
Learning Path: docs/learning-path.md

Enunciado:
Dada una lista con las notas finales de un curso, calcula el promedio
general, cuenta cuántos estudiantes aprobaron (nota >= 6) y cuántos
reprobaron, e imprime un resumen del curso.

Conceptos integrados:
- Bucles (for) — Paso 05
- Condicionales (if / else) — Paso 05
- Listas — Paso 07

Este reto no introduce ningún concepto nuevo: combina, con mayor
autonomía, conceptos que ya fueron enseñados por separado.
"""

notas_del_curso = [8.5, 5.0, 6.2, 9.1, 4.8, 7.0, 6.0, 3.5]

suma_notas = 0
cantidad_aprobados = 0
cantidad_reprobados = 0

for nota in notas_del_curso:
    suma_notas = suma_notas + nota

    if nota >= 6:
        cantidad_aprobados = cantidad_aprobados + 1
    else:
        cantidad_reprobados = cantidad_reprobados + 1

promedio_curso = suma_notas / len(notas_del_curso)

print("Notas del curso:", notas_del_curso)
print("Promedio del curso:", round(promedio_curso, 2))
print("Estudiantes aprobados:", cantidad_aprobados)
print("Estudiantes reprobados:", cantidad_reprobados)