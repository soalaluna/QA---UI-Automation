import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.pldtglobal.com/en/enterprise/pgc-data-centers-and-hyperscale-integration")
    page.get_by_role("link", name="Enterprise", exact=True).click()
    expect(page.get_by_role("heading", name="Data Centers and Hyperscale")).to_be_visible()
    expect(page.get_by_text("Powered by the PLDT Group’s")).to_be_visible()
    expect(page.locator("section").filter(has_text="Back to").locator("img")).to_be_visible()
    page.get_by_role("link", name="Learn More").click()
    page.goto("https://www.pldtglobal.com/en/enterprise/pgc-data-centers-and-hyperscale-integration")
