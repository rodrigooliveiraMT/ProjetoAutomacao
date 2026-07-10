import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Pericia_Medica:
    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)
        self.login = '1340'
        self.senha = 'fgh38a'

    # Declaração dos elementos
    @property
    def titulo_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.logo-name")

    @property
    def username(self):
        return self.driver.find_element(By.ID, "txtLogin")

    @property
    def password(self):
        return self.driver.find_element(By.ID, "txtSenha")
    
    @property
    def buttonLogin(self):
        return self.driver.find_element(By.ID, "btnLogin")
    
    @property
    def titulo_inicial(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Perícia Médica')]")))
    
    @property
    def acessarModuloConfiguracoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Configurações')]")))
    
    @property
    def acessarMenuGruposPermissoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='GrupoPermissoes.aspx']")))
    
    @property
    def validarTituloGrupoPermissoes(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Grupos - Permissões']")))

    @property
    def buttonNovoGrupoPermissoes(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "btnNovo")))
    
    @property
    def modalCadastroGruposPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "modalcadastronome1")))
    
    @property
    def campoNomeGrupo(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_txtNomeGrupo")))
    
    @property
    def buttonSalvarCadastroGrupo(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "btnSalvarDocumento")))
    
    @property
    def linhaGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'Automação')]")))
    
    # Editar Permissão de Grupo Permissões
    @property
    def buttonEditarGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_edit')]")))
    
    @property
    def buttonExcluirGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_remove')]")))
    
    @property
    def buttonPermissoesGrupoPermissao(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tr[td[contains(.,'Automação')]]//a[contains(@class,'editor_perm')]")))

    #-------------------------------------------------------------------------------------------------#
    #Validar mensagem de erro ou sucesso
    @property
    def toastTitulo(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-title")))

    @property
    def toastMensagem(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))
    
    def toastTituloOculto(self):
        return self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-title")))

    def toastMensagemOculto(self):
        return self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-message")))

    #Métodos
    def efetuar_login(self):
        self.titulo_login.is_displayed(), "Elemento não encontrado!"
        assert self.titulo_login.text == "Perícia Médica", f"Encontrado: '{self.titulo_login.text}'"
        self.username.send_keys(self.login)
        self.password.send_keys(self.senha)
        self.buttonLogin.click()
        self.titulo_inicial.is_displayed(), "Login falhou! Elemento não encontrado!"
        assert self.titulo_inicial.text == "Perícia Médica", f"Encontrado: '{self.titulo_inicial.text}'"