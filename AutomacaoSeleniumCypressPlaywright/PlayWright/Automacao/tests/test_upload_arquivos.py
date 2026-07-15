from playwright.sync_api import expect

def test_importar_arquivo_unico(page):
    page.goto('https://www.transfernow.net/pt')
    page.get_by_role("button", name="Aceitar e Continuar").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Começar").click()
    file_chooser = fc_info.value
    file_chooser.set_files(r"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\upload_arquivos\arquivo01.txt")
    page.get_by_role("button", name="Criar um link").click()
    page.get_by_role("textbox", name="Seu e-mail").fill("teste@agenda.com.br")
    page.get_by_role("button", name="Obter um link").click()
    expect(page.get_by_text("Seu link está pronto!")).to_be_visible(timeout=50000)
    page.pause()

def test_importar_arquivo_multiplo(page):
    page.goto('https://www.transfernow.net/pt')
    page.get_by_role("button", name="Aceitar e Continuar").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Começar").click()
    file_chooser = fc_info.value
    file_chooser.set_files([r"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\upload_arquivos\arquivo01.txt",
                            r"C:\Automacao\ProjetoAutomacao\AutomacaoSeleniumCypressPlaywright\PlayWright\Automacao\stores\upload_arquivos\arquivo02.txt"])
    page.get_by_role("button", name="Criar um link").click()
    page.get_by_role("textbox", name="Seu e-mail").fill("teste@agenda.com.br")
    page.get_by_role("button", name="Obter um link").click()
    expect(page.get_by_text("Seu link está pronto!")).to_be_visible(timeout=50000)
    page.pause()