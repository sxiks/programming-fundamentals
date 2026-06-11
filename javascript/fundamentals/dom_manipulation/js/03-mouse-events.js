// Seleccionar el boton

let boton = document.querySelector("#btn");

// Evento de click

boton.addEventListener("click", function() {
    console.log("Click detectado");
});

// Evento MouseOver

boton.addEventListener("mouseover", function() {
    console.log("Mouse Encima");
});

// Seleccionar el input

let input = document.querySelector("#nombre");

// Evento de input 

input.addEventListener("input", function(){
    console.log(input.value);
});