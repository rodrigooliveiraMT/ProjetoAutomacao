import time
import pytest
import pathlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from selenium import webdriver
from pages.cadastro_produtos_po import Cadastro_Produto


def test_titulo_login(setup):
    driver, dsl = setup
    assert "Login" in driver.title

def test_validar_tela_login(setup):
    driver, dsl = setup
    dsl.validar_elementos(dsl.campo_email)
    dsl.validar_elementos(dsl.campo_senha)
    dsl.validar_elementos(dsl.btn_entrar)

def test_entrar_sem_informar_credenciais(setup):
    driver, dsl = setup
    dsl.btn_entrar.click()
    texto = dsl.mensagem_dados_invalidos.text
    dsl.validar_texto(dsl.mensagem_dados_invalidos, "Informe usuário e senha, os campos não podem ser brancos.")
    dsl.btn_close.click()

def test_efetuar_login_dados_invalidos(setup):
    driver, dsl = setup
    dsl.campo_email.send_keys('admin@gmail.com')
    dsl.campo_senha.send_keys('123')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.mensagem_dados_invalidos, 'E-mail ou senha inválidos')
    dsl.btn_close.click()
    dsl.campo_email.clear()
    dsl.campo_senha.clear()

def test_efetuar_login_dados_validos(setup):
    driver, dsl = setup
    dsl.campo_email.send_keys('admin@gmail.com')
    dsl.campo_senha.send_keys('admin')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'Controle de produtos')
    dsl.btn_criar.click()
    dsl.btn_criar.click()
    dsl.validar_texto(dsl.titulo_cadastro_produto, 'Produto'), f"{dsl.titulo_cadastro_produto.text}"
    dsl.btn_salvar.click()
    dsl.validar_mensagem(dsl.mensagem_dados_invalidos, 'Todos os campos são obrigatórios para o cadastro!')
    dsl.campo_codigo.send_keys('1010')
    dsl.campo_nome.send_keys('Celular')
    dsl.campo_quantidade.send_keys('10')
    dsl.campo_valor.send_keys('1.500,00')
    dsl.campo_data_cadastro.send_keys('02/04/2026')
    dsl.btn_salvar.click()
    dsl.btn_sair.click()
    dsl.validar_texto(dsl.linha_cadastro, 'Celular')