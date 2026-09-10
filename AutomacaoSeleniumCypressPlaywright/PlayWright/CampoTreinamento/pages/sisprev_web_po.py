from pages.BasePage import BasePage
from resources.sisprev_web_url import url_sisprev_web


class SisprevWebPO(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador(url_sisprev_web)
        self.logar = ["1340", "7qr85e"]
        self.login = page.locator("#txtUSER")
        self.senha = page.locator("#txtPassWord")
        self.btn_acessar = page.get_by_role("link", name="Acessar")
        self.titulo_modal_compulsoria = page.get_by_text("Direito a aposentadoria")
        self.btn_fechar_modal_compulsoria = page.get_by_role("button", name="Fechar")
        self.titulo_inicial = page.get_by_role("heading", name="Inicial")

        # Cadastrar Pessoas
        self.btn_cadastros = page.get_by_role("link", name="Cadastros ")
        self.btn_pessoas = page.get_by_role("link", name="Pessoas ")
        self.btn_consulta = page.get_by_role("link", name="Consulta")
        self.btn_nova_pessoa = page.get_by_role("link", name="Nova pessoa")
        self.btn_avancar = page.get_by_role("link", name="Avançar")
        self.txt_cpf = page.get_by_role("textbox", name="Informe os números do CPF (Ex")
        self.txt_nome = page.get_by_role("textbox", name="Informe nome e sobrenome", exact=True)
        self.opt_masculino = page.get_by_role("option", name="Masculino")
        self.txt_data_nascimento = page.get_by_role("textbox", name="Informe a data de nascimento")
        self.txt_nome_mae = page.get_by_role("textbox", name="Informe nome e sobrenome da M")
        self.btn_avancar_pessoa = page.get_by_role("link", name="Avançar")

    def validar_title(self, texto_esperado):
        assert self.page.title() == texto_esperado

    def preencher_login(self, login=None, senha=None):
        login = login or (self.logar[0] if len(self.logar) > 0 else "")
        senha = senha or (self.logar[1] if len(self.logar) > 1 else "")
        self.login.fill(login)
        self.senha.fill(senha)

    def dialog_preencher_login(self, botao_locator, texto_esperado):
        def alert(dialog):
            assert dialog.type == "alert"
            assert dialog.message == texto_esperado, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_esperado}"
            dialog.accept()
        self.page.once("dialog", alert)
        botao_locator.click()