
const elements = require('./elements').ELEMENTS


class pessoasPage {
    clicarBtnConsultar(){
        cy.get(elements.paginaPessoas.btnConsultar).click()
    }

    clicarBtnNovo(){
        cy.get(elements.paginaPessoas.btnNovo).click()
    }

    preencheCampoDescricao(descricao){
        cy.get(elements.paginaPessoas.inputDescricao).type(descricao)
    }

    preencherCampoNomeCadastro(nomePessoa){
        cy.get(elements.paginaCadastroPessoa.inputNomePessoa).type(nomePessoa)
    }

    preencherCampoCPFCadastro(cpf){
        cy.get(elements.paginaCadastroPessoa.inputCPF).type(cpf)
    }

    preencherCampoDataNascimento(dataNascimento){
        cy.get(elements.paginaCadastroPessoa.inputDataNascimento).type(dataNascimento)
    }

    preencherCampoNomeMae(nomeMae){
        cy.get(elements.paginaCadastroPessoa.inputNomeMae).type(nomeMae)
    }

    selecionaPesquisarPorConsultaPessoas(selecionaPor){
        cy.get(elements.paginaPessoas.dropDowmListpesquisarPor).select(selecionaPor)       
    }

    selecionaSexocadastro(sexo){
        cy.get(elements.paginaCadastroPessoa.dropDowmListSexo).select(sexo)
    }

    verificaConsultaRealizada(descricao,coluna){
        cy.get(elements.paginaPessoas.tableResultados).contains(coluna).invoke('index').then((index) => {
            cy.get(`${elements.paginaPessoas.tableResultados} ${elements.paginaPessoas.colunaTabelaResultadosConsulta}(${index + 1})`).each((colunaEncontrada, index) => {
                cy.get(elements.paginaPessoas.tableResultados).find('tr').its('length').should('be.gt', 1);
                if(index > 0){
                    cy.get(colunaEncontrada).contains(descricao.toUpperCase())
                }
            })
        })
    }

}

export default new pessoasPage()
