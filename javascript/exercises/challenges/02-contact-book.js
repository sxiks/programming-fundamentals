/*
 * Reto de integración — Libreta de contactos
 * Learning Path: docs/learning-path.md
 *
 * Enunciado:
 * Construye una pequeña libreta de contactos. Cada contacto se identifica
 * por su nombre y guarda su teléfono y su ciudad. Debes poder agregar un
 * contacto nuevo y buscar un contacto existente por su nombre.
 *
 * Conceptos integrados:
 * - Funciones — Paso 06
 * - Objetos — Paso 07
 * - Bucles (for...in) — Paso 05
 * - Condicionales (if / else) — Paso 05
 *
 * Este reto no introduce ningún concepto nuevo: combina, con mayor
 * autonomía, conceptos que ya fueron enseñados por separado.
 */

const libretaDeContactos = {
  Camila: { telefono: "3001234567", ciudad: "Palmira" },
  Andrés: { telefono: "3009876543", ciudad: "Cali" },
};

function agregarContacto(libreta, nombre, telefono, ciudad) {
  if (nombre in libreta) {
    console.log(nombre, "ya existe en la libreta. No se agregó de nuevo.");
    return;
  }

  libreta[nombre] = { telefono: telefono, ciudad: ciudad };
  console.log(nombre, "fue agregado a la libreta.");
}

function buscarContacto(libreta, nombre) {
  if (nombre in libreta) {
    const contacto = libreta[nombre];
    console.log(nombre, "- Teléfono:", contacto.telefono, "- Ciudad:", contacto.ciudad);
  } else {
    console.log(nombre, "no está en la libreta.");
  }
}

agregarContacto(libretaDeContactos, "Laura", "3012345678", "Palmira");
agregarContacto(libretaDeContactos, "Camila", "0000000000", "Bogotá"); // ya existe

buscarContacto(libretaDeContactos, "Andrés");
buscarContacto(libretaDeContactos, "Mateo");

console.log("\nTodos los contactos:");
for (const nombre in libretaDeContactos) {
  console.log("-", nombre, ":", libretaDeContactos[nombre]);
}