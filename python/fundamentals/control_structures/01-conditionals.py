"""
Paso 05 — Estructuras de Control: Condicionales
Learning Path: docs/learning-path.md

Concepto principal: tomar decisiones en el código usando if / elif / else.

Un condicional permite que el programa ejecute un bloque de código
diferente dependiendo de si una condición es verdadera o falsa.
"""

nota = 7.5

if nota >= 9:
    print("Excelente, tu nota es", nota)
elif nota >= 6:
    print("Aprobado, tu nota es", nota)
else:
    print("Reprobado, tu nota es", nota)


# Un condicional sin "elif" — solo dos caminos posibles.
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Las condiciones pueden combinarse con operadores lógicos
# (esto ya lo viste en el Paso 04 — Operadores).
temperatura = 30
es_fin_de_semana = True

if temperatura > 25 and es_fin_de_semana:
    print("Buen día para ir a la piscina")
else:
    print("Mejor quedarse en casa")