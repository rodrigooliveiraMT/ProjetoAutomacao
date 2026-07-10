from playwright.sync_api import expect

from dicionario.pericia_medica.cadastro_pessoas import cadastro_pessoa
from pages.pericia_medica_po import PericiaMedica

def test_login(page):
    dsl = PericiaMedica(page)
    #page.pause()
    expect(page).to_have_title("Pericia | Login")
    expect(dsl.tituto_login).to_have_text("Perícia Médica")
    dsl.login.fill('automacao')
    dsl.senha.fill('123')
    dsl.clique_botao(dsl.btn_login)
    expect(dsl.alert).to_have_text('Login ou Senha inválida!')
    dsl.clique_botao(dsl.button_ok)
    dsl.login.clear()
    dsl.senha.clear()
    dsl.login.fill('cqs.rodrigocosta')
    dsl.senha.fill('123')
    dsl.clique_botao(dsl.btn_login)
    dsl.verificar_texto(dsl.titulo_inicial, "Perícia Médica")
    dsl.clique_botao(dsl.link_cadastrar_pessoas)
    dsl.verificar_texto(dsl.label_consulta_pessoas, "Consulta de Pessoas")
    dsl.clique_botao(dsl.button_novo_pessoas)
    dsl.verificar_texto(dsl.link_dados_pessoais,"Dados Pessoais")
    dsl.preencher_campos(cadastro_pessoa)
    page.pause()