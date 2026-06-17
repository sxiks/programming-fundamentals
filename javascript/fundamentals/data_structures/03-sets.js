/*
 * Paso 07 — Estructuras de Datos: Conjuntos (Sets)
 * Learning Path: docs/learning-path.md
 *
 * Concepto principal: los conjuntos son colecciones de elementos
 * únicos, sin duplicados y sin un orden garantizado.
 *
 * Nota de compatibilidad: las operaciones de unión, intersección y
 * diferencia se implementan aquí manualmente con el operador de
 * propagación (spread) y filter(), en lugar de los métodos nativos
 * Set.prototype.union/intersection/difference, que no están
 * disponibles en Node.js 18 (la versión de referencia de este
 * repositorio, ver README).
 */

// Crear un conjunto. Aunque "rojo" se repite, el conjunto solo lo
// guarda una vez.
const coloresFavoritos = new Set(["rojo", "verde", "azul", "rojo"]);
console.log("Conjunto de colores:", coloresFavoritos);

// Agregar un elemento
coloresFavoritos.add("amarillo");
console.log("Conjunto después de agregar un color:", coloresFavoritos);

// Intentar agregar un elemento que ya existe no produce ningún cambio
coloresFavoritos.add("rojo");
console.log("Conjunto después de intentar agregar un color repetido:", coloresFavoritos);

// Verificar si un elemento pertenece al conjunto
console.log("¿'verde' está en el conjunto?", coloresFavoritos.has("verde"));
console.log("¿'negro' está en el conjunto?", coloresFavoritos.has("negro"));

// Operaciones entre conjuntos
const coloresDeMaria = new Set(["azul", "negro", "blanco"]);

// Intersección: elementos que están en ambos conjuntos.
const interseccion = new Set(
  [...coloresFavoritos].filter((color) => coloresDeMaria.has(color))
);
console.log("Colores que tienen en común:", interseccion);

// Unión: todos los elementos de ambos conjuntos, sin duplicados.
const union = new Set([...coloresFavoritos, ...coloresDeMaria]);
console.log("Todos los colores entre ambos:", union);

// Diferencia: elementos que solo están en el primer conjunto.
const diferencia = new Set(
  [...coloresFavoritos].filter((color) => !coloresDeMaria.has(color))
);
console.log("Colores que solo tiene el primer conjunto:", diferencia);