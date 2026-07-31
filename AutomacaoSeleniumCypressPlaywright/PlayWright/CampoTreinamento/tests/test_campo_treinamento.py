import pytest

from playwright.sync_api import expect

from pages.CampoTreinamentoPO import CampoTreinamentoPO

def test_button_simple(page):
    dsl = CampoTreinamentoPO(page)
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
    #page.pause()
    dsl.handle_alert(dsl.ifram1, "Frame OK!")
    dsl.handle_alert(dsl.button_alert, "Alert Simples")
    dsl.handle_confirm(dsl.button_confirm, "Confirm Simples", True, "Confirmado")
    dsl.handle_confirm(dsl.button_confirm, "Confirm Simples", False, "Negado")