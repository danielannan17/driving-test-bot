from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage

class StartPage(AbstractPage):
    def __init__(self, page):
        self.categorySelect = page.locator('#businessBookingTestCategoryRecordId')
        self.weekPicker = page.locator('#weekBeginningDate')

        self.centreGroupSelect = page.locator('#testcentregroups')
        self.noDisabilitiesRadio = page.locator('#specialNeedsChoice-noneeds') # Has label - input name us specialNeedsChoice-noneeds
        self.startButton = page.locator('.govuk-button--start')
        self.submitButton = page.locator('input[type="submit"]')


    def select_car_category(self):
        self.categorySelect.select_option('TC-B')
        # Assert Car option is selected

    def select_test_centre_group_A(self):
        self.centreGroupSelect.select_option('label=Group A') # value is "145346"
        # Assert Group A option is selected

    def select_test_centre_group_B(self):
        self.centreGroupSelect.select_option('label=Group B') # value is "146213"
        # Assert Group A option is selected

    def select_week_beginning_date(self, date):
        # Check Date format is dd/mm/YYYY
        self.weekPicker.fill(date)

    def select_no_disabilities(self):
        self.noDisabilitiesRadio.click()