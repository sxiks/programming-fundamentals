/*
 * Ejercicio guiado — Paso 05: Bucles
 * Learning Path: docs/learning-path.md
 *
 * Enunciado:
 * Una tienda registró sus ventas diarias durante una semana. Calcula el
 * total de ventas usando un bucle for, sin usar el método incorporado
 * reduce().
 *
 * Concepto reforzado: Bucles (for) — Paso 05.
 * Conceptos reutilizados: Arrays — Paso 07.
 */

const ventasDeLaSemana = [120000, 95000, 150000, 80000, 200000, 175000, 60000];

let totalVentas = 0;

for (let i = 0; i < ventasDeLaSemana.length; i++) {
  totalVentas = totalVentas + ventasDeLaSemana[i];
}

console.log("Ventas de la semana:", ventasDeLaSemana);
console.log("Total de ventas:", totalVentas);