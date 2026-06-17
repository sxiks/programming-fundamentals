/*
 * Paso 08 — Paradigmas Básicos: Programación Orientada a Objetos (introducción)
 * Learning Path: docs/learning-path.md
 *
 * Concepto principal: la POO organiza el código alrededor de objetos
 * que combinan datos (atributos) y comportamiento (métodos).
 *
 * Nota de alcance: esta es una introducción básica — clases, encapsulamiento,
 * herencia y polimorfismo. No se cubren aquí patrones de relación entre
 * clases (asociación, composición, dependencia) ni principios de diseño
 * avanzados.
 *
 * Nota de distinción: en el Paso 07 (Estructuras de Datos) ya usaste objetos
 * literales ({ ... }) para guardar datos. Una clase es algo distinto: es un
 * molde para crear objetos que comparten la misma estructura y el mismo
 * comportamiento.
 */

// --- Clases e instancias ---
class Persona {
  // El símbolo # marca un campo privado: solo es accesible
  // desde dentro de la propia clase. Esto es encapsulamiento.
  #edad;

  constructor(nombre, edad) {
    this.nombre = nombre;
    this.#edad = edad;
  }

  // Un método público que controla cómo se accede al dato privado.
  obtenerEdad() {
    return this.#edad;
  }

  // Encapsulamiento: en lugar de modificar #edad directamente desde
  // fuera, el cambio pasa por este método, que puede validar el valor.
  cumplirAnios() {
    this.#edad = this.#edad + 1;
  }

  describir() {
    return `${this.nombre} tiene ${this.#edad} años`;
  }
}

const persona1 = new Persona("Carlos", 30);
console.log(persona1.describir());

persona1.cumplirAnios();
console.log(persona1.describir());

// persona1.#edad daría un error si se intentara acceder directamente
// desde fuera de la clase — esa es la idea del encapsulamiento.


// --- Herencia ---
// Una clase puede heredar atributos y métodos de otra usando "extends".
class Estudiante extends Persona {
  constructor(nombre, edad, programa) {
    super(nombre, edad); // llama al constructor de Persona
    this.programa = programa;
  }

  // --- Polimorfismo ---
  // Estudiante redefine describir(). El mismo nombre de método
  // produce un comportamiento distinto según el tipo de objeto.
  describir() {
    return `${this.nombre} estudia ${this.programa} y tiene ${this.obtenerEdad()} años`;
  }
}

const estudiante1 = new Estudiante("Camila", 22, "Análisis y Desarrollo de Software");
console.log(estudiante1.describir());

// Polimorfismo en acción: el mismo método, llamado sobre objetos
// de clases distintas, produce salidas distintas (bucle del Paso 05).
const personas = [persona1, estudiante1];

for (const persona of personas) {
  console.log(persona.describir());
}