/**
 * var se utiliza para declarar variables que pueden cambiar su valor a lo largo del programa.
 * let se utiliza para declarar variables que pueden cambiar su valor, pero su alcance es limitado al bloque en el que se declaran.
 * const se utiliza para declarar variables que no pueden cambiar su valor después de ser asignadas, es decir, son constantes.
 */

var nombre = "Juan"; // Declaración de variable sin var, let o const (no recomendado)
var apellido = "Pérez"; // Declaración de variable sin var, let o const (no recomendado)

console.log(nombre); // Imprime "Juan"
console.log(apellido); // Imprime "Pérez"

let edad = 30; // Declaración de variable con let
console.log(edad); // Imprime 30

const PI = 3.14159; // Declaración de variable con const
console.log(PI); // Imprime 3.14159

// Intentar cambiar el valor de una variable declarada con const generará un error
// PI = 3.14; // Esto generará un error porque PI es una constante