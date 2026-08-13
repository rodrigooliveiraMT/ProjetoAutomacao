import os
import pytest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STORAGE_FILE = BASE_DIR / "storage" / "state.json"

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False, # Abre o navegador na máquina local, mas não deve ficar ativo para pipeline CI/CD
        "slow_mo": 200, # Intervado de tempo de execução de um caso de teste para outro
        "args": ["--start-maximized"], # Abrir o navegador em tela cheia (Maximizado)
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    args = {
        **browser_context_args,
        "no_viewport": True, # Abre o navegador em tela cheia
                # record_video_dir="videos" # Grava vídeos da execução dos testes
                # record_video_size={"width": 1280, "height": 720} # Define o tamanho do vídeo (opcional)
    }

    if STORAGE_FILE.exists():
        args["storage_state"] = STORAGE_FILE
    return args