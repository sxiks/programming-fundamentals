"""
Reto de integración — Libreta de contactos
Learning Path: docs/learning-path.md

Enunciado:
Construye una pequeña libreta de contactos. Cada contacto se identifica
por su nombre y guarda su teléfono y su ciudad. Debes poder agregar un
contacto nuevo y buscar un contacto existente por su nombre.

Conceptos integrados:
- Funciones — Paso 06
- Diccionarios — Paso 07
- Bucles (for) — Paso 05
- Condicionales (if / else) — Paso 05

Este reto no introduce ningún concepto nuevo: combina, con mayor
autonomía, conceptos que ya fueron enseñados por separado.
"""

libreta_de_contactos = {
    "Camila": {"telefono": "3001234567", "ciudad": "Palmira"},
    "Andrés": {"telefono": "3009876543", "ciudad": "Cali"},
}


def agregar_contacto(libreta, nombre, telefono, ciudad):
    if nombre in libreta:
        print(nombre, "ya existe en la libreta. No se agregó de nuevo.")
        return

    libreta[nombre] = {"telefono": telefono, "ciudad": ciudad}
    print(nombre, "fue agregado a la libreta.")


def buscar_contacto(libreta, nombre):
    if nombre in libreta:
        contacto = libreta[nombre]
        print(nombre, "- Teléfono:", contacto["telefono"], "- Ciudad:", contacto["ciudad"])
    else:
        print(nombre, "no está en la libreta.")


agregar_contacto(libreta_de_contactos, "Laura", "3012345678", "Palmira")
agregar_contacto(libreta_de_contactos, "Camila", "0000000000", "Bogotá")  # ya existe

buscar_contacto(libreta_de_contactos, "Andrés")
buscar_contacto(libreta_de_contactos, "Mateo")

print("\nTodos los contactos:")
for nombre, datos in libreta_de_contactos.items():
    print("-", nombre, ":", datos)