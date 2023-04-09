import datetime
from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage
from utils import get_date_of_week, get_unique_xpath, get_start_date

class ConfirmReservePage(AbstractPage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.gov.uk/book-pupil-driving-test"
        self.weekStart = None

        self.nextAvailableButton = page.locator('#searchForWeeklySlotsNextAvailable')
        self.errorMessage = page.locator('#searchResults .error')
        self.currentWeekText = page.locator('#searchResults > h3') # "Number of available tests between 10th Jul 2023 – 16th Jul 2023"

    def get_tests(self):
            # Assertions use the expect API.
        soup = BeautifulSoup(self.page.locator('html').inner_html(), 'html.parser')
        table = soup.find("table", {"id": "displaySlot"})

        # Create an empty list to store the data
        data = []

        # Loop through each row in the table (skipping the header row)
        for row in table.find_all("tr")[1:]:
            # Create a dictionary to store the data for this row
            row_data = {}

            # Extract the data from each column in the row
            columns = row.find_all("td")
            row_data["Test type"] = columns[0].text.strip()
            row_data["Time"] = columns[1].text.strip()
            row_data["Price"] = columns[2].text.strip()
            row_data["Tests available"] = columns[3].text.strip()
            row_data["Last date to cancel"] = columns[4].text.strip()
            row_data["anchorTag"] = columns[5].find('a')
            # Append the row data to the list of data
            data.append(row_data)
        return data

    def reserve_best_test(self, tests):
        if len(tests) > 0:
            # TODO Sort array based on test centre and date
            print(get_unique_xpath(tests[0]['anchorTag']))
            self.page.locator(get_unique_xpath(tests[0]['anchorTag'])).click() # Click first element anchor tag