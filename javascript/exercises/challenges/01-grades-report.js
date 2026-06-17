/*
 * Reto de integración — Notas del curso
 * Learning Path: docs/learning-path.md
 *
 * Enunciado:
 * Dado un array con las notas finales de un curso, calcula el promedio
 * general, cuenta cuántos estudiantes aprobaron (nota >= 6) y cuántos
 * reprobaron, e imprime un resumen del curso.
 *
 * Conceptos integrados:
 * - Bucles (for) — Paso 05
 * - Condicionales (if / else) — Paso 05
 * - Arrays — Paso 07
 *
 * Este reto no introduce ningún concepto nuevo: combina, con mayor
 * autonomía, conceptos que ya fueron enseñados por separado.
 */

const notasDelCurso = [8.5, 5.0, 6.2, 9.1, 4.8, 7.0, 6.0, 3.5];

let sumaNotas = 0;
let cantidadAprobados = 0;
let cantidadReprobados = 0;

for (let i = 0; i < notasDelCurso.length; i++) {
  const nota = notasDelCurso[i];
  sumaNotas = sumaNotas + nota;

  if (nota >= 6) {
    cantidadAprobados = cantidadAprobados + 1;
  } else {
    cantidadReprobados = cantidadReprobados + 1;
  }
}

const promedioCurso = sumaNotas / notasDelCurso.length;

console.log("Notas del curso:", notasDelCurso);
console.log("Promedio del curso:", promedioCurso.toFixed(2));
console.log("Estudiantes aprobados:", cantidadAprobados);
console.log("Estudiantes reprobados:", cantidadReprobados);