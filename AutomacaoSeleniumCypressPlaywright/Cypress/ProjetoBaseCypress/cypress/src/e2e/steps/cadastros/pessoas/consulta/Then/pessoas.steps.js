import { Then } from "@badeball/cypress-cucumber-preprocessor";
import pessoasPage from "../../../../../pages/pessoas/pessoas.page"


Then('deve ser apresentada a pessoa vinculada ao cpf {string} na coluna {string} da tabela', (descricao, colunaTabela) => {
    pessoasPage.verificaConsultaRealizada(descricao,colunaTabela)
})

