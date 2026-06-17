"""
Paso 07 — Estructuras de Datos: Conjuntos (Sets)
Learning Path: docs/learning-path.md

Concepto principal: los conjuntos son colecciones de elementos únicos,
sin duplicados y sin un orden garantizado.
"""

# Crear un conjunto. Aunque "rojo" se repite, el conjunto solo lo
# guarda una vez.
colores_favoritos = {"rojo", "verde", "azul", "rojo"}
print("Conjunto de colores:", colores_favoritos)

# Agregar un elemento
colores_favoritos.add("amarillo")
print("Conjunto después de agregar un color:", colores_favoritos)

# Intentar agregar un elemento que ya existe no produce ningún cambio
colores_favoritos.add("rojo")
print("Conjunto después de intentar agregar un color repetido:", colores_favoritos)

# Verificar si un elemento pertenece al conjunto
print("¿'verde' está en el conjunto?", "verde" in colores_favoritos)
print("¿'negro' está en el conjunto?", "negro" in colores_favoritos)

# Operaciones entre conjuntos
colores_de_maria = {"azul", "negro", "blanco"}

print("Colores que tienen en común:", colores_favoritos & colores_de_maria)
print("Todos los colores entre ambos:", colores_favoritos | colores_de_maria)
print("Colores que solo tiene el primer conjunto:", colores_favoritos - colores_de_maria)