import pytest

from playwright.sync_api import expect

from pages.CampoTreinamentoPO import CampoTreinamentoPO

@pytest.mark.order(1)
def test_validar_campos(page):
    dsl = CampoTreinamentoPO(page)
    dsl.alerta("Frame OK!", dsl.botao)

def test_preencher_campos(page):
    dsl = CampoTreinamentoPO(page)
    dsl.input_nome.fill("Teste")
    dsl.input_sobrenome.fill("Automatizado")
    dsl.radio_sexo_masculino.check()
    page.pause()

def test_button_simple(page):
    dsl = CampoTreinamentoPO(page)
    #page.pause()
    dsl.button_simple.click()
    dsl.validar_texto_input(dsl.button_simple, "Obrigado!")
    dsl_nova_guia1 = dsl.abrir_nova_guia(dsl.button_abri_popup)
    dsl_nova_guia1.locator("textarea").fill("Teste de preenchimento de textarea")
    dsl_nova_guia1.close()
    dsl_nova_guia2 = dsl.abrir_nova_guia(dsl.button_abri_popup_hard)
    dsl_nova_guia2.locator("textarea").fill("Teste de preenchimento de textarea")
    dsl_nova_guia2.close()
    dsl.button_resposta_demorada.click()
    expect(dsl.input_campo_novo).to_be_visible()
    dsl.input_campo_novo.fill("Campo preenchido após resposta demorada")
    dsl.alerta("Alert Simples", dsl.button_alert)
    dsl.confirmar(
        elemento=dsl.button_confirm,
        texto_confirmacao="Confirm Simples",
        aceitar_confirmacao=True,
        texto_alerta="Confirmado"
    )
    dsl.confirmar(
        elemento=dsl.button_confirm,
        texto_confirmacao="Confirm Simples",
        aceitar_confirmacao=False,
        texto_alerta="Negado1"
    )