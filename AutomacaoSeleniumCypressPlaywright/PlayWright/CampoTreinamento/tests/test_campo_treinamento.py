from tkinter import dialog
import pytest

from playwright.sync_api import expect

from pages.CampoTreinamentoPO import CampoTreinamentoPO

@pytest.mark.order(1)
def test_validar_campos(page):
    dsl = CampoTreinamentoPO(page)
    page.pause()
    dsl.alert("Frame OK!", dsl.botao)

def test_preencher_campos(page):
    dsl = CampoTreinamentoPO(page)
    dsl.input_nome.fill("Teste")
    dsl.input_sobrenome.fill("Automatizado")
    dsl.radio_sexo_masculino.check()

def test_button_simple(page):
    dsl = CampoTreinamentoPO(page)
    dsl.button_simple.click()
    expect(dsl.button_simple).to_have_text("Obrigado!")
    page.pause()