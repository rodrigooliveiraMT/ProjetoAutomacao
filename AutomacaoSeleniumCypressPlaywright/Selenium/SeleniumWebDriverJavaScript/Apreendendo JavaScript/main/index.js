console.log('Olá, mundo! Este é o meu primeiro código JavaScript.');

let nomeCompleto = 'Rodrigo de Oliveira Costa';
console.log('Meu nome é ' + nomeCompleto + '.');

// Variáveis e tipos de dados
let idade = 28;
console.log('Minha idade é ' + idade.toString() + ' anos.');

let estudante = 'Sim';
console.log('Sou estudante: ' + estudante.toLocaleUpperCase());

if (idade >= 18) {
    console.log('Sou maior de idade.');
} else {
    console.log('Sou menor de idade.');
}

/* Tipos de Váriaveis
Premitivos | Referencia
-------------------------
String    | Objects
Numero    | Arrays
Boolean   | Functions
undefined
null           
*/

// Variáveis
let itemName = 'Caneta';
let itemPrice = 2.50;
let itemValidade = true;
let itemColor = 'Azul';

// Objetos
let pen = {
    itemName: 'Caneta',
    itemPrice: 2.50,
    itemValidade: true,
    itemColor: 'Azul',
}
pen.itemColor = 'Vermelho';
console.log(pen.itemName);

// Index
let items = ['Caneta', 'Lápis', 'Borracha'];
items[1] = 'Caderno'; // Alterando o valor do índice 1
console.log(items[0]);
console.log(items[1]); // Imprime 'Caderno' após a alteração
console.log(items[2]);

// ==========================================================================================
// Função
function calcularSoma(a, b) {
    return a + b;
}
calcularSoma("resultado: " + 5, 3); // Chama a função para calcular a soma de 5 e 3
console.log(calcularSoma("resultado: " + (5 + 3))); // Imprime "resultado: 8"
// ==========================================================================================

// ==========================================================================================
function saleStatus(status, total /*parâmetro*/) {
    console.log('O status da venda é: ' + status, total);
}
saleStatus('Aprovada', 1000 /*Argumento*/); // Chama a função para exibir o status da venda
// ==========================================================================================

// ==========================================================================================
function calcularDesconto(price) {
    return price - (price * 10 / 100);
}
let total = calcularDesconto(20);
console.log('O preço com desconto é: ' + total);
// ==========================================================================================