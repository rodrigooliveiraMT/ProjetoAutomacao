import pathlib
import time
import pytest

import pytest
from selenium import webdriver

from pages.cadastro_produtos_po import Cadastro_Produto
from pages.portal_integracao_po import Portal_Integracao
from pages.pericia_medica_po import Pericia_Medica
from pages.sisprevweb_po import Sisprev_Web
from pages.curso_selenium_po import LoginPage

from resources.portal_integracao_url import url_portal_integracao
from resources.pericia_medica_url import url_pericia_medica
from resources.siprevweb_url import url_sisprev_web
from resources.cadastro_produto_url import url_cadastro_produto
from resources.curso_selenium import base_url

URLS = {
    'portal_integracao': url_portal_integracao,
    'pericia_medica': url_pericia_medica,
    'sisprev_web': url_sisprev_web,
    'cadastro_produto': url_cadastro_produto
}

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    dsl = Cadastro_Produto(driver)
    driver.get(URLS["cadastro_produto"])
    yield driver, dsl
    time.sleep(2)
    driver.quit()

@pytest.fixture
def setup_portal_integracao(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    dsl = Portal_Integracao(driver)
    driver.get(URLS["portal_integracao"])
    yield driver, dsl
    time.sleep(2)
    driver.quit()

@pytest.fixture
def setup_pericia_medica(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    dsl = Pericia_Medica(driver)
    driver.get(URLS["pericia_medica"])
    yield driver, dsl
    time.sleep(2)
    driver.quit()

@pytest.fixture
def setup_sisprev_web(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    dsl = Sisprev_Web(driver)
    driver.get(URLS["sisprev_web"])
    yield driver, dsl
    time.sleep(2)
    driver.quit()

@pytest.fixture
def setup():
    pm = webdriver.Chrome()
    pm.maximize_window()
    dsl = LoginPage(pm)
    path = pathlib.Path(base_url) # pm.get(r"C:\Automação\Sites\Cadastro de Produtos\login.html")
    pm.get(path.as_uri())
    yield pm, dsl
    time.sleep(2)
    pm.quit()