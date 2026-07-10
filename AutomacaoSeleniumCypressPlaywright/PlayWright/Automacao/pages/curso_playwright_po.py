from resources.curso_playwright_url import curso_playwright_api_url1
from playwright.sync_api import expect
from pages.BasePage import BasePage
from playwright.sync_api import TimeoutError

class CursoPlaywirght(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.abrir_navegador(curso_playwright_api_url1)
        self.credenciais = ['teste@testeabcd.com', '123456789']
        self.button_home = page.get_by_role('link', name='Home')
        self.button_produtos = page.get_by_role("link", name="Products")
        self.button_compras = page.get_by_role("link", name="Cart")
        self.button_login = page.get_by_role("link", name="Signup / Login")
        self.input_email_login = page.locator("form").filter(has_text = "Login").get_by_placeholder("Email Address")
        self.input_senha_login = page.get_by_role("textbox", name = "Password")
        self.btn_login = page.get_by_role("button", name="Login")
        self.msg_dados_login_invalido = page.get_by_text("Your email or password is")
        self.texto_cadastrar_novo_usuario = page.get_by_text("New User Signup!", exact=True)
        self.input_nome_novo_usuario = page.locator('[data-qa="signup-name"]')
        self.input_email_novo_usuario = page.locator('[data-qa="signup-email"]')
        self.botao_signup = page.locator('[data-qa="signup-button"]')
        self.texto_informacoes_novo_usuario = page.get_by_text("Enter Account Information")
        self.radio_masculino_formulario = page.get_by_role("radio", name="Mr.")
        self.texto_nome_formulario = page.locator('[data-qa="name"]')
        self.texto_email_formulario = page.locator('[data-qa="email"]')
        self.input_senha_formulario = page.locator("#password")
        self.select_dia_formulario = page.locator("#days")
        self.select_mes_formulario = page.locator("#months")
        self.select_ano_formulario = page.locator("#years")
        self.checkbox_increverse_formulario = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.checkbox_ofertas_formulario = page.get_by_role("checkbox", name="Receive special offers from")
        self.input_primeiro_nome_formulario = page.get_by_role("textbox", name="First name *")
        self.input_segundo_nome_formulario = page.get_by_role("textbox", name="Last name *")
        self.input_nome_empresa_formulario = page.get_by_role("textbox", name="Company", exact=True)
        self.input_endereco_formulario = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.input_pais_formulario = page.get_by_label("Country *")
        self.input_estado_formulario = page.get_by_role("textbox", name="State *")
        self.input_cidade_formulario = page.get_by_role("textbox", name="City * Zipcode *")
        self.input_cep_formulario = page.locator("#zipcode")
        self.input_numero_telefone_formulario = page.get_by_role("textbox", name="Mobile Number *")
        self.button_criar_conta_formulario = page.get_by_role("button", name="Create Account")
        self.texto_conta_criada = page.get_by_text("Account Created!")
        self.button_continuar = page.get_by_role("link", name="Continue")
        self.texto_nome_usuario = page.locator("body")
        self.button_delete_usuario = page.get_by_role("button", name="Delete Account")
        self.button_delete_usuario1 = page.get_by_role("link", name="Delete Account")
        self.texto_conta_excluida = page.get_by_text("Account Deleted!")
        self.btn_close = page.locator("iframe[name=\"aswift_1\"]").content_frame.get_by_role("button", name="Close ad")

        self.btn_sair = page.get_by_role("link", name=" Logout")
        self.msg_login = page.get_by_role("heading", name="Login to your account")

    def acessar_home(self):
        self.button_home.click()

    def acessar_produtos(self):
        self.button_produtos.click()

    def acessar_compras(self):
        self.button_compras.click()

    def acessar_login(self):
        self.button_login.click()

    def click(self, elemento):
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.click()

    def fazer_login(self, email='', senha=''):
        self.input_email_login.fill(email or self.credenciais[0])
        self.input_senha_login.fill(senha or self.credenciais[1])
        self.btn_login.click()

    def button_close(self):
        self.btn_close.click()

    def fechar_popup_se_existir(self):
        try:
            self.btn_close().wait_for(state="visible", timeout=2000)
            self.button_close()
        except TimeoutError:
            pass