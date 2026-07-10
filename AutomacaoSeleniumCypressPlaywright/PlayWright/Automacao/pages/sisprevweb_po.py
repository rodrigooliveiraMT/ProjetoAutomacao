from playwright.sync_api import expect
from pages.BasePage import BasePage

class SisprevWeb(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.login = ["1340", "lmn682"]
        self.txt_usuario = page.locator("#txtUSER")
        self.txt_senha = page.locator("#txtPassWord")
        self.btn_login = page.locator("#btnLogin")
        self.fechar_janela_compulsoria = page.locator("#btnFecharInfoAlerta")

    def abrir(self, url):
        self.page.goto(url)

    def aguardar_elemento_visivel_e_enabled(self, elemento):
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()

    def realizar_login(self, usr_login=None, usr_senha=None):
        if usr_login is None:
            usr_login = self.login[0]
        if usr_senha is None:
            usr_senha = self.login[1]

        self.txt_usuario.fill(usr_login)
        self.txt_senha.fill(usr_senha)
        self.btn_login.click()

    def validar_texto(self, elemento, texto):
        expect(elemento).to_have_text(texto)

    def fechar_popup_compulsorio(self):
        popup = self.fechar_janela_compulsoria
        if popup.is_visible():
            popup.click()

    def pausar(self):
        self.page.pause()

    def pausa_temporaria(self):
        self.page.wait_for_timeout(10000)

    @property
    def titulo_inicial(self):
        return self.page.locator("//h2[text()='Inicial']")

    def validar_pagina_inicial(self):
        expect(self.titulo_inicial).to_be_visible()