"""
Paso 03 — Tipos de Datos: Cadenas de Texto (profundización)
Learning Path: docs/learning-path.md

Concepto principal: una cadena de texto (string) es una secuencia de
caracteres. 03-data-types.py ya la presentó como tipo compuesto; este
archivo profundiza en las operaciones más comunes sobre cadenas.
"""

nombre = "Camila"

# Concatenación: unir cadenas con +.
saludo = "Hola, " + nombre
print(saludo)

# Repetición: multiplicar una cadena por un número la repite.
separador = "-" * 10
print(separador)

# Una cadena es una secuencia, igual que una lista (Paso 07):
# se puede acceder a cada carácter por su posición (índice).
print(nombre[0])   # primer carácter
print(nombre[-1])  # último carácter

# Slicing: extraer una parte de la cadena indicando inicio y fin.
print(nombre[0:3])  # los primeros 3 caracteres

# len() devuelve cuántos caracteres tiene la cadena.
print(len(nombre))

# Algunos métodos comunes de las cadenas:
texto = "  Hola Mundo  "

print(texto.upper())     # todo en mayúsculas
print(texto.lower())     # todo en minúsculas
print(texto.strip())     # elimina espacios al inicio y al final
print(texto.replace("Mundo", "Python"))  # reemplaza una parte del texto

# f-strings: la forma más común en Python moderno de combinar
# variables con texto, usando el prefijo f y llaves {}.
edad = 22
mensaje = f"{nombre} tiene {edad} años"
print(mensaje)

# Recorrer una cadena carácter por carácter, reutilizando el bucle
# for ya visto en el Paso 05.
for letra in "Sol":
    print(letra)