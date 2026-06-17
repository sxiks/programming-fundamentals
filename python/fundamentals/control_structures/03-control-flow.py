"""
Paso 05 — Estructuras de Control: Control de Flujo (break, continue)
Learning Path: docs/learning-path.md

Concepto principal: alterar el comportamiento normal de un bucle.

Nota de alcance: "return" también es parte del control de flujo,
pero termina una función — por eso se estudia en el Paso 06 (Funciones),
no aquí. Este archivo se enfoca solo en lo que se puede explicar
usando exclusivamente bucles, que es lo que ya conoces hasta este punto.
"""

# break: termina el bucle por completo, sin importar cuántas
# repeticiones quedaban pendientes.
print("Ejemplo con break:")

for numero in range(1, 10):
    if numero == 4:
        break
    print("Número:", numero)

print("El bucle se detuvo apenas numero llegó a 4")


# continue: salta el resto del cuerpo del bucle en esa repetición
# y pasa directamente a la siguiente.
print("\nEjemplo con continue:")

for numero in range(1, 6):
    if numero == 3:
        continue
    print("Número:", numero)

print("El número 3 nunca se imprimió, pero el bucle sí continuó")