from playwright.sync_api import Page
from resource.config.context import TARGET_URL

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_homepage(self):
        self.page.goto(TARGET_URL)