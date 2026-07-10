
import time
from typing import Any
import pytest_html

from selenium import webdriver
from inicializacao import setup

def test_validar_titulo(setup):
    driver, dsl = setup
    assert "Login" in driver.title, f"Exibido: {driver.title}"
    dsl.validar_texto(dsl.validar_titulo_login, "Login")
    assert dsl.validar_campo(dsl.campo_email), f"Apresentou erro!"
    assert dsl.validar_campo(dsl.campo_senha), f"Apresentou erro!"
    assert dsl.validar_campo(dsl.btn_entrar), f"Apresentou erro!"

def test_validar_credenciais_campos_vazios(setup):
    driver, dsl = setup
    dsl.btn_entrar().click()
    dsl.validar_texto(dsl.validar_credenciais, "Informe usuário e senha, os campos não podem ser brancos.")
    dsl.btn_close().click()
    assert not dsl.btn_close().is_displayed(), "O botão de fechar não foi ocultado."

def test_validar_credenciais_dados_invalidos(setup):
    driver, dsl = setup
    dsl.campo_email().send_keys("usuario_invalido")
    dsl.campo_senha().send_keys("senha_invalida")
    dsl.btn_entrar().click()
    dsl.validar_texto(dsl.validar_credenciais, "E-mail ou senha inválidos")
    dsl.btn_close().click()
    assert not dsl.btn_close().is_displayed(), "O botão de fechar não foi ocultado."

def test_validar_credenciais_dados_validos(setup):
    driver, dsl = setup
    dsl.campo_email().send_keys("admin@admin.com")
    dsl.campo_senha().send_keys("admin")
    dsl.btn_entrar().click()
    dsl.validar_texto(dsl.titulo_pagina_inicial, "Controle de produtos")

time.sleep(2)