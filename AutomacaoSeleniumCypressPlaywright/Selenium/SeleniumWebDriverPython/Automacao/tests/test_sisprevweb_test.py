import time
import pytest

from selenium import webdriver
from resources.siprevweb_url import url_sisprev_web

def test_validar_titulo_login(setup_sisprev_web):
    driver, dsl = setup_sisprev_web
    assert 'SISPREV WEB - Sistema de Gestão de Regime Próprio de Previdência Social' in driver.title
    dsl.validar_elementos(dsl.campo_login)
    dsl.validar_elementos(dsl.campo_senha)
    dsl.validar_elementos(dsl.btn_acessar)

def test_validar_login_sem_credenciais(setup_sisprev_web):
    driver, dsl = setup_sisprev_web
    dsl.btn_acessar.click()
    dsl.alerta("Usuário não encontrado ou senha inválida!")

def test_validar_login_com_credenciais_invalidas(setup_sisprev_web):
    driver, dsl = setup_sisprev_web
    dsl.preencher_campo(dsl.campo_login, "usuario_invalido")
    dsl.preencher_campo(dsl.campo_senha, "senha_invalida")
    dsl.btn_acessar.click()
    dsl.alerta("Usuário não encontrado ou senha inválida!")

def test_validar_login_com_credenciais_validas(setup_sisprev_web):
    driver, dsl = setup_sisprev_web
    dsl.login()
    dsl.validar_elementos(dsl.titulo_inicial)

def test_cadastrar_novas_pessoas(setup_sisprev_web):
    driver, dsl = setup_sisprev_web
    dsl.login()
    dsl.validar_elementos(dsl.titulo_inicial)
    #dsl.janela_aposentadoria_compulsoria.click()
    dsl.menu_cadastros.click()
    dsl.menu_pessoas.click()
    dsl.menu_consulta.click()
    dsl.validar_elementos(dsl.tela_consulta_pessoas)
    dsl.btn_novo_pessoa.click()
    dsl.validar_elementos(dsl.validar_campo_cpf)
    dsl.preencher_campo(dsl.cadpessoa_cpf, "12345678900")
    dsl.cadpessoa_btn_avancar.click()