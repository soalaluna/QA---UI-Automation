import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://hayopnimanam.com/terms-conditions/")
    page.get_by_role("link", name="amoy.street@hayopnimanam.com").click()
    page.get_by_role("link", name="momentgroup@hayopnimanam.com").click()
