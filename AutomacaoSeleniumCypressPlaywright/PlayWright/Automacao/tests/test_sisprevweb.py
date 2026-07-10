from time import time

from pages.sisprevweb_po import LoginPage
from playwright.sync_api import expect
from resources.sisprevweb_url import sisprevweb_api_url


def test_verificar_login(page):
    dsl = LoginPage(page)
    dsl.abrir(sisprevweb_api_url)
    dsl.aguardar_elemento_visivel_e_enabled(dsl.txt_usuario)
    dsl.aguardar_elemento_visivel_e_enabled(dsl.txt_senha)
    dsl.aguardar_elemento_visivel_e_enabled(dsl.btn_login)
    dsl.realizar_login()