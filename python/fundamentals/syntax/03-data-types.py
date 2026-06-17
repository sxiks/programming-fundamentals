"""
Paso 03 — Tipos de Datos
Learning Path: docs/learning-path.md

Concepto principal: cada valor que se guarda en una variable tiene
un tipo, que determina qué operaciones se pueden hacer con él.

Nota de alcance: Listas y Diccionarios ya se cubrieron en detalle en
data_structures/ (Paso 07). Aquí solo se mencionan brevemente como
tipos compuestos, sin repetir su contenido.
"""

# --- Tipos primitivos ---

# Números enteros: valores sin parte decimal.
edad = 22
print(edad, type(edad))

# Números decimales (float): valores con punto flotante.
promedio = 8.75
print(promedio, type(promedio))

# Booleanos: solo pueden ser True o False.
esta_matriculado = True
print(esta_matriculado, type(esta_matriculado))

# Nulo/Vacío: en Python se representa con None, la ausencia
# intencional de un valor.
telefono_alternativo = None
print(telefono_alternativo, type(telefono_alternativo))

# Nota: Python no tiene un tipo "carácter" separado. Un carácter es
# simplemente una cadena de texto de longitud 1.
inicial = "C"
print(inicial, type(inicial))


# --- Tipos compuestos ---

# Cadenas de texto: secuencias de caracteres.
nombre = "Camila"
print(nombre, type(nombre))

# Arrays/Listas y Objetos (diccionarios) ya se cubrieron con
# profundidad en data_structures/01-lists.py y 02-dictionaries.py.
# Aquí solo se nombran como ejemplo de tipo compuesto:
colores = ["rojo", "verde", "azul"]
estudiante = {"nombre": "Camila", "edad": 22}

# Tuplas: colecciones inmutables de tamaño fijo. A diferencia de una
# lista, una tupla no se puede modificar después de creada.
coordenada = (4.6, -75.6)
print(coordenada, type(coordenada))

# Las tuplas son útiles para devolver varios valores relacionados
# que no deben cambiar, como una coordenada de latitud y longitud.


# --- Sistemas de tipos ---

# Python usa tipado dinámico: el tipo de una variable se determina
# en tiempo de ejecución, y puede cambiar si se le asigna un valor
# de otro tipo.
valor = 10
print(valor, type(valor))

valor = "ahora soy un texto"
print(valor, type(valor))

# Python también usa tipado fuerte: no convierte automáticamente
# entre tipos incompatibles. La siguiente línea, si se ejecutara,
# produciría un error porque Python no suma un número con un texto
# de forma automática:
#
#     5 + "5"   →  TypeError
#
# Para combinarlos, hay que convertir el tipo explícitamente:
resultado = 5 + int("5")
print(resultado)