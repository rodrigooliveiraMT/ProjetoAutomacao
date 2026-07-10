from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common .keys import Keys
from selenium.webdriver.remote.utils import dump_json
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.usuario = "adm@gmail.com"
        self.senha = "123"

    # ============================================================================================================
    # Declaração dos elementos (Modelos abaixo)
    # ============================================================================================================
    #@property ---> Usar (@property) para transformar métodos em propriedades (sem parênteses)
    
    @property
    def validar_titulo_login(self):
        return self.driver.find_element(By.TAG_NAME, 'h1')
    
    @property
    def campo_email(self):
        return self.driver.find_element(By.ID, 'email')
    
    @property
    def campo_senha(self):
        return self.driver.find_element(By.ID, 'senha')
    
    @property
    def btn_entrar(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'btn-entrar')))
    
    @property
    def validar_credenciais(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'mensagem')))
    
    @property
    def titulo_cadastro(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-brand")))

    @property
    def botao_cadastrar_produtos(self):
        return self.driver.find_element(By.ID, "btn-adicionar")
    
    @property
    def titulo_grid_produtos(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-title")))
    
    @property
    def acessarModuloConfiguracoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "liConfiguracoes")))

    @property
    def btn_close(self):
        return self.driver.find_element(By.CLASS_NAME, 'close')
    
    @property
    def titulo_pagina_inicial(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Controle de produtos")]')))

    
        
    # ============================================================================================================
    #Métodos
    # ============================================================================================================
    def validar_titulo(self, titulo_esperado):
        titulo_atual = self.driver.title   # ✅ já é string, sem .text (Direto, sem .text)
        assert titulo_atual == titulo_esperado, f"Encontrado: '{titulo_atual}'"

    def assert_valida(self, elemento, mensagem_esperada):
        mensagem = elemento.text # ✅ self.driver.find_element(...).text - texto visível de um WebElement Com .text
        assert mensagem == mensagem_esperada, f"Encontrado: '{mensagem}'"
    
    def acessar_site(self):
        self.campo_email().send_keys(self.usuario)
        self.campo_senha().send_keys(self.senha)
        self.btn_entrar().click()

    def validar_texto(self, elemento_uf, texto_esperado):
        elemento = elemento_uf()
        texto = elemento.text.strip()
        assert texto == texto_esperado, f"Texto Exibido: {texto}"

    def validar_campo(self, elemento_uf):
        try:
            elemento = elemento_uf()
            return elemento.is_displayed() and elemento.is_enabled()
        except Exception:
            return False