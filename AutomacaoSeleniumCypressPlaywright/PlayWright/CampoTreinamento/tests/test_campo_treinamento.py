import pytest

from playwright.sync_api import expect

from pages.CampoTreinamentoPO import CampoTreinamentoPO

def test_button_simple(page):
    dsl = CampoTreinamentoPO(page)
    dsl.button_simple.click()
    expect(dsl.button_simple).to_have_text("Obrigado!")
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
    dsl.dialogo_alert(dsl.ifram1, "Frame OK!")
    dsl.dialogo_alert(dsl.button_alert, "Alert Simples")
    dsl.dialogo_confirm(dsl.button_confirm, "Confirm Simples", "Confirmado", clicar_sim=True)
    dsl.dialogo_confirm(dsl.button_confirm, "Confirm Simples", "Negado", clicar_sim=False)
    dsl.dialogo_prompt(dsl.button_prompt, texto_prompt="Digite um numero", numero="42", clicar_prompt=True, texto_confirm="Era 42?", clicar_confirm=True, texto_alert=":D")
    dsl.dialogo_prompt(dsl.button_prompt, texto_prompt="Digite um numero", numero="42", clicar_prompt=True, texto_confirm="Era 42?", clicar_confirm=False, texto_alert=":(")
    dsl.dialogo_prompt(dsl.button_prompt, texto_prompt="Digite um numero", numero="42", clicar_prompt=False, texto_confirm="Era null?", clicar_confirm=True, texto_alert=":D")
    dsl.dialogo_prompt(dsl.button_prompt, texto_prompt="Digite um numero", numero="42", clicar_prompt=False, texto_confirm="Era null?", clicar_confirm=False, texto_alert=":(")