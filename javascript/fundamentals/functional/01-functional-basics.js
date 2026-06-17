/*
 * Paso 08 — Paradigmas Básicos: Programación Funcional (introducción)
 * Learning Path: docs/learning-path.md
 *
 * Concepto principal: la programación funcional trata el código como
 * evaluación de funciones. Una idea central es la función pura: dada
 * la misma entrada, siempre devuelve la misma salida, sin modificar
 * nada fuera de sí misma.
 *
 * Nota de alcance: introducción básica. No se usan aquí los métodos
 * nativos map/filter/reduce — el objetivo es entender qué es una
 * función de orden superior construyendo una, no aprender la API
 * nativa de arrays (eso pertenece al Paso 07, ya cubierto).
 */

// --- Función pura ---
// Para la misma entrada, "duplicar" siempre devuelve la misma salida.
function duplicar(numero) {
  return numero * 2;
}

console.log(duplicar(4)); // 8
console.log(duplicar(4)); // sigue siendo 8, sin importar cuántas veces se llame


// --- Contraste: una función con efecto secundario ---
// Esta función no es pura: además de devolver un resultado, modifica
// un array que existe fuera de ella ("historial").
const historial = [];

function registrarYDuplicar(numero) {
  historial.push(numero);
  return numero * 2;
}

console.log(registrarYDuplicar(4)); // 8
console.log(registrarYDuplicar(4)); // 8 otra vez
console.log("Historial:", historial); // [4, 4] — el programa cambió de estado


// --- Función de orden superior ---
// Una función de orden superior recibe otra función como parámetro
// y la usa internamente.
function aplicarACadaElemento(lista, funcion) {
  const resultado = [];
  for (const elemento of lista) {
    resultado.push(funcion(elemento));
  }
  return resultado;
}

function alCuadrado(numero) {
  return numero * numero;
}

const numeros = [1, 2, 3, 4];

const duplicados = aplicarACadaElemento(numeros, duplicar);
const cuadrados = aplicarACadaElemento(numeros, alCuadrado);

console.log("Original:", numeros);
console.log("Duplicados:", duplicados);
console.log("Al cuadrado:", cuadrados);