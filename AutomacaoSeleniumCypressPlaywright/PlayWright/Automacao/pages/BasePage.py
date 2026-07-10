class BasePage:
    def __init__(self, page):
        self.page = page

    def abrir_navegador(self, url):
        self.page.goto(url)