import pytest
from playwright.sync_api import expect

def test_get_by_role(page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name=" Signup / Login").click()
    page.get_by_role("button", name="Login").click()

def test_get_by_text(page):
    page.goto("https://automationexercise.com/login")
    expect(page.get_by_text("Login to your account")).to_be_visible()

def test_get_by_label(page):
    page.goto("https://automationexercise.com/login")
    page.get_by_label("Email Address").fill("usuario_invalido@teste.com")

def test_get_by_placeholder(page):
    page.goto("https://automationexercise.com/login")
    page.get_by_placeholder("Password").fill("senhaErrada123")

def test_get_by_title(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_title('Source Title').nth(1).click()

def test_locator(page):
    page.goto("https://automationexercise.com/view_cart")
    page.locator(".cart_quantity_delete").first.click()

def test_get_by_alt_text(page):
    page.goto("https://automationexercise.com/products")
    page.get_by_alt_text("Blue Top").click()

def test_locator_css(page):
    page.goto('https://automationexercise.com/')
    page.pause()
    page.locator('#accordian .panel-title').first.click()

def test_locator_xpath(page):
    page.goto('https://automationexercise.com/login')
    page.pause()
    page.locator('//*[@id="form"]/div/div/div[1]/div/form/button').click()

def test_goto(page):
    page.goto("https://automationexercise.com/", wait_until="networkidle") # Ir para a página da url