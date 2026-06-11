// Funcion base

function saludar(){
    console.log("Hola");
}

saludar();

// Saludar con parametros

function saludo(nombre){
    console.log(`Hola ${nombre}`);
}

saludo("Carlos");

// Funcion con retorno

function sumar(a, b){
    return a + b;
}

let resultado = sumar(5, 8);
console.log(resultado);