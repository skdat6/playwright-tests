import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
import logging

#####CONSTANTS
BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def login_logout(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()
    browser.close()

@pytest.fixture
def input_username():
    return 'standard_user'

@pytest.fixture
def input_password():
    return 'secret_sauce'

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger().setLevel(logging.INFO)
    config.addinivalue_line("markers", "log: mark the test function to show log in the report")

def pytest_collection_modifyitems(items, config):
    for item in items:
        if "log" in item.keywords:
            item.parent.session._fixturemanager.parsefactories(item)