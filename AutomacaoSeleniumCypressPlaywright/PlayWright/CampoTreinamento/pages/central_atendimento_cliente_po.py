from pages.BasePage import BasePage
from resources.central_atendimento_cliente import url_central_atendimento_cliente


class CentralAtendimentoClientePO(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador(url_central_atendimento_cliente)
        self.titulo = page.locator("#title")

        # Campos do formulário
        self.nome = page.locator("#firstName")
        self.sobrenome = page.locator("#lastName")
        self.email = page.locator("#email")
        self.telefone = page.locator("#phone")
        self.produto = page.locator("#product")
        self.radio_ajuda = page.get_by_text("Ajuda", exact=True)
        self.radio_elogio = page.get_by_text("Elogio", exact=True)
        self.radio_feedback = page.get_by_text("Feedback", exact=True)
        self.check_email = page.locator("#check").get_by_text("E-mail")
        self.check_telefone = page.locator("#check").get_by_text("Telefone")
        self.contato_email = page.locator("#email-checkbox")
        self.contato_telefone = page.locator("#phone-checkbox")
        self.mensagem = page.locator("#open-text-area")
        self.btn_arquivo = page.locator("#file-upload")
        self.btn_enviar = page.get_by_role("button", name="Enviar")
        self.privacidade = page.locator('[href="privacy.html"]')

        #mensagens de sucesso e erro
        self.mensagem_sucesso = page.locator(".success")
        self.mensagem_erro = page.locator(".error")

        # Título da nova guia
        self.titulo_nova_guia = "#title"

        self.tipos_contato = {
            "ajuda": self.radio_ajuda,
            "elogio": self.radio_elogio,
            "feedback": self.radio_feedback
        }


    def validar_title(self, texto_esperado):
        assert self.page.title() == texto_esperado

    def validar_texto(self, elemento, texto_esperado):
        assert elemento.inner_text() == texto_esperado, (
            f"Texto esperado: '{texto_esperado}', "
            f"mas foi encontrado: '{elemento.inner_text()}'"
        )

    def privacidade_link(self):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_role("link", name="Política de Privacidade").click()
            page1 = page1_info.value

    def uploads(self, elemento, arquivos):
        if isinstance(arquivos, str):
            arquivos = [arquivos]
        with self.page.expect_file_chooser() as fc_info:
            elemento.click()
        fc_info.value.set_files(arquivos)

    def validar_texto_nova_guia(self, elemento, seletor, texto_esperado):
        with self.page.context.expect_page() as nova_pagina:
            elemento.click()
        pagina = nova_pagina.value
        pagina.wait_for_load_state()
        texto = pagina.locator(seletor).inner_text().strip()
        assert texto == texto_esperado, (
            f"Texto esperado: '{texto_esperado}', "
            f"mas encontrado: '{texto}'"
        )
        return pagina


    def abrir_nova_guia(self, botao):
        with self.page.context.expect_page() as nova_pagina:
            botao.click()
        pagina = nova_pagina.value
        pagina.wait_for_load_state()
        return pagina

    def preencher_formulario(self, dados):
        self.nome.fill(dados["nome"])
        self.sobrenome.fill(dados["sobrenome"])
        self.email.fill(dados["email"])
        self.telefone.fill(dados["telefone"])
        self.produto.select_option(dados["produto"])
        self.tipos_contato[dados["tipo_contato"]].check()
        self.contato_email.set_checked(dados["contato_email"])
        self.contato_telefone.set_checked(dados["contato_telefone"])
        self.mensagem.fill(dados["mensagem"])
        self.uploads(self.btn_arquivo, dados["arquivo"])