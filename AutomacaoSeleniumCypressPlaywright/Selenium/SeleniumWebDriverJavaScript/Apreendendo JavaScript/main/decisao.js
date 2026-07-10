// Se quiser, posso te mostrar também:
// estrutura ideal de projeto Node + Selenium
// como rodar testes com npm run test
// diferença entre npm start, npm run, npx e node (isso evita muita confusão).

// if and else

// if (condicao) {
//     condicao = true
// } else {
//     condicao = false
// }

const nome = 'Edu'

// SIM
if (nome == 'Edu'){
    console.log('Verdadeiro')
} else {
    console.log('Falso')
}

// NÃO
if (nome == 'Echo'){
    console.log('Verdadeiro')
} else {
    console.log('Falso')
}

// Uso de ternário
let resultado = nome === 'Echo' ? 'Sim' : 'Não'
console.log(resultado)
