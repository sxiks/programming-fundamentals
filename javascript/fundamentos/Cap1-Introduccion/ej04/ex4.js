let nombre, edad, direccion, movil, email; //Se pueden declarar varias variables en una sola línea, separándolas por comas

//Promt es una función que muestra un cuadro de diálogo que solicita al usuario que ingrese un valor. El valor ingresado se almacena en la variable correspondiente.

nombre = prompt("Ingrese su nombre:"); //Pedir datos al usuario.
document.write("Bienvenido: ", nombre, "<br>");
console.log("Bienvenido: ", nombre);

edad = prompt("Escriba su edad:"); //Pedir datos al usuario.
document.write("Edad: ", edad, "<br>");
console.log("Edad: ", edad);


direccion = prompt("Escriba su dirección:"); //Pedir direccion al usuario.
document.write("Dirección: ", direccion, "<br>");
console.log("Dirección: ", direccion);

movil = prompt("Escriba su número de móvil:"); //Pedir el movil del usuario.
document.write("Número de móvil: ", movil, "<br>");
console.log("Número de móvil: ", movil);

email = prompt("Escriba su correo electrónico:"); //Pedir el correo al usuario.
document.write("Correo electrónico: ", email, "<br>");
console.log("Correo electrónico: ", email);
