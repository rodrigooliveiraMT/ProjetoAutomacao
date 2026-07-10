// Exercício 2 - Estrutura de decisão

// Percorrer uma lista de cidades
// contendo: ['Cuiabá', 'Vg', 'Jangada', 'Caceres']
// Para cada item, verificar se a cidade de Vg está presente na lista
// Printar nome da cidade
// Caso esteja, avisar
// Caso não seja o elemento procurado, avisar também
// Número da execução

// Execução: 1
// Cidade: Cuiabá
// Encontrado / Não Encontrado
// ---------------------------

const cidades = ['Cuiabá', 'Vg', 'Jangada', 'Caceres']

cidades.forEach((cidade, indice) => {
    console.log('Índice: ', indice + 1)
    console.log('Cidade: ', cidade)

    if (cidade == 'Vg') {
        console.log('Encontrado')
    } else {
        console.log('Não Encontrado')
    }
    console.log('-----------')
})

