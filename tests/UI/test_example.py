from playwright.sync_api import expect
from src.pages.navigation_page import NavigationPage


def test_homepage_title(page):
    nav = NavigationPage(page)
    nav.navigate_to_homepage()
    expect(page).to_have_title("Writing tests | Playwright Python")
