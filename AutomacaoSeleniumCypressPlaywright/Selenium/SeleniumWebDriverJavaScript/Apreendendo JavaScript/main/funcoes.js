// Criar Funções
function gerarNome(){
    const nome = 'Rodrigo '
    const sobreNome = 'Costa'
    const idade = 27

    console.log('Nome: ', nome + sobreNome)
    console.log('Idade: ', idade)
}

// Chamar Funções em JavaScript
gerarNome()



// Criar Funções
// Passando Funções por parâmetros
function gerarNome(nome, sobreNome, idade){
    console.log('Nome: ', nome + sobreNome)
    console.log('Idade: ', idade)
}

// Chamar Funções em JavaScript
gerarNome('Roger ', 'Costa', 31)


// Criar Funções
// Passando Funções por parâmetros
// Funções que retorna dados
function gerarNome(nome, sobreNome, idade){
    return 'Nome: ' + nome + sobreNome + idade
}

// Chamar Funções em JavaScript

// Usando console.log
console.log(gerarNome('Roger ', 'Costa ', 31))

// Usando const
const nomeGerado = gerarNome('Roger ', 'Costa ', 31)
console.log(nomeGerado)