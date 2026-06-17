"""
Paso 02 — Variables
Learning Path: docs/learning-path.md

Concepto principal: una variable es un nombre que se le da a un
espacio en memoria para guardar un valor, y que puede cambiar
durante la ejecución del programa.

Nota: el archivo 01-define-call-return-variables.py ya usa variables
de forma práctica. Este archivo se enfoca exclusivamente en el
concepto de variable en sí: cómo se crean, cómo se reasignan, y
cómo deben nombrarse.
"""

# Crear una variable es asignarle un valor con el operador "=".
nombre = "Camila"
print(nombre)

# Una variable puede reasignarse: el mismo nombre puede apuntar a
# un valor distinto en otro momento del programa.
nombre = "Andrés"
print(nombre)

# Python permite asignar varias variables en una sola línea.
ciudad, pais = "Palmira", "Colombia"
print(ciudad, pais)

# Los nombres de variable en Python siguen la convención snake_case:
# palabras en minúscula separadas por guion bajo.
edad_estudiante = 22
promedio_general = 8.7

print(edad_estudiante)
print(promedio_general)

# Un nombre de variable no puede empezar con un número, ni contener
# espacios o símbolos como -, +, @. Estos dos nombres son válidos:
nombre_completo = "Laura Gómez"
_total = 100

print(nombre_completo)
print(_total)