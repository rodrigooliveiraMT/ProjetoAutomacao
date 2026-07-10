const env = require('../../../../../cypress.env.json')
const faker = require('faker')

const Login = require('../../../../../cypress.env.json').usuario.login
const Senha = require('../../../../../cypress.env.json').usuario.senha


class LoginPage{
    acessarSisprev(){
        cy.visit(`${env.config.UrlBase}${env.config.BaseDados}${env.config.sisprevweb}${env.config.login}`)
    }

    realizaAutenticacao(){
        const options = {cacheSession: true}
        cy.commandrealizaLogin(Login, Senha, options)
    }

}
export default new LoginPage();