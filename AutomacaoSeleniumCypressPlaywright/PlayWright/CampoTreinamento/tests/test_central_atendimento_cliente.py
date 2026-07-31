from playwright.sync_api import expect
import pytest
from pages.central_atendimento_cliente_po import CentralAtendimentoClientePO
from pages.politica_privacidade_po import PoliticaPrivacidadePO
from dicionario.central_atendimento_cliente import FORMULARIO_PADRAO

@pytest.mark.order(1)
def test_validar_titulo(page):
        dsl = CentralAtendimentoClientePO(page)
        dsl.validar_title("Central de Atendimento ao Cliente TAT")

@pytest.mark.order(2)
def test_validar_titulo_invalido(page):
        dsl = CentralAtendimentoClientePO(page)
        dsl.validar_texto(dsl.titulo, "ATENDIMENTO AO CLIENTE")

@pytest.mark.order(3)
def test_validar_envio_informacoes(page):
        dsl = CentralAtendimentoClientePO(page)
        dsl.btn_enviar.click()
        expect(dsl.mensagem_erro).to_be_visible()
        expect(dsl.mensagem_erro).to_have_text("Valide os campos obrigatórios!")

def test_preencher_formulario_enviar(page):
        dsl = CentralAtendimentoClientePO(page)
        dsl.preencher_formulario(FORMULARIO_PADRAO)
        dsl.btn_enviar.click()
        expect(dsl.mensagem_sucesso).to_be_visible()
        expect(dsl.mensagem_sucesso).to_have_text("Mensagem enviada com sucesso.")

def test_preencher_formulario_enviar_alterar_dado(page):
        dsl = CentralAtendimentoClientePO(page)
        dados = FORMULARIO_PADRAO.copy()
        dados["email"] = "teste@email.com"
        dsl.preencher_formulario(dados)
        dsl.btn_enviar.click()
        expect(dsl.mensagem_sucesso).to_be_visible()
        expect(dsl.mensagem_sucesso).to_have_text("Mensagem enviada com sucesso.")

def test_privacidade_link(page):
        dsl = CentralAtendimentoClientePO(page)
        nova_guia = dsl.abrir_nova_guia(dsl.privacidade)
        dsl = PoliticaPrivacidadePO(nova_guia)
        dsl.validar_texto(dsl.titulo, "CAC TAT - Política de Privacidade")
        dsl.validar_politica_privacidade([
            "Não salvamos dados submetidos no formulário da aplicação CAC TAT.",
            "Utilzamos as tecnologias HTML, CSS e JavaScript, para simular uma aplicação real.",
            "No entanto, a aplicação é um exemplo, sem qualquer persistência de dados, e usada para fins de ensino.",
            "Talking About Testing"
        ])