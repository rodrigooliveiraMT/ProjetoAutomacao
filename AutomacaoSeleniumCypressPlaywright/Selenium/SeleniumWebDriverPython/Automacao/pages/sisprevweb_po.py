from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sisprev_Web:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.usuario_padrao = "cqs.rodrigocosta"
        self.senha_padrao = "121212"

    @property
    def campo_login(self) -> WebElement:
        return self.driver.find_element(By.ID, "txtUSER")

    @property
    def campo_senha(self) -> WebElement:
        return self.driver.find_element(By.ID, "txtPassWord")

    @property
    def btn_acessar(self) -> WebElement:
        return self.driver.find_element(By.ID, "btnLogin")
    
    @property
    def titulo_inicial(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Inicial']")))
    
    @property
    def janela_aposentadoria_compulsoria(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "btnFecharInfoAlerta")))
    
    @property
    def menu_cadastros(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@title='Cadastros']/a")))
    
    @property
    def menu_pessoas(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@title='Pessoas']/a")))
    
    @property
    def menu_consulta(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@title='Consulta']/a")))

    @property
    def tela_consulta_pessoas(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_lblTituloPagina")))
    
    @property
    def btn_novo_pessoa(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentToolBar_btnNovo")))
    
    @property
    def validar_campo_cpf(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentCampos_TabContainer1_tabInformacoes_lbltextoCPF")))
    
    @property
    def cadpessoa_cpf(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentCampos_TabContainer1_tabInformacoes_txtPessoaCPF")))
    
    @property
    def cadpessoa_btn_avancar(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentToolBar_btnAvancaCPF")))
    
    @property
    def cadpessoa_insert_nome(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentCampos_TabContainer1_tabInformacoes_txtPessoaNome")))
    
    @property
    def cadpessoa_insert_sexo(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentCampos_TabContainer1_tabInformacoes_ddlPessoaSexo")))

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

    def preencher_campo(self, elemento, texto):
        elemento.clear() # Pequena pausa para garantir que o campo seja limpo
        elemento.send_keys(texto)

    def selecionar_opcao(self, elemento, texto):
        Select(elemento).select_by_visible_text(texto)

    def selecionar_opcao_desabilitada(self, elemento, texto):
        # Verifica se o <select> inteiro está desabilitado
        assert elemento.get_attribute('disabled') is not None, f"Está habilitado!"
        # Verifica se a opção correta está selecionada
        select = Select(elemento)
        assert select.first_selected_option.text.strip() == texto, f"Opção selecionada é '{select.first_selected_option.text}', esperado '{texto}'."

    def alerta(self, texto_esperado):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == texto_esperado
        alert.accept()

    def login(self, usuario = None, senha: str = None):
        self.wait.until(lambda d: self.campo_login.is_displayed() and self.campo_login.is_enabled())
        self.wait.until(lambda d: self.campo_senha.is_displayed() and self.campo_senha.is_enabled())
        self.wait.until(lambda d: self.btn_acessar.is_displayed() and self.btn_acessar.is_enabled())

        usuario = usuario or self.usuario_padrao
        senha = senha or self.senha_padrao

        self.campo_login.clear()
        self.campo_login.send_keys(usuario)

        self.campo_senha.clear()
        self.campo_senha.send_keys(senha)

        self.btn_acessar.click()