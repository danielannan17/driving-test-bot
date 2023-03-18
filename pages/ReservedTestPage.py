from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage


class ReserveTestPage(AbstractPage):
    def __init__(self, page, earliestDate):
        self.url = "https://www.gov.uk/book-pupil-driving-test"
        self.weekStart = None
        
        self.testType = page.locator('.orderSideBar tbody td[headers="slotType"]')
        self.testDateTime = page.locator('.orderSideBar tbody td[headers="dateTime"]')
        self.bookTestButton = page.locator('.orderSideBar a#bookReserved')
        self.cancelTestButton = page.locator('#progressBarCancelOrder')

    
