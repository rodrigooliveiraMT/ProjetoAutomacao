import time
import pytest

from selenium import webdriver
from pages.portal_integracao_po import Portal_Integracao


def test_validar_titulo_login(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    assert "Portal Integração" in driver.title
    dsl.validar_texto(dsl.texto_credenciais_login, "Digite suas informações de Acesso:")
    dsl.validar_elementos(dsl.campo_login)
    dsl.validar_elementos(dsl.campo_senha)
    dsl.validar_elementos(dsl.btn_entrar)
    dsl.validar_elementos(dsl.btn_novo_cadastro)

def test_validar_acesso_login_invalido(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_credenciais_invalidos, 'Login ou Senha incorretos!')
    dsl.validar_texto(dsl.mensagem_credenciais_invalidos, 'Favor verifique as informações digitadas e tente novamente.')
    dsl.btn_fechar_credenciais_invalidos.click()

def test_validar_novo_cadastro(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.btn_novo_cadastro.click()
    dsl.validar_texto(dsl.titulo__novo_cadastro_invalidos, 'Como solicitar sua senha')
    dsl.validar_texto(dsl.mensagem_novo_cadastro_invalidos, 'Entre em contato com o Instituto para receber seus dados de acesso.')
    dsl.btn_fechar_novo_cadastro.click()

def test_efetuar_login(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_btn_sair.click()
    dsl.validar_texto(dsl.texto_credenciais_login, 'Digite suas informações de Acesso:')

def test_enviar_arquivos_validar_campos(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_enviar_arquivos.click()
    dsl.validar_texto(dsl.enviar_arquivos, 'Enviar Arquivos')
    dsl.enviar_arquivos_campo_responsavel_pelo_envio.clear()
    dsl.enviar_arquivos_email.clear()
    dsl.btn_enviar_arquivos.click()
    dsl.alerta('Atenção: Campo(s) Responsável pelo envio e E-mail são obrigatórios!')

def test_enviar_arquivos(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_enviar_arquivos.click()
    dsl.validar_texto(dsl.enviar_arquivos, 'Enviar Arquivos')
    dsl.preencher_campo(dsl.enviar_arquivos_campo_responsavel_pelo_envio, 'AUTOMAÇÃO')
    dsl.preencher_campo(dsl.enviar_arquivos_email, 'rodrigo.costa@agendaassessoria.com.br')
    dsl.selecionar_opcao(dsl.enviar_arquivos_mes, 'Janeiro')
    dsl.selecionar_opcao(dsl.enviar_arquivos_ano, '2026')
    dsl.anexar_arquivo.send_keys(anexo_arquivo)
    dsl.alerta('Atenção: Arquivo(s) enviado(s) com sucesso(s), Aguarde o término do carregamento!')
    dsl.anexar_arquivo.send_keys(anexo_arquivo)
    dsl.enviar_arquivos_remover.click()  # Remove o arquivo anexado
    dsl.validar_texto(dsl.enviar_arquivos_anexar_arquivo, 'Selecionar arquivos....')  # Verifica se o arquivo foi removido
    dsl.anexar_arquivo.send_keys(anexo_arquivo)  # Anexa novamente o arquivo
    dsl.btn_enviar_arquivos.click()
    dsl.alerta('Atenção: Arquivo(s) enviado(s) com sucesso(s), Aguarde o término do carregamento!')

def test_carregar_arquivos_enviados(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_carregar_arquivo.click()
    dsl.validar_texto(dsl.titulo_carregar_arquivos, 'Carregar Arquivos')
    dsl.selecionar_opcao_desabilitada(dsl.carregar_arquivos_poder, 'Executivo')
    assert dsl.carregar_arquivos_tipo_informacoes_oculto, f"Está Exibindo!"
    dsl.selecionar_opcao(dsl.carregar_arquivos_orgoes, 'GOVERNO DE SANTA CATARINA')
    assert dsl.carregar_arquivos_tipo_informacoes_visivel.is_displayed(), f"Não Está Exibindo!"
    dsl.selecionar_opcao(dsl.carregar_arquivos_mes, 'Janeiro')
    dsl.preencher_campo(dsl.carregar_arquivos_ano, '2026')
    dsl.selecionar_opcao(dsl.carregar_arquivos_tipo_informacoes_visivel, 'TODOS')
    assert dsl.carregar_arquivos_tabela_oculto, f"Está Exibindo!"
    dsl.btn_carregar_arquivos.click()
    dsl.alerta('Processamento em execução, você pode continuar utilizando o sistema, após conclusão do processo você receberá uma mensagem!')
    dsl.btn_consultar_arquivos_carregados.click()
    assert dsl.carregar_arquivos_tabela_visivel.is_displayed(), f"Não Está Exibindo!"

def test_boletos(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_boletos.click()
    dsl.validar_texto(dsl.titulo_boletos, 'Boletos de Arrecadação')
    dsl.selecionar_opcao(dsl.boletos_grupo_pagamento, 'ALEXANDRA CASTRO')
    dsl.selecionar_opcao(dsl.boletos_mes_inicio, 'Janeiro')
    dsl.preencher_campo(dsl.boletos_ano_inicio, '2020')
    dsl.selecionar_opcao(dsl.boletos_mes_fim, 'Dezembro')
    dsl.preencher_campo(dsl.boletos_ano_fim, '2026')
    dsl.boletos_btn_consultar.click()
    assert dsl.boletos_tabela.is_displayed(), f"Não Está Exibindo!"

def test_alterar_senha(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_alterar_senha.click()
    dsl.validar_texto(dsl.titulo_alterar_senha, 'Alterar Senha')
    assert dsl.alterar_senha_campo_login.get_attribute('value') == 'portalintegracao', f"Valor do campo Login é '{dsl.alterar_senha_campo_login.get_attribute('value')}', esperado 'portalintegracao'."
    dsl.alterar_senha_btn_alterar.click()
    dsl.alerta('É necessário o preenchimento de todos os campos para realizar a alteração!!!')
    dsl.preencher_campo(dsl.alterar_senha_campo_senha_atual, '123')
    dsl.preencher_campo(dsl.alterar_senha_campo_senha_nova, 'NovaSenha123@')
    dsl.preencher_campo(dsl.alterar_senha_campo_confirmar_senha_nova, 'NovaSenha123@')
    dsl.alterar_senha_btn_alterar.click()
    dsl.alerta('A senha atual está incorreta!!!')
    dsl.preencher_campo(dsl.alterar_senha_campo_senha_atual, '123@')
    dsl.preencher_campo(dsl.alterar_senha_campo_senha_nova, 'NovaSenha123@')
    dsl.preencher_campo(dsl.alterar_senha_campo_confirmar_senha_nova, 'NovaSenha123')
    dsl.alterar_senha_btn_alterar.click()
    dsl.alerta('A nova senha não confere com o conteúdo digitado em Confirma Senha!!!')
    dsl.preencher_campo(dsl.alterar_senha_campo_senha_atual, '123@')
    dsl.preencher_campo(dsl.alterar_senha_campo_senha_nova, '123@')
    dsl.preencher_campo(dsl.alterar_senha_campo_confirmar_senha_nova, '123@')
    dsl.alterar_senha_btn_alterar.click()
    dsl.alerta('Senha atualizada com sucesso!!!')
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')

def test_sair(setup_portal_integracao):
    driver, dsl = setup_portal_integracao
    dsl.campo_login.send_keys('portalintegracao')
    dsl.campo_senha.send_keys('123@')
    dsl.btn_entrar.click()
    dsl.validar_texto(dsl.titulo_inicial, 'AUTOMAÇÃO')
    dsl.modulo_btn_sair.click()
    dsl.validar_texto(dsl.texto_credenciais_login, 'Digite suas informações de Acesso:')