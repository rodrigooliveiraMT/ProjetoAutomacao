from pages.BasePage import BasePage
from resources.iframe_url import url_iframe


class iframe_po(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador(url_iframe)
        self.iframe = page.frame_locator("#iframeResult")
        self.inner_frame = self.iframe.frame_locator('[src="demo_iframe.htm"]')

    @property
    def label_texto(self):
        return self.inner_frame.locator("h1")
