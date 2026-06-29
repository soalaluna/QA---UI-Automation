import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://hayopnimanam.com/privacy-policy/")
    page.get_by_role("link", name="amoy.street@hayopnimanam.com").click()
    page.get_by_role("link", name="momentgroup@hayopnimanam.com").click()
