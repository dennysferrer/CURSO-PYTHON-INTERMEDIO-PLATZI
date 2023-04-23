
const inquirer = require('inquirer');


const inquirerInput = async () => {
    const pregunta = [
        {
            type: 'input',
            name: 'palabra',
            message: 'Ingrese la palabra: '
        }
    ];

    const { palabra } = await inquirer.prompt(pregunta);
    return palabra;

}

const palindrome = async () => {
    const palabra = await inquirerInput();
    const palabraInvertida = palabra.split("").reverse().join("");
    if (palabra == palabraInvertida){
        console.log('La palabra es Palindromo');
    } else {
        console.log('La palabra no es palindromo');
    }
}

palindrome();

