from playwright.sync_api import expect
from pages.BasePage import BasePage

def test_validar_paginas_paralelos_home(page):
    dsl = BasePage(page)
    dsl.abrir_navegador("https://automationexercise.com")
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

def test_validar_paginas_paralelos_produtos(page):
    dsl = BasePage(page)
    dsl.abrir_navegador("https://automationexercise.com/products")
    expect(page.get_by_role("img", name="Website for practice")).to_be_visible()

def test_validar_paginas_paralelos_carrinho(page):
    dsl = BasePage(page)
    dsl.abrir_navegador("https://automationexercise.com/view_cart")
    expect(page.get_by_text("Home Shopping Cart")).to_be_visible()

def test_validar_paginas_paralelos_login(page):
    dsl = BasePage(page)
    dsl.abrir_navegador("https://automationexercise.com/login")
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()