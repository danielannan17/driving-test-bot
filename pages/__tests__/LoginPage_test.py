import os, pytest
from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # print("beforeEach")
    # Go to the starting url before each test.
    page.goto(os.path.dirname(os.path.realpath(__file__)) + '\\assets\\LoginPage.html')
    yield
    # print("afterEach")

def test_log_in(page: Page):
    # Assertions use the expect API.
    USERNAME = os.getenv('C')
    PASS = os.getenv('P')
    loginPage = LoginPage(page)
    loginPage.fill()
    expect(loginPage.userField).to_have_value(USERNAME)
    expect(loginPage.passwordField).to_have_value(PASS)
