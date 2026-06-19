from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.username = "#user-name"
        self.password = "#password"
        self.login_btn = "#login-button"

    def open(self):

        self.page.goto(
            "https://www.saucedemo.com"
        )

    def login(self, username, password):

        self.page.locator(
            self.username
        ).fill(username)

        self.page.locator(
            self.password
        ).fill(password)

        self.page.locator(
            self.login_btn
        ).click()