import json

import pytest
import os

STORAGE_FILE = "storage/state.json"

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False, # Abrir navegador ao executar o(s) teste(s): False = abre o navegador, True = não abre o navegador
        "slow_mo": 1000,  # Dura 1 segundo entre cada ação
        "args": ["--start-maximized"], # Abrir o navegador em tela cheia(maximizado)
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    args = {
        **browser_context_args,
        "no_viewport": True,    # Abre o navegador em tela cheia
                # record_video_dir="videos" # Grava vídeos da execução dos testes
                # record_video_size={"width": 1280, "height": 720} # Define o tamanho do vídeo (opcional)
    }

    if os.path.exists(STORAGE_FILE):
        args["storage_state"] = STORAGE_FILE

    return args


@pytest.fixture(scope="session")
def context(browser, browser_context_args):
    context = browser.new_context(**browser_context_args)

    yield context

    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    context.storage_state(path=STORAGE_FILE)
    context.close()