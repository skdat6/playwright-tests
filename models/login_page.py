from locators import LoginPageLocators


class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.query_selector(LoginPageLocators.USERNAME_INPUT).fill(username)

    def enter_password(self, password):
        self.page.query_selector(LoginPageLocators.PASSWORD_INPUT).fill(password)

    def click_login_button(self):
        self.page.query_selector(LoginPageLocators.LOGIN_BUTTON).click()

