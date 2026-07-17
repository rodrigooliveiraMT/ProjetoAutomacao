from playwright.sync_api import expect
from pages.upload_download_arquivos_po import UploadDownloadArquivo

def test_importar_arquivo_unico(page):
    dsl = UploadDownloadArquivo(page)
    page.pause()
    dsl.button_aceitar_continuar.click()
    dsl.uploads(dsl.button_comecar, r"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\upload_arquivos\arquivo01.txt")
    dsl.button_criar_link.click()
    dsl.input_email.fill("teste@teste.com")
    dsl.button_obter_link.click()
    expect(dsl.label_link_gerado, "Seu link está pronto!").to_be_visible(timeout=50000)

def test_importar_arquivo_multiplo(page):
    dsl = UploadDownloadArquivo(page)
    dsl.button_aceitar_continuar.click()
    dsl.uploads(dsl.button_comecar, [
        r"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\upload_arquivos\arquivo01.txt",
        r"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\upload_arquivos\arquivo02.txt"
    ])
    dsl.button_criar_link.click()
    dsl.input_email.fill("teste@agenda.com.br")
    dsl.button_obter_link.click()
    expect(dsl.label_link_gerado).to_be_visible(timeout=50000)
    page.pause()

def test_download(page):
    dsl = UploadDownloadArquivo(page)
    dsl.abrir_navegador('https://www.transfernow.net/pt/cld?utm_source=20260717vmRhPPJr')
    page.pause()
    dsl.downloads(dsl.button_baixar)