from playwright.sync_api import expect
from pages.BasePage import BasePage

class CadastrarProdutoPo(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.credenciais = ["admin@admin.com", "admin"]
        self.email = page.locator("#email")
        self.senha = page.locator("#senha")
        self.btn_entrar = page.locator("#btn-entrar")
        self.titulo_login = page.locator("//h1[text()='Controle de Produtos']")
        self.btn_entrar1 = page.locator("//form[@id='login-form']//button[text()='Entrar']")
        self.mensagem_login_erro = page.locator("#login-error")
        self.mensagem_login_sucesso = page.locator("#login-success")
        self.cadastro = page.locator("//span[text()='Cadastros']")
        self.resultado_cadastro = page.locator("#kpi-total")

    def abrir(self, url):
        self.page.goto(url)

    def realizar_login(self, usr_login = None, usr_senha = None):
        expect(self.email).to_be_visible()
        expect(self.email).to_be_enabled()
        expect(self.senha).to_be_visible()
        expect(self.senha).to_be_enabled()
        expect(self.btn_entrar).to_be_visible()
        expect(self.btn_entrar).to_be_enabled()

        if usr_login is None:
            usr_login = self.credenciais[0]
        if usr_senha is None:
            usr_senha = self.credenciais[1]

        self.email.fill(usr_login)
        self.senha.fill(usr_senha)
        self.btn_entrar.click()
