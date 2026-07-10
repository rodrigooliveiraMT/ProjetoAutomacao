import time
import pytest

from selenium import webdriver

# ✅ Opção 1 — usando == False
# assert relembrar.is_displayed() == False, "Elemento deveria estar oculto!"

# ✅ Opção 2 — usando not (mais pythônico)
# assert not relembrar.is_displayed(), "Elemento deveria estar oculto!"

# ✅ Verifica que está visível
# assert relembrar.is_displayed() == True, "Elemento não está visível!"

def test_TC001_validarTitulos(setup_pericia_medica):
    pm, page = setup_pericia_medica
    assert pm.title == "Pericia | Login", f"Errado! Encontrado: '{pm.title}'"
    titulo = page.titulo_login.text
    assert titulo == "Perícia Médica", f"Errado! Encontrado: '{titulo}'"

def test_TC002_validarCamposLogin(setup_pericia_medica):
    pm, page = setup_pericia_medica
    page.buttonLogin.is_displayed(), "Não!"
    page.buttonLogin.is_enabled(), "Não!"
    page.buttonLogin.click()
    titulo2 = page.toastTitulo.text
    assert titulo2 == "Atenção!", f"Encontrado: '{titulo2}'"
    mensagem2 = page.toastMensagem.text
    assert mensagem2 == "Esse usuário não pertence ao grupo Perícia Médica!", f"Encontrado: '{mensagem2}'"
    assert page.toastTituloOculto(), "Atenção"
    assert page.toastMensagemOculto(), "Esse usuário não pertence ao grupo Perícia Médica!"

def test_TC003_efetuarLogin(setup_pericia_medica):
    pm, page = setup_pericia_medica
    page.efetuar_login()

def test_TC004_cadastrarGrupoPermissao(setup_pericia_medica):
    pm, page = setup_pericia_medica
    page.efetuar_login()
    page.acessarModuloConfiguracoes.click()
    page.acessarMenuGruposPermissoes.click()
    assert page.validarTituloGrupoPermissoes.text == "Grupos - Permissões", f"Encontrado: '{page.validarTituloGrupoPermissoes.text}'"
    page.buttonNovoGrupoPermissoes.click()
    assert page.modalCadastroGruposPermissao.text == "Cadastro de Grupos de Permissão", f"Encontrado: '{page.modalCadastroGruposPermissao.text}'"
    page.campoNomeGrupo.send_keys("Automação")
    page.buttonSalvarCadastroGrupo.click()
    assert page.toastTitulo.text == "Atenção!", f"Encontrado: '{page.toastTitulo.text}'"
    assert page.toastMensagem.text == "Grupo cadastrado com sucesso!", f"Encontrado: '{page.toastMensagem.text}'"
    assert page.linhaGrupoPermissao.text == "Automação", f"Encontrado: '{page.linhaGrupoPermissao.text}'"

def test_TC005_editarCadastroGrupoPermissao(setup_pericia_medica):
    pm, page = setup_pericia_medica
    page.efetuar_login()
    page.acessarModuloConfiguracoes.click()
    page.acessarMenuGruposPermissoes.click()
    assert page.validarTituloGrupoPermissoes.text == "Grupos - Permissões", f"Encontrado: '{page.validarTituloGrupoPermissoes.text}'"
    page.campoNomeGrupo.send_keys("Automação")