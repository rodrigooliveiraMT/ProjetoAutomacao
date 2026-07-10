Feature: Usuário realiza consultas na página de consulta de pessoas

    Background:
        Given o Usuário está logado no SisprevWeb
        When navega para a página de Consulta de pessoas
    
    Scenario: o usuário realiza uma consulta com um cpf válido
        And seleciona pesquisar por "Nome" para consultar pessoa 
        And informa a descricao "maria" 
        And clica no botão Consulta para realizar a consulta
        Then deve ser apresentada a pessoa vinculada ao cpf "maria" na coluna "Nome" da tabela

    Scenario: o usuario realizar uma consulta pelo nome da mãe
        And seleciobe pesquisarpor "Nome da Mãe" para consultar pessoa
        And informa a descricao "MARIA INÊS SOUZA"
        And clica no botão Consulta para realizar a consulta
        Then deve ser apresentado o registro "MARIA INÊS SOUZA" na coluna "Mãe" da tabela dos resultados encontrados na consulta