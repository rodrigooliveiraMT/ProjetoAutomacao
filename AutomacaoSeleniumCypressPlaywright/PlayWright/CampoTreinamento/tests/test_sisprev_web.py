from playwright.sync_api import expect
from pages.sisprev_web_po import SisprevWebPO


def test_validar_titulo(page):
    dsl = SisprevWebPO(page)
    dsl.validar_title("SISPREV WEB - Sistema de Gestão de Regime Próprio de Previdência Social")

def test_validar_login_sem_dados(page):
    dsl = SisprevWebPO(page)
    dsl.dialog_preencher_login(dsl.btn_acessar, "Usuário não encontrado ou senha inválida!")

def test_validar_login_com_dados_invalidos(page):
    dsl = SisprevWebPO(page)
    dsl.preencher_login("usuario_invalido", "senha_invalida")
    dsl.dialog_preencher_login(dsl.btn_acessar, "Usuário não encontrado ou senha inválida!")

def test_validar_login_com_dados_validos(page):
    dsl = SisprevWebPO(page)
    dsl.preencher_login()
    dsl.btn_acessar.click()
    expect(dsl.titulo_modal_compulsoria).to_have_text("Direito a aposentadoria compulsória")
    dsl.btn_fechar_modal_compulsoria.click()
    expect(dsl.titulo_inicial).to_have_text("Inicial")
    page.pause()