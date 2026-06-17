"""
Paso 04 — Operadores
Learning Path: docs/learning-path.md

Concepto principal: los operadores realizan acciones sobre uno o más
valores (operandos) y producen un resultado.
"""

# --- Operadores aritméticos ---

a = 10
b = 3

print(a + b)   # suma
print(a - b)   # resta
print(a * b)   # multiplicación
print(a / b)   # división (siempre devuelve decimal en Python)
print(a % b)   # módulo: el residuo de la división
print(a ** b)  # potencia: a elevado a b


# --- Operadores de comparación ---

print(a == b)   # ¿son iguales en valor?
print(a != b)   # ¿son distintos en valor?
print(a > b)
print(a < b)
print(a >= 10)
print(a <= 10)

# Nota importante: "==" compara el VALOR. "is" compara la IDENTIDAD,
# es decir, si dos variables apuntan exactamente al mismo objeto en
# memoria. Esto se ve claramente con listas (Paso 07):
lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]
lista_3 = lista_1

print(lista_1 == lista_2)  # True: mismo contenido
print(lista_1 is lista_2)  # False: son dos listas distintas en memoria
print(lista_1 is lista_3)  # True: lista_3 es la misma lista que lista_1


# --- Operadores lógicos ---

es_mayor_de_edad = True
tiene_matricula_pagada = False

print(es_mayor_de_edad and tiene_matricula_pagada)  # ambas deben ser True
print(es_mayor_de_edad or tiene_matricula_pagada)   # al menos una debe ser True
print(not tiene_matricula_pagada)                   # invierte el valor

# Evaluación de cortocircuito: en "and", si el primer valor ya es
# False, Python ni siquiera evalúa el segundo, porque el resultado
# ya está decidido.
print(False and (10 / 0 == 0))  # no genera error: nunca llega a evaluar la división


# --- Operadores de asignación ---

contador = 5
print(contador)

contador += 1   # equivalente a: contador = contador + 1
print(contador)

contador -= 2   # equivalente a: contador = contador - 2
print(contador)

contador *= 3   # equivalente a: contador = contador * 3
print(contador)

contador /= 4   # equivalente a: contador = contador / 4
print(contador)


# --- Expresión condicional (el equivalente de Python al operador ternario) ---

nota = 7.5

resultado = "aprobado" if nota >= 6 else "reprobado"
print(resultado)


# --- Operadores bit a bit ---
# Nota de alcance: este es el sub-tema más avanzado de este paso.
# Se muestra brevemente por completitud, sin profundizar más allá
# de esto — no es el foco principal de Operadores.

x = 5   # 0101 en binario
y = 3   # 0011 en binario

print(x & y)    # AND a nivel de bits
print(x | y)    # OR a nivel de bits
print(x ^ y)    # XOR a nivel de bits
print(~x)       # NOT a nivel de bits
print(x << 1)   # desplazamiento a la izquierda
print(x >> 1)   # desplazamiento a la derecha