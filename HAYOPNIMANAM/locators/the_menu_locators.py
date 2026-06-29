import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://hayopnimanam.com/menu/?current_menu=menu-0")
    expect(page.get_by_role("img", name="hayop_Kinilaw_Hamachi-update-")).to_be_visible()
    expect(page.get_by_role("img", name="hayop_Manams-Wagyu-Watermelon")).to_be_visible()
    expect(page.get_by_role("img", name="hayop_MidnightAdobo_1-scaled-")).to_be_visible()
    expect(page.get_by_role("img", name="hayop_Drinks_Carousel-scaled.")).to_be_visible()
    expect(page.get_by_text("the menu", exact=True)).to_be_visible()
    expect(page.get_by_text("behind the taste")).to_be_visible()
    expect(page.get_by_role("heading", name="a la carte")).to_be_visible()
    expect(page.get_by_text("about the menu")).to_be_visible()
    expect(page.get_by_text("Filipino food as it is, at")).to_be_visible()
    expect(page.get_by_text("While the hayop pantry list")).to_be_visible()
    expect(page.locator("span").filter(has_text="a la carte")).to_be_visible()
    expect(page.get_by_text("main menu")).to_be_visible()
    expect(page.locator("span").filter(has_text="lunch sets")).to_be_visible()
    expect(page.get_by_text("tsibog combo")).to_be_visible()
    expect(page.locator("span").filter(has_text="dessert")).to_be_visible()
    expect(page.get_by_text("minatamis")).to_be_visible()
    expect(page.get_by_text("drinks")).to_be_visible()
    expect(page.get_by_role("paragraph").filter(has_text="inumin")).to_be_visible()
