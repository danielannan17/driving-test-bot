from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage


class AvailableTestsPage(AbstractPage):
    def __init__(self, page, earliestDate):
        self.url = "https://www.gov.uk/book-pupil-driving-test"
        self.weekStart = None
        
        self.nextAvailableButton = page.locator('#searchForWeeklySlotsNextAvailable')
        self.errorMessage = page.locator('#searchResults .error')
        self.currentWeekText = page.locator('#searchResults > h3') # "Number of available tests between 10th Jul 2023 – 16th Jul 2023"
    
    def find_next_available_test(self):
        self.nextAvailableButton.click()
        # for each test centre in specific order
        # read .day.slotsavailable


    def get_week_start_date(self):
        pass
        # Read text from self.currentWeekText
        # Extract start date
        # Ensure start date is after earliestDate
