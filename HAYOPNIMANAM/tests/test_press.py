import re

import pytest
from playwright.sync_api import Page, expect

from locators.press_locators import PressPage, PRESS_LINKS


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
    expect(press_page.pagination_summary).to_be_visible()


@pytest.mark.parametrize("link_name, page_number", PRESS_LINKS)
def test_press_page_links_visible(
    press_page: PressPage, link_name: str, page_number: int
) -> None:
    """Each press link is visible on its expected pagination page."""
    press_page.goto_pagination_page(page_number)
    expect(press_page.link(link_name).first).to_be_visible()


@pytest.mark.parametrize("link_name, page_number", PRESS_LINKS)
def test_press_link_opens_in_new_tab(
    press_page: PressPage, link_name: str, page_number: int
) -> None:
    """Clicking a press link opens the source article in a new tab."""
    press_page.goto_pagination_page(page_number)
    link = press_page.link(link_name).first
    link.scroll_into_view_if_needed()
    press_page.page.wait_for_timeout(500)
    with press_page.page.expect_popup() as popup_info:
        link.click(force=True)
    popup = popup_info.value
    expect(popup).to_have_url(re.compile(r"^https?://"), timeout=10000)
    popup.close()


def test_debug_read_more_matches(press_page: PressPage) -> None:
    matches = press_page.page.locator("a").filter(has_text="read more").all()
    print(f"\n--- Found {len(matches)} <a> matching 'read more' on page 1 ---")
    for i, m in enumerate(matches):
        try:
            href = m.get_attribute("href")
            target = m.get_attribute("target")
            text = m.inner_text()[:60]
            visible = m.is_visible()
            print(f"[{i}] href={href!r} target={target!r} visible={visible} text={text!r}")
        except Exception as e:
            print(f"[{i}] error: {e}")

    print("\n--- press_page.read_more_link (exact role match) ---")
    try:
        rml = press_page.read_more_link
        print(f"href={rml.get_attribute('href')!r} target={rml.get_attribute('target')!r}")
    except Exception as e:
        print(f"error: {e}")


# ── Footer Tests ──────────────────────────────────────────────────────────────

def test_footer_instagram_link_present(press_page: PressPage) -> None:
    """Instagram link should be present in the DOM (may be hidden by animation)."""
    expect(press_page.footer_instagram).to_be_attached()


def test_footer_privacy_navigates(press_page: PressPage) -> None:
    """Privacy Policy footer link should navigate correctly."""
    press_page.footer_privacy.first.click()
    expect(press_page.page).to_have_url("https://hayopnimanam.com/privacy-policy/")


def test_footer_terms_navigates(press_page: PressPage) -> None:
    """Terms & Conditions footer link should navigate correctly."""
    press_page.footer_terms.first.click()
    expect(press_page.page).to_have_url("https://hayopnimanam.com/terms-conditions/")