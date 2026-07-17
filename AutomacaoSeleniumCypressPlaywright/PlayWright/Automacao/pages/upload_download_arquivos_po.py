import os

from pages.BasePage import BasePage
from resources.upload_download_arquivos_url import upload_arquivos_api_url

class UploadDownloadArquivo(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador(upload_arquivos_api_url)

        #Upload
        self.button_aceitar_continuar = page.get_by_role("button", name="Aceitar e Continuar")
        self.button_comecar = page.get_by_role("button", name="Começar")
        self.button_criar_link = page.get_by_role("button", name="Criar um link")
        self.input_email = page.get_by_role("textbox", name="Seu e-mail")
        self.button_obter_link = page.get_by_role("button", name="Obter um link")
        self.label_link_gerado = page.get_by_text("Seu link está pronto!")

        #Download
        self.button_baixar = page.get_by_role("link", name="Baixar o arquivo")
        self.button_fechar_anuncio = page.locator(".continue-prompt-text")


    def uploads(self, elemento, arquivos):
        if isinstance(arquivos, str):
            arquivos = [arquivos]
        with self.page.expect_file_chooser() as fc_info:
            elemento.click()
        fc_info.value.set_files(arquivos)


    def downloads(self, elemento):
        with self.page.expect_download() as download_info:
            elemento.click()
        download = download_info.value
        caminho_final = fr"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\download_arquivos\{download.suggested_filename}"
        download.save_as(caminho_final)
        assert os.path.exists(caminho_final), "Arquivo não encontrado!"