/*
 * Ejercicio guiado — Paso 07: Arrays
 * Learning Path: docs/learning-path.md
 *
 * Enunciado:
 * Mantén una lista de estudiantes inscritos en un curso. Antes de
 * inscribir a un nuevo estudiante, verifica que no esté ya en la lista
 * para evitar inscripciones duplicadas.
 *
 * Concepto reforzado: Arrays — Paso 07.
 * Conceptos reutilizados: Condicionales — Paso 05.
 */

const estudiantesInscritos = ["Camila", "Andrés", "Laura"];

const nuevoEstudiante = "Andrés";

if (estudiantesInscritos.includes(nuevoEstudiante)) {
  console.log(nuevoEstudiante, "ya está inscrito. No se agregó de nuevo.");
} else {
  estudiantesInscritos.push(nuevoEstudiante);
  console.log(nuevoEstudiante, "fue inscrito correctamente.");
}

console.log("Lista actual de inscritos:", estudiantesInscritos);