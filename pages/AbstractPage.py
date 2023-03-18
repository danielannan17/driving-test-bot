from bs4 import BeautifulSoup

class AbstractPage:
    def __init__(self, page):
        self.page = page
        self.testUrl = self.__class__.__name__

    async def navigate(self):
        await self.page.goto(self.url)