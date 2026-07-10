from playwright.sync_api import expect

from dicionario.pericia_medica.cadastro_pessoas import cadastro_pessoa
from pages.BasePage import BasePage
from resources.pericia_medica_url import pericia_medica_api_url


class PericiaMedica(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador(pericia_medica_api_url)
        self.login = page.locator('#txtLogin')
        self.page = page
        self.tituto_login = page.locator('.text-center.fw-bold.mb-2')
        self.login = page.locator('#txtLogin')
        self.senha = page.locator('#txtSenha')
        self.btn_login = page.locator('#btnLogin')
        self.alert = page.locator('.jconfirm-content')
        self.button_ok = page.locator('.btn.btn-default')
        self.titulo_inicial = page.get_by_role("heading", name="Perícia Médica")
        self.link_cadastrar_pessoas = page.get_by_role('link', name="Cadastrar Pessoas")
        self.label_consulta_pessoas = page.get_by_text('Consulta de Pessoas')
        self.button_novo_pessoas = page.locator('#btnNovo')
        self.link_dados_pessoais = page.get_by_role('link', name="Dados Pessoais")

        # CADASTRAR PESSOA
        self.campos = {
            "tipo_pessoa": {"locator": page.locator('#ContentPlaceHolder1_ddl_PESSOAS_TIPO_PESSOA'), "tipo": "select"},
            "nome": {"locator": page.locator("#ContentPlaceHolder1_txt_PESSOAS_NOME"),"tipo": "input"},
            "cpf": {"locator": page.locator("#ContentPlaceHolder1_txt_PESSOAS_CPF"), "tipo": "input"},
        }

    def preencher_campos(self, dados):
        for nome_campo, valor in dados.items():
            config = self.campos[nome_campo]
            locator = config["locator"]
            tipo = config["tipo"]
            if tipo == "input":
                locator.fill(str(valor))
            elif tipo == "select":
                locator.select_option(label=str(valor))
            elif tipo == "checkbox":
                if valor:
                    locator.check()
                else:
                    locator.uncheck()

    def preencher_campo(self, elemento, valor):
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.fill(valor)

    def clique_botao(self, elemento):
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.click()

    def realizar_login(self, usr_login = '', usr_senha = ''):
        expect(self.login).to_be_visible()
        expect(self.login).to_be_enabled()
        expect(self.senha).to_be_visible()
        expect(self.senha).to_be_enabled()
        expect(self.btn_login).to_be_visible()
        expect(self.btn_login).to_be_enabled()

        self.login.fill(usr_login)
        self.senha.fill(usr_senha)
        self.btn_login.click()

    def verificar_texto(self, elemento, texto):
        expect(elemento).to_be_visible()
        expect(elemento).to_have_text(texto)

    def selecionar_opcao(self, elemento, valor):
        elemento.select_option(valor)