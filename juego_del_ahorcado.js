const inquirer = require('inquirer');
const fs = require('fs');
require('colors');


const menu = async (palabraBD) => {

    const palabraArrayFiltrada = palabraBD.split('').filter(item => item != '\r');
    const limite = 15;
    const palabraGenerada = [];

    console.log('###### JUEGO DEL AHORCADO ###### \n');

    console.log(`La palabra tiene ${palabraArrayFiltrada.length} caracteres ...\n`);

    const pregunta = [
        {
            type: 'input',
            name: 'letra',
            message: 'Digite una letra: '
        }
    ]

    for (let i=0; i<=limite; i++){

        if (palabraGenerada === palabraArrayFiltrada){
            console.log('Ganaste!!! ...');
        }
        const { letra } = await inquirer.prompt(pregunta);
        const indice = buscar(letra, palabraArrayFiltrada);
        palabraGenerada[indice] = letra;
    }

    console.log('Perdiste!!! No adivinaste la palabra ...\n');
    console.log(`La palabra era ${palabraArrayFiltrada}`);
        
}

const read = () => {

    const contenido = fs.readFileSync('./archivos/palabras.txt', 'utf-8');
    const palabras = contenido.split('\n');

    const palabrasArray = palabras.filter(item => item != '\r');
    const palabrasArray2 = palabrasArray.filter(item => item != '');

    const index = Math.floor(Math.random()*(palabrasArray2.length + 1));

    return palabrasArray2[index];
    
}

const buscar = (letra, arreglo = []) => {
    if (arreglo.indexOf(letra) == -1){
        console.log('La Letra no esta en la palabra ...\n'.red);
    } else {
        console.log(`La letra ${letra} está en la posicion ${arreglo.indexOf(letra)+1}\n`.green);

        return arreglo.indexOf(letra);
    }
}

const palabraBD = read();

menu(palabraBD);








