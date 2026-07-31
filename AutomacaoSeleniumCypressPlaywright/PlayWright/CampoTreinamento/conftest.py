import os
import pytest

STORAGE_FILE = "storage/state.json"


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 100,
        "args": ["--start-maximized"],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    args = {
        **browser_context_args,
        "no_viewport": True,
    }

    if os.path.exists(STORAGE_FILE):
        args["storage_state"] = STORAGE_FILE

    return args


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    yield

    page = item.funcargs.get("page")
    if page is None:
        return

    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    page.context.storage_state(path=STORAGE_FILE)