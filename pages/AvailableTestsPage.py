import datetime
from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage
from utils import get_date_of_week, get_unique_xpath, get_start_date


class AvailableTestsPage(AbstractPage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.gov.uk/book-pupil-driving-test"
        self.weekStart = None
        
        self.nextAvailableButton = page.locator('#searchForWeeklySlotsNextAvailable')
        self.errorMessage = page.locator('#searchResults .error')
        self.currentWeekText = page.locator('#searchResults > h3') # "Number of available tests between 10th Jul 2023 – 16th Jul 2023"
    

    def get_available_dates(self):
            # Assertions use the expect API.
        soup = BeautifulSoup(self.page.locator('html').inner_html(), 'html.parser')
        availableDates = []
        for slot in soup.find_all(class_= 'day slotsavailable'):
            day = slot['headers'][0] # Return day of the week
            startDate = get_start_date(self.currentWeekText.inner_text())
            date = get_date_of_week(startDate, day) # calculate date based on headers and week beginning
            
            anchorTag = slot.find('a')
            testCentre = slot.find_previous_sibling(class_='testcentre') # find sibling with id = testcentre
            testCentreName = testCentre.find(class_='bold').text # Read text from first span tag to get centre
            # TODO Check if date and test centre match criterita 
            availableDates.append((testCentreName, date, anchorTag)) # Store all the information in an array
        return availableDates

    def reserve_best_test(self, availableDates):
        if len(availableDates) > 0:
            # TODO Sort array based on test centre and date
            print(get_unique_xpath(availableDates[0][2]))
            self.page.locator(get_unique_xpath(availableDates[0][2])).click() # Click first element anchor tag