import { When } from "@badeball/cypress-cucumber-preprocessor";
import pessoasPage from "../../../../../pages/pessoas/pessoas.page"

When('seleciona pesquisar por {string} para consultar pessoa', (selecionaPor) => {
    pessoasPage.selecionaPesquisarPorConsultaPessoas(selecionaPor)
})

When('informa a descricao {string}', (descricao) => {
    pessoasPage.preencheCampoDescricao(descricao)
})

When('clica no botão Consulta para realizar a consulta', () => {
    pessoasPage.clicaBtnConsultar()
})

When('informa o nome {string} para o cadastro da pessoa', (nomePessoa) => {
    pessoasPage.preencherCampoNomeCadastro(nomePessoa)
})

When('informa o cpf {string} para o cadastro da pessoa', (cpf) => {
    pessoasPage.preencherCampoCPFCadastro(cpf)
})

When('informa a data de nascimento {string} para o cadastro da pessoa', (dataNascimento) => {
    pessoasPage.preencherCampoDataNascimento(dataNascimento)
})

When('informa o nome da mãe como {string} para o cadastro da pessoa', (nomeMae) => {
    pessoasPage.preencherCampoNomeMae(nomeMae)
})

When('clica no botão novo', () =>{
    pessoasPage.clicarBtnNovo()
})

When('seleciona o sexo {string} para o cadastro da pessoa', (sexo) =>{
    pessoasPage.selecionaSexocadastro(sexo)
})