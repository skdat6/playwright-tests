import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

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

