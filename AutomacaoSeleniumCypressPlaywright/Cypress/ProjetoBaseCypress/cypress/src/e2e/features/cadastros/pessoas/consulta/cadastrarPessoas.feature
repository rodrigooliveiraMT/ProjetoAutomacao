Feature: O usuário realiza cadastro de pessoas

    Background:
            Given o Usuário está logado no SisprevWeb
            When navega para a página de Consulta de pessoas
            And clica no botão novo

    Scenario: o usuario realiza o cadastro de uma nova pessoa no sistema
        And informa o nome "Eduarda Moreira" para o cadastro da pessoa
        And informa o cpf "123.456.789-11" para o cadastro da pessoa
        And seleciona o sexo "Feminino" para o cadastro da pessoa
        And informa a data de nascimento "13/03/2000" para o cadastro da pessoa
        And informa o nome da mãe como "Marilza Moreira" para o cadastro da pessoa 