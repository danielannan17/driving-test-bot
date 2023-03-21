import os, pytest, datetime
from playwright.sync_api import Page, expect
from pages.AvailableTestsPage import AvailableTestsPage

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # print("beforeEach")
    # Go to the starting url before each test.
    page.goto(os.path.dirname(os.path.realpath(__file__)) + '/assets/AvailableTests.html')
    yield
    # print("afterEach")

def test_gets_all_available_tests(page: Page):
    availableTestsPage = AvailableTestsPage(page)
    availableTests = availableTestsPage.get_available_dates()
    assert availableTests[0][0] == 'Ballater'
    assert availableTests[0][1] == datetime.date(2023, 7, 10)
    availableTestsPage.reserve_best_test(availableTests)
