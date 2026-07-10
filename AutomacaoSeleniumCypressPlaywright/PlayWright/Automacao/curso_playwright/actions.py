import pytest
from playwright.sync_api import expect

def test_click(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    page.get_by_role('link', name="Website for automation").click(button='right')
    page.get_by_role('link', name="Website for automation").click(position={'x': 10, 'y': 10})
    page.get_by_role('link', name="Website for automation").click(modifiers=['Control'])

def test_click_primary(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_role('button', name="Primary").nth(1).click(force=True) # Força clicar no elemento mesmo que está desabilitado ou invisivel

def test_fill(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.get_by_role("textbox", name="Name").fill('Rodrigo')
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill('teste@gmail.com')
    page.get_by_role("button", name="Signup").click()

def test_check_uncheck(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_role("checkbox", name="Default checkbox").check() #Marcar checkbox
    page.get_by_role("checkbox", name="Checked checkbox").uncheck() #Desmarcar checkbox

def test_select_option(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_label('Example select').select_option('2') #Selecionar uma única opção
    page.get_by_label('Example multiple select').select_option(['3', '5']) #Selecionar múltiplas opções

def test_press(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_placeholder('name@example.com').fill('teste@gmail.com')
    page.get_by_placeholder('name@example.com').press('Tab') #Pula para linha de baixo
    page.keyboard.type('123') #Preenche o campo sem declarar o elemento. Simula o teclado
    page.get_by_role('textbox', name="Example textarea").fill('teste teste teste') # Preencher campo
    page.get_by_role('textbox', name="Example textarea").press('Control+A') # Selecionar todos os texto do campo
    page.get_by_role('textbox', name="Example textarea").press('Control+C') # Copiar texto selecionado
    page.get_by_placeholder('name@example.com').clear() # Limpar campo
    page.get_by_placeholder('name@example.com').press('Control+V') # Colar texto copiado no campo

def test_type(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_role('textbox', name = 'Example textarea').type('Lorem Ipsum is simply dummy text of the printing and typesetting industry.', delay=50) # delay é o tempo que o sistema leva para digitar cada caracter

def test_hover(page):
    page.goto('https://automationexercise.com')
    page.pause()
    page.locator('.single-products:visible').filter(has_text = 'Madame Top For Women').hover() # O filter busca qualquer elemento que possui um determinado texto ---> :visible busca somente elementos visível na tela ---> hover mantém somente a seta do mouse sobre o elemento
    page.locator("div:nth-child(9) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn").click()

def test_dblblick(page):
    page.goto('https://automationexercise.com')
    page.pause()
    page.locator('.login-form h2').dblclick()

def test_expect(page):
    page.goto('https://automationexercise.com/')
    page.pause()
    page.locator('.single-products:visible').filter(        has_text='Madame Top For Women').hover()  # O filter busca qualquer elemento que possui um determinado texto ---> :visible busca somente elementos visível na tela ---> hover mantém somente a seta do mouse sobre o elemento
    page.locator(        "div:nth-child(9) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn").click()
    expect(page.locator('#cartModal')).to_contain_text('Your product has been added to cart.', timeout=10000)
    expect(page.get_by_role('button', name="Continue Shopping")).to_be_visible()
    expect(page.get_by_role('button', name="Continue Shopping")).to_be_enabled()
    page.get_by_role('button', name="Continue Shopping").click()
    expect(page.locator('#cartModal')).not_to_be_visible()