import { When } from "@badeball/cypress-cucumber-preprocessor"
import rotas from "../../../../fixtures/rotas.json"

When('navega para a página de Consulta de pessoas', () => {
    cy.commandNavegaParaPagina(rotas.url.consultaPessoa)
})