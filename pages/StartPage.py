from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage

class StartPage(AbstractPage):
    def __init__(self, page):
        self.url = "https://www.gov.uk/book-pupil-driving-test"
        self.startButton = page.locator('.govuk-button--start')

    def start(self):
        self.startButton.click()