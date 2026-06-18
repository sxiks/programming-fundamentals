"""
Paso 01 — Sintaxis: Salida básica con print()
Learning Path: docs/learning-path.md

Concepto principal: print() es la instrucción más básica de Python
para mostrar un resultado en pantalla. Es la primera herramienta que
necesitas para "ver" lo que tu código está haciendo.

Nota de numeración: este archivo aparece como 05 en la carpeta, pero
conceptualmente corresponde al Paso 01 (Sintaxis) — el archivo
01-define-call-return-variables.py ya existente mezcla varios pasos
(Sintaxis, Variables, Funciones), por lo que este archivo se agregó
después para cubrir Sintaxis por separado, sin tocar el original.
"""

# Lo más simple que puede hacer un programa: mostrar un mensaje.
print("Hola, mundo")

# print() puede recibir varios valores separados por comas. Por
# defecto, los separa con un espacio.
print("El resultado es:", 10, "puntos")

# El parámetro sep cambia el separador entre los valores.
print("rojo", "verde", "azul", sep=" - ")

# El parámetro end cambia qué se imprime al final (por defecto es un
# salto de línea). Aquí, dos print() seguidos terminan en la misma línea.
print("Cargando", end="...")
print("listo")

# Un comentario empieza con "#". Python lo ignora por completo al
# ejecutar el programa — solo es una nota para quien lee el código.
# print() es también la herramienta más usada para depurar: mostrar
# el valor de una variable en cualquier punto del programa para
# entender qué está pasando.
edad = 22
print("Valor de edad en este punto del programa:", edad)