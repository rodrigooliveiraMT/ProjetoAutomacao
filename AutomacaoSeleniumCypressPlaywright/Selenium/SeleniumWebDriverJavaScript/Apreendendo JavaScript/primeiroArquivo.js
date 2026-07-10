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

// Função
function calcularSoma(a, b) {
    return a + b;
    console.log('Imprime após o return'); // Este código não será executado
}
calcularSoma(5, 3); // Chama a função para calcular a soma de 5 e 3
console.log(calcularSoma(5, 3)); // Imprime 8