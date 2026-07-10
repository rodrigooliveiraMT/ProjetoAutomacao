import { Given, When, Then} from "@badeball/cypress-cucumber-preprocessor";
import loginPage from "../../pages/login/login.page";

Given('o Usuário está logado no SisprevWeb', () => {
    loginPage.realizaAutenticacao()
})