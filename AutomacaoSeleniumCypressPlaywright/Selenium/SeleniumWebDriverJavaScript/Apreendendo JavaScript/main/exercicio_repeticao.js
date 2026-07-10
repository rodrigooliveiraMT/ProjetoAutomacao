const nomes = ['Rodrigo', 'Roger', 'Ronaldy', 'Edu', 'Leticia']

// Arrey
nomes.forEach((nome, indice) => {
    console.log('Indice:', indice + 1)
    console.log('Nome: ', nome)
    console.log('-------------')
})

// For
for (let indice = 1; indice < nomes.length; indice++) {
    console.log(indice)
     console.log(nomes[indice])
}