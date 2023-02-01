from playwright.sync_api import Playwright, sync_playwright, expect


class LoginPageLocators:
    USERNAME_INPUT = '#user-name'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#login-button'

