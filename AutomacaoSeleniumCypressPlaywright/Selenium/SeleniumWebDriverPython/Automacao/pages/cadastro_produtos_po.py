from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class Cadastro_Produto:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ELEMENTOS
    @property
    def titulo_login(self):
        return self.driver.find_element(By.TAG_NAME, 'h1')
    
    @property
    def campo_email(self):
        return self.driver.find_element(By.ID, 'email')
    
    @property
    def campo_senha(self):
        return self.driver.find_element(By.ID, 'senha')
    
    @property
    def btn_entrar(self) -> WebElement:
        return self.driver.find_element(By.ID, 'btn-entrar')
    
    @property
    def mensagem_dados_invalidos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'mensagem')))
    
    @property
    def btn_close(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
    
    @property
    def titulo_inicial(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'navbar-brand')))
    
    @property
    def btn_criar(self) -> WebElement:
        return self.driver.find_element(By.ID, 'btn-adicionar')
    
    @property
    def titulo_cadastro_produto(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))

    @property
    def campo_codigo(self) -> WebElement:
        return self.driver.find_element(By.ID, 'codigo')
    
    @property
    def campo_nome(self) -> WebElement:
        return self.driver.find_element(By.ID, 'nome')
    
    @property
    def campo_quantidade(self) -> WebElement:
        return self.driver.find_element(By.ID, 'quantidade')
    
    @property
    def campo_valor(self) -> WebElement:
        return self.driver.find_element(By.ID, 'valor')
    
    @property
    def campo_data_cadastro(self) -> WebElement:
        return self.driver.find_element(By.ID, 'data')
    
    @property
    def btn_salvar(self) -> WebElement:
        return self.driver.find_element(By.ID, 'btn-salvar')
    
    @property
    def btn_sair(self) -> WebElement:
        return self.driver.find_element(By.ID, 'btn-sair')
    
    @property
    def linha_cadastro(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//tbody/tr/td[2][text()="Celular"]')
    
    # MÉTODOS
    def validar_elementos(self, elemento):
        assert elemento.is_displayed(), f"Elemento: {elemento}"
        assert elemento.is_enabled(), f"Elemento: {elemento}"

    def validar_texto(self, elemento, mensagem_esperada):
        texto = elemento.text.strip()
        assert texto == mensagem_esperada, f"{texto}"

    def validar_mensagem(self, elemento, mensagem_esperada):
        texto = elemento.text.strip()
        assert texto == mensagem_esperada, f"{texto}"