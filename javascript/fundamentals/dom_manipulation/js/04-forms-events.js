// Seleccionar el formulario y enviar el evento (refactorizado para enviar la repeticion del evento)
// let formulario = document.query.Selector("#formulario");

//      Evento para el envio del formulario

// formulario.addEventlistener("submit", function(event){
//     event.preventDefault(); // Evitar envio del formulario

    // Capturar el valor del input
//     let nombre = document.querySelector("#nombre").value;

//     console.log("Formulario Enviado");
//     console.log(nombre); // Mostrar el valor del input
// });

// Seleccionar el formulario

let formulario = document.querySelector("#formulario");

formulario.addEventListener("submit", function(event){
    event.preventDefault();
    console.log("Formulario enviado");
});

// Capturar el calor del input

let nombre = document.querySelector("#nombre");

formulario.addEventListener("submit", function(event){
    event.preventDefault();
    console.log(nombre.value);
});
