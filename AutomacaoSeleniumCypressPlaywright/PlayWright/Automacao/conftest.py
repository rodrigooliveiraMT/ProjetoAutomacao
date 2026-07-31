import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "args": ["--start-maximized"]
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True # Abre o navegador em tela cheia
                # record_video_dir="videos" # Grava vídeos da execução dos testes
                # record_video_size={"width": 1280, "height": 720} # Define o tamanho do vídeo (opcional)
    }