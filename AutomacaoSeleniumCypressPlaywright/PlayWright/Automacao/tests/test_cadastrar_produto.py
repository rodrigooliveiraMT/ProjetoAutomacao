import pytest
from playwright.sync_api import expect

from pages.cadastrar_produto_po import BasePage
from resources.cadastrar_produto_url import cadastrar_produto_api_url

@pytest.mark.order(1)
def test_abrir_cadastro_produto(page):
    dsl = BasePage(page)
    dsl.abrir(cadastrar_produto_api_url)
    expect(page).to_have_title("Login")

@pytest.mark.order(2)
def test_fazer_login(page):
    dsl = BasePage(page)
    dsl.abrir(cadastrar_produto_api_url)
    expect(page).to_have_title("Login")
    dsl.realizar_login()
    expect(dsl.titulo_login).to_have_text("Controle de Produtos")

@pytest.mark.order(3)
def test_caso01(page):
    dsl = BasePage(page)
    dsl.abrir(cadastrar_produto_api_url)
    expect(page).to_have_title("Login")
    dsl.realizar_login()
    expect(dsl.titulo_login).to_have_text("Controle de Produtos")
    dsl.email.fill("")
    dsl.senha.fill("")
    dsl.btn_entrar1.click()
    expect(dsl.mensagem_login_erro).to_have_text("Informe e-mail e senha.")
    dsl.email.fill("admin@empresa.com")
    dsl.senha.fill("123")
    dsl.btn_entrar1.click()
    expect(dsl.mensagem_login_erro).to_have_text("E-mail ou senha inválidos.")
    dsl.email.fill("admin@empresa.com")
    dsl.senha.fill("123456")
    dsl.btn_entrar1.click()
    expect(dsl.mensagem_login_sucesso).to_have_text("Login realizado com sucesso.")

@pytest.mark.order(4)
def test_caso02(page):
    dsl = BasePage(page)
    dsl.abrir(cadastrar_produto_api_url)
    expect(page).to_have_title("Login")
    dsl.realizar_login()
    expect(dsl.titulo_login).to_have_text("Controle de Produtos")
    dsl.email.fill("")
    dsl.senha.fill("")
    dsl.btn_entrar1.click()
    expect(dsl.mensagem_login_erro).to_have_text("Informe e-mail e senha.")
    dsl.email.fill("admin@empresa.com")
    dsl.senha.fill("123")
    dsl.btn_entrar1.click()
    expect(dsl.mensagem_login_erro).to_have_text("E-mail ou senha inválidos.")
    dsl.email.fill("admin@empresa.com")
    dsl.senha.fill("123456")
    dsl.btn_entrar1.click()
    expect(dsl.mensagem_login_sucesso).to_have_text("Login realizado com sucesso.")

    expect(dsl.cadastro).to_have_text("Cadastros")
    expect(dsl.resultado_cadastro).to_have_text("3")