"""
Paso 05 — Estructuras de Control: Bucles
Learning Path: docs/learning-path.md

Concepto principal: repetir un bloque de código varias veces usando
los bucles for y while.
"""

# for: cuando ya sabes cuántas veces quieres repetir algo.
for numero in range(1, 6):
    print("Contando:", numero)


# for también se usa para recorrer los elementos de una colección.
frutas = ["manzana", "banano", "fresa"]

for fruta in frutas:
    print("Fruta:", fruta)


# while: cuando no sabes de antemano cuántas veces se repetirá,
# y la repetición depende de una condición.
contador = 0

while contador < 3:
    print("El contador vale:", contador)
    contador = contador + 1

print("El bucle while terminó porque contador ya no es menor que 3")