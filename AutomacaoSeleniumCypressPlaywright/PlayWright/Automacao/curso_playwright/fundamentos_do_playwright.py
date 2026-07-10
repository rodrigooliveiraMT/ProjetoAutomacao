import pytest

#get_by_role()
def test_get_by_role(page):
    page.goto("https://automationexercise.com")
    page.pause()
    page.get_by_role('link', name = "Signup / Login").click()
    page.get_by_role('button', name="Login").click()

def test_get_by_role1(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_role('button', name = 'Dropdown').nth(1).click() #nth(x) procura o primeiro elemento
    page.locator('#navebarColor01').get_by_role('button', name = 'Dropdown').nth(0).click()

#get_by_text()
def test_get_by_text(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    page.get_by_text('Full-Fledged practice website for Automation Engineers').first.click() # first seleciona o primeiro texto
    page.get_by_text('Full-Fledged practice website for Automation Engineers', exact = True).click()  # Procura pelo texto exato
    page.get_by_text('Full-Fledged practice website for Automation Engineers').click()

#get_by_placeholder()
def test_get_by_placeholder(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.get_by_placeholder('Name').fill('Jhon')
    page.get_by_placeholder('Email Address').nth(1).fill('jhon@gmail.com')

#get_by_label()
def test_get_by_label(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_label('Valid input', exact=True).fill('Hellow')
    page.get_by_label('Invalid input', exact=True).fill('Jhon')
    page.get_by_text("'Sorry, that username's taken. Try another?", exact = True)

#get_by_title()
def test_get_by_title(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.get_by_title('Automation Exercise - Signup / Login1').click()
    page.get_by_title('Blank').click()

def test_locator(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    page.locator('#accordian .panel-title').first.click() # O sistema vai procurar elemento classe "panel-title" dentro do elemento id "accordian"