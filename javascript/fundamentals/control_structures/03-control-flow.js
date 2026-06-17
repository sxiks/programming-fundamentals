/*
 * Paso 05 — Estructuras de Control: Control de Flujo (break, continue)
 * Learning Path: docs/learning-path.md
 *
 * Concepto principal: alterar el comportamiento normal de un bucle.
 *
 * Nota de alcance: "return" también es parte del control de flujo,
 * pero termina una función — por eso se estudia en el Paso 06
 * (Funciones), no aquí. Este archivo se enfoca solo en lo que se
 * puede explicar usando exclusivamente bucles.
 */

// break: termina el bucle por completo, sin importar cuántas
// repeticiones quedaban pendientes.
console.log("Ejemplo con break:");

for (let numero = 1; numero < 10; numero++) {
  if (numero === 4) {
    break;
  }
  console.log("Número:", numero);
}

console.log("El bucle se detuvo apenas numero llegó a 4");


// continue: salta el resto del cuerpo del bucle en esa repetición
// y pasa directamente a la siguiente.
console.log("\nEjemplo con continue:");

for (let numero = 1; numero < 6; numero++) {
  if (numero === 3) {
    continue;
  }
  console.log("Número:", numero);
}

console.log("El número 3 nunca se imprimió, pero el bucle sí continuó");