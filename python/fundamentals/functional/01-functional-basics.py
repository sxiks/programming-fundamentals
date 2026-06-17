"""
Paso 08 — Paradigmas Básicos: Programación Funcional (introducción)
Learning Path: docs/learning-path.md

Concepto principal: la programación funcional trata el código como
evaluación de funciones. Una idea central de este paradigma es la
función pura: una función que, dada la misma entrada, siempre devuelve
la misma salida y no modifica nada fuera de sí misma.

Nota de alcance: esta es solo una introducción básica. No se cubren
aquí map/filter/reduce, composición de funciones ni inmutabilidad
estricta — el objetivo es mostrar la idea central usando únicamente
herramientas que ya conoces: funciones, listas y bucles.
"""

# --- Función pura ---
# Para la misma entrada, "duplicar" siempre devuelve la misma salida,
# y no modifica absolutamente nada fuera de ella misma.

def duplicar(numero):
    return numero * 2

print(duplicar(4))   # 8
print(duplicar(4))   # sigue siendo 8, sin importar cuántas veces se llame


# --- Contraste: una función con efecto secundario ---
# Esta función no es pura: además de devolver un resultado, modifica
# una lista que existe fuera de ella ("historial"). Esa modificación
# externa es justamente lo que el PDF llama "efecto secundario".

historial = []

def registrar_y_duplicar(numero):
    historial.append(numero)
    return numero * 2

print(registrar_y_duplicar(4))   # 8
print(registrar_y_duplicar(4))   # 8 otra vez
print("Historial:", historial)   # [4, 4] — el programa cambió de estado


# --- Función de orden superior ---
# Una función de orden superior es una función que recibe otra función
# como parámetro y la usa internamente.

def aplicar_a_cada_elemento(lista, funcion):
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


def al_cuadrado(numero):
    return numero * numero


numeros = [1, 2, 3, 4]

duplicados = aplicar_a_cada_elemento(numeros, duplicar)
cuadrados = aplicar_a_cada_elemento(numeros, al_cuadrado)

print("Original:", numeros)
print("Duplicados:", duplicados)
print("Al cuadrado:", cuadrados)