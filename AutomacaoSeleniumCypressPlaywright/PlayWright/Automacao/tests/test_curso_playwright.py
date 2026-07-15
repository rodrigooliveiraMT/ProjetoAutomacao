import pytest

from pages.curso_playwright_po import CursoPlaywirght
from playwright.sync_api import expect

@pytest.mark.order(1)
def test_criar_cadastro(page):
    dsl = CursoPlaywirght(page)
    dsl.acessar_login()
    expect(dsl.texto_cadastrar_novo_usuario).to_be_visible()
    expect(dsl.texto_cadastrar_novo_usuario).to_have_text("New User Signup!")
    dsl.input_nome_novo_usuario.fill("Rodrigo Costa")
    dsl.input_email_novo_usuario.fill("teste@testeabcd.com")
    dsl.botao_signup.click()
    expect(dsl.texto_informacoes_novo_usuario).to_be_visible()
    expect(dsl.texto_informacoes_novo_usuario).to_have_text("Enter Account Information")
    dsl.radio_masculino_formulario.check()
    expect(dsl.texto_nome_formulario).to_have_value("Rodrigo Costa")
    expect(dsl.texto_email_formulario).to_have_value("teste@testeabcd.com")
    dsl.input_senha_formulario.fill("123456789")
    dsl.select_dia_formulario.select_option("16")
    dsl.select_mes_formulario.select_option("March")
    dsl.select_ano_formulario.select_option("1998")
    dsl.checkbox_increverse_formulario.check()
    dsl.checkbox_ofertas_formulario.check()
    dsl.input_primeiro_nome_formulario.fill("Automação")
    dsl.input_segundo_nome_formulario.fill("Software")
    dsl.input_nome_empresa_formulario.fill("Automação Sênior")
    dsl.input_endereco_formulario.fill("Rua Santos, Centro, 3900")
    dsl.input_pais_formulario.select_option("United States")
    dsl.input_estado_formulario.fill("Estado do Campinas")
    dsl.input_cidade_formulario.fill("Unbrela")
    dsl.input_cep_formulario.fill("78005300")
    dsl.input_numero_telefone_formulario.fill("66996990000")
    page.pause()
    dsl.button_criar_conta_formulario.click()
    expect(dsl.texto_conta_criada).to_have_text("Account Created!")
    dsl.button_continuar.click()
    dsl.fechar_popup_se_existir()
    expect(dsl.texto_nome_usuario).to_contain_text("Logged in as")

@pytest.mark.order(2)
def test_login_valido(page):
    dsl = CursoPlaywirght(page)
    dsl.acessar_login()
    dsl.fazer_login()
    expect(dsl.texto_nome_usuario).to_contain_text("Logged in as")
    dsl.click(dsl.btn_sair)
    expect(dsl.msg_login).to_contain_text("Login to your account")

@pytest.mark.order(3)
def test_login_invalido(page):
    dsl = CursoPlaywirght(page)
    dsl.acessar_login()
    dsl.fazer_login("teste@agenda.com", "123")
    expect(dsl.msg_dados_login_invalido).to_have_text("Your email or password is incorrect!")

@pytest.mark.order(4)
def test_excluir_cadastro(page):
    dsl = CursoPlaywirght(page)
    dsl.acessar_login()
    dsl.fazer_login()
    expect(dsl.texto_nome_usuario).to_contain_text("Logged in as")
    dsl.button_delete_usuario1.click()
    expect(dsl.texto_conta_excluida).to_have_text("Account Deleted!")

def test_carrinho(page):
    dsl = CursoPlaywirght(page)
    dsl.acessar_produtos()
    dsl.fechar_propaganda()
    dsl.adicionar_produto_ao_carrinho(dsl.card_produto1, dsl.botao_adicionar_carrinho1)
    dsl.click(dsl.btn_continuar)
    dsl.adicionar_produto_ao_carrinho(dsl.card_produto2, dsl.botao_adicionar_carrinho2)
    dsl.click(dsl.link_visualizar_carrinho)
    expect(dsl.text_carrinho).to_have_text("Shopping Cart")
    dsl.validar_carrinho(indice_produto=0,
                         descricao="Blue Top",
                         subdescricao="Women > Tops",
                         valor="Rs. 500",
                         valor_total="Rs. 500")
    dsl.validar_carrinho(indice_produto=1,
                         descricao="Men Tshirt",
                         subdescricao="Men > Tshirts",
                         valor="Rs. 400",
                         valor_total="Rs. 400")