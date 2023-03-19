import os, pytest
from playwright.sync_api import Page
from pages.SearchPage import SearchPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # print("beforeEach")
    # Go to the starting url before each test.
    page.goto(os.path.dirname(os.path.realpath(__file__)) + '\\assets\\BookingCriteria.html')
    yield
    # print("afterEach")

def test_log_in(page: Page):
    # Assertions use the expect API.
    searchPage = SearchPage(page)
    searchPage.select_car_category()
    searchPage.select_no_disabilities()
    searchPage.select_test_centre_group_A()
    searchPage.select_week_beginning_date('07/02/2022')
