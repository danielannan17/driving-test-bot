import os, pytest
from playwright.sync_api import Page
from pages.StartPage import StartPage

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # print("beforeEach")
    # Go to the starting url before each test.
    page.goto(os.path.dirname(os.path.realpath(__file__)) + '/assets/AvailableTests.html')
    yield
    # print("afterEach")

def test_gets_all_available_tests(page: Page):
    pass
