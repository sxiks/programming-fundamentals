/*
 * Ejercicio guiado — Paso 05: Condicionales
 * Learning Path: docs/learning-path.md
 *
 * Enunciado:
 * Dado el precio de una compra, determina si aplica envío gratis. La
 * tienda ofrece envío gratis para compras de 50.000 o más. Si la compra
 * es menor, debe informarse cuánto falta para alcanzar el envío gratis.
 *
 * Concepto reforzado: Condicionales (if / else) — Paso 05.
 */

const precioCompra = 35000;
const montoMinimoEnvioGratis = 50000;

if (precioCompra >= montoMinimoEnvioGratis) {
  console.log("¡Felicidades! Tu compra tiene envío gratis.");
} else {
  const montoFaltante = montoMinimoEnvioGratis - precioCompra;
  console.log("Te faltan", montoFaltante, "para obtener envío gratis.");
}