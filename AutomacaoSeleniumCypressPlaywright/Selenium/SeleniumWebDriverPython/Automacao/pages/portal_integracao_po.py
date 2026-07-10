from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Portal_Integracao:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ELEMENTOS
    @property
    def texto_credenciais_login(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//strong[1][text() = "Digite suas informações de Acesso:"]')
    
    @property
    def campo_login(self) -> WebElement:
        return self.driver.find_element(By.ID, 'txtCpfAcesso')
    
    @property
    def campo_senha(self) -> WebElement:
        return self.driver.find_element(By.ID, 'txtSenhaAcesso')
    
    @property
    def btn_entrar(self) -> WebElement:
        return self.driver.find_element(By.ID, 'btnAcessar')
    
    @property
    def btn_novo_cadastro(self) -> WebElement:
        return self.driver.find_element(By.ID, 'lnkbtSolicitaSenha')
    
    @property
    def titulo_credenciais_invalidos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'lblTituloErro')))
    
    @property
    def mensagem_credenciais_invalidos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'lblMsgErro')))
    
    @property
    def btn_fechar_credenciais_invalidos(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'lnkFechar')))
    
    @property
    def titulo__novo_cadastro_invalidos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'lbTitutloSolicitaSenha')))
    
    @property
    def mensagem_novo_cadastro_invalidos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'lbMensagemSolicitaSenha')))
    
    @property
    def btn_fechar_novo_cadastro(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'lnkFecharSolicita')))
    
    @property
    def titulo_inicial(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'lblNomeSegurado')))
    
    @property
    def modulo_btn_sair(self) -> WebElement:
        return self.driver.find_element(By.ID, 'Topo1_btnSair')
    
    @property
    def modulo_enviar_arquivos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'pnlArquivos')))
    
    @property
    def enviar_arquivos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_lblTitulo')))
    
    @property
    def enviar_arquivos_campo_responsavel_pelo_envio(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_txt_UPLOAD_ARQUIVO_NOME_RESPONSAVEL')))
    
    @property
    def enviar_arquivos_email(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_txt_UPLOAD_ARQUIVO_EMAIL_RESPONSAVEL')))
    
    @property
    def enviar_arquivos_mes(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_ddl_UPLOAD_ARQUIVO_MES')))
    
    @property
    def enviar_arquivos_ano(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_ddl_UploadArquivoAno')))
    
    @property
    def enviar_arquivos_remover(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dz-remove')))
    
    @property
    def enviar_arquivos_anexar_arquivo(self) -> WebElement:
        return self.driver.find_element(By.ID, 'dZUpload')
    
    @property
    def btn_enviar_arquivos(self) -> WebElement:
        return self.driver.find_element(By.ID, 'btn_enviar')
    
    @property
    def modulo_carregar_arquivo(self) -> WebElement:
        return self.driver.find_element(By.ID, 'pnlConsultarArquivos')
    
    @property
    def titulo_carregar_arquivos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentFiltros_lblTitulo')))
    
    @property
    def carregar_arquivos_poder(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentFiltros_ddlPoder')))
    
    @property
    def carregar_arquivos_orgoes(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentFiltros_ddlOrgaos')))

    @property
    def carregar_arquivos_mes(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentFiltros_txt_UPLOAD_ARQUIVO_MES')))
    
    @property
    def carregar_arquivos_ano(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentFiltros_txt_UPLOAD_ARQUIVO_ANO')))

    @property
    def btn_carregar_arquivos(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentFiltros_btnCarregarArq')))
    
    @property
    def btn_consultar_arquivos_carregados(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentFiltros_btnConArqCarregado')))
    
    @property
    def carregar_arquivos_tipo_informacoes_oculto(self) -> bool:
        return self.wait.until(EC.invisibility_of_element_located((By.ID, 'ctl00_ContentFiltros_ddl_TIPO_UPLOAD_TIPO_ID')))
    
    @property
    def carregar_arquivos_tipo_informacoes_visivel(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentFiltros_ddl_TIPO_UPLOAD_TIPO_ID')))
    
    @property
    def carregar_arquivos_tabela_oculto(self) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'DataGridFixedHeader')))
    
    @property
    def carregar_arquivos_tabela_visivel(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//tr[2]/td[3][contains(text(), "INICIO EXPORTACAO DE TABELAS PELAS VIEWS")]')))
    
    @property
    def modulo_boletos(self) -> WebElement:
        return self.driver.find_element(By.ID, 'pnlBoleto')

    @property
    def titulo_boletos(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_lblCR')))
    
    @property
    def boletos_grupo_pagamento(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_ddlGrupoPagamento')))
    
    @property
    def boletos_mes_inicio(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_ddlMES_INI')))
    
    @property
    def boletos_ano_inicio(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_txtANO_INI')))
    
    @property
    def boletos_mes_fim(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_ddlMES_FIM')))
    
    @property
    def boletos_ano_fim(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentConteudo_txtANO_FIM')))
    
    @property
    def boletos_btn_consultar(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ContentConteudo_btnConsultar')))
    
    @property
    def boletos_tabela(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//td[2][contains(text(), "ALEXANDRA CASTRO")]')))

    @property
    def modulo_alterar_senha(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'pnlSenha')))
    
    @property
    def titulo_alterar_senha(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'lblCR')))
    
    @property
    def alterar_senha_campo_login(self) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((By.ID, 'txtuser')))
    
    @property
    def alterar_senha_campo_senha_atual(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'txtSenha')))
    
    @property
    def alterar_senha_campo_senha_nova(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'txtSenhaNova')))
    
    @property
    def alterar_senha_campo_confirmar_senha_nova(self) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'txtConfirmaSenhaNova')))
    
    @property
    def alterar_senha_btn_alterar(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'btnAlterar'))) 

    @property
    def anexar_arquivo(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//input[@type="file"]')
    
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