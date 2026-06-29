"""
Test suite for the Press page - momentgroup.ph/press
Tests behavior (filter works, articles have valid links, footer works)
rather than clicking every individual article — leaner and more stable
as new press articles get added over time.
"""

import pytest
from playwright.sync_api import Page, expect
from locators.press_locators import PressLocators as PL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_press(page: Page):
    page.goto(PL.BASE_URL, wait_until="domcontentloaded", timeout=60000)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.get_by_role("link", name="Press").click()
    page.wait_for_url("**/press/**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestPressNavigation:

    def test_press_page_loads(self, page: Page):
        expect(page).to_have_url(PL.PRESS_URL)

    def test_press_heading_visible(self, page: Page):
        expect(page.locator(PL.PRESS_HEADING)).to_be_visible()


# ── Brand Filter Tests ────────────────────────────────────────────────────────

class TestPressBrandFilter:

    def test_filter_dropdown_visible(self, page: Page):
        expect(page.get_by_role("combobox")).to_be_visible()

    def test_filter_by_manam(self, page: Page):
        """Selecting a brand should update the dropdown value."""
        page.get_by_role("combobox").select_option("Manam")
        expect(page.get_by_role("combobox")).to_have_value(re_or_text("Manam"))

    def test_filter_by_hayop(self, page: Page):
        page.get_by_role("combobox").select_option("hayop")
        expect(page.get_by_role("combobox")).to_have_value(re_or_text("hayop"))

    def test_filter_reset_to_all_brands(self, page: Page):
        """Resetting filter back to 'All Brands' should work."""
        page.get_by_role("combobox").select_option("Manam")
        page.get_by_role("combobox").select_option("All Brands")
        expect(page.get_by_role("combobox")).to_have_value(re_or_text("All Brands"))


def re_or_text(text: str):
    """Helper since select_option value attributes may differ from visible label."""
    import re
    return re.compile(text, re.IGNORECASE)


# ── Article Link Tests ────────────────────────────────────────────────────────

class TestPressArticles:

    def test_articles_have_valid_links(self, page: Page):
        """All visible article links should have a valid, non-empty href."""
        links = page.locator(PL.ARTICLE_LINKS)
        count = links.count()
        assert count > 0, "No article links found on the press page"
        for i in range(min(count, 20)):  # cap check at first 20 to keep test fast
            href = links.nth(i).get_attribute("href")
            assert href and href.strip() != "", f"Article {i} has an empty href"

    def test_first_article_opens_popup(self, page: Page):
        """Sample test: clicking the first article should open a new tab."""
        with page.expect_popup() as popup_info:
            page.locator(PL.ARTICLE_LINKS).first.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()


# ── Contact Tests ─────────────────────────────────────────────────────────────

class TestPressContact:

    def test_press_email_link_has_correct_mailto(self, page: Page):
        link = page.locator(PL.EMAIL_PRESS)
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", "mailto:press@momentgroup.ph")