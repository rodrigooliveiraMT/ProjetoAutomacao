class BasePage:
    def __init__(self, page):
        self.page = page

    def abrir_navedor(self, url, url_base = ''):
        self.page.goto(url or url_base)