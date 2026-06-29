import re

import pytest
from playwright.sync_api import Page, expect

from pages.press_page import PRESS_LINKS, PressPage


@pytest.fixture
def press_page(page: Page) -> PressPage:
    """Navigate to the press page fresh for each test."""
    pp = PressPage(page)
    pp.goto()
    return pp


def test_press_page_header_content(press_page: PressPage) -> None:
    """Static header / featured press content on page 1."""
    expect(press_page.featured_date).to_be_visible()
    expect(press_page.featured_source).to_be_visible()
    expect(press_page.featured_image).to_be_visible()
    expect(press_page.featured_heading).to_be_visible()
    expect(press_page.read_more_link).to_be_visible()
    expect(press_page.press_features_label).to_be_visible()
    expect(press_page.pagination_summary).to_be_visible()


@pytest.mark.parametrize("link_name, page_number", PRESS_LINKS)
def test_press_page_links_visible(
    press_page: PressPage, link_name: str, page_number: int
) -> None:
    """Each press link is visible on its expected pagination page."""
    press_page.goto_pagination_page(page_number)
    expect(press_page.link(link_name)).to_be_visible()


@pytest.mark.parametrize("link_name, page_number", PRESS_LINKS)
def test_press_link_opens_in_new_tab(
    press_page: PressPage, link_name: str, page_number: int
) -> None:
    """Clicking a press link opens the source article in a new tab."""
    press_page.goto_pagination_page(page_number)
    with press_page.page.expect_popup() as popup_info:
        press_page.link(link_name).click()
    popup = popup_info.value
    popup.wait_for_load_state()
    expect(popup).to_have_url(re.compile(r"^https?://"))