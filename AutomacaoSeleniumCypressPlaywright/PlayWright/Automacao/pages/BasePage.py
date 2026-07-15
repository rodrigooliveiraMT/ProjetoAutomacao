class BasePage:
    def __init__(self, page):
        self.page = page

    def abrir_navegador(self, url, url1 = ''):
        self.page.goto(url or url1)