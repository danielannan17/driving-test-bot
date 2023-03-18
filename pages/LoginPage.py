import os
from bs4 import BeautifulSoup
from playwright.sync_api import Page
from pages.AbstractPage import AbstractPage
from dotenv import load_dotenv



class LoginPage(AbstractPage):
    load_dotenv()
    def __init__(self, page):
        self.url = "https://www.access.service.gov.uk/login/signin/creds"
        self.userField = page.locator("label[for='user_id']")
        self.passwordField = page.locator("label[for='password']")
        self.submitButton = page.locator('input[type="submit"]')

    def signIn(self):
        USERNAME = os.getenv('C')
        PASS = os.getenv('P')
        self.userField.fill(USERNAME)
        self.passwordField.fill(PASS)
        self.submitButton.click()