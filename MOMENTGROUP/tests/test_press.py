import pytest
from playwright.sync_api import Page, expect
from locators.press_locators import PressLocators as PL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_press(page: Page):
    page.goto(PL.PRESS_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Layout & Static Info ───────────────────────────────────────────────────────

class TestPressLayout:

    def test_headings_and_text_visible(self, page: Page):
        expect(page.locator(PL.HEADING_COL1)).to_be_visible()
        expect(page.locator(PL.HEADING_COL2)).to_be_visible()
        expect(page.locator(PL.HEADING_INQUIRIES)).to_be_visible()
        expect(page.locator(PL.TEXT_INQUIRIES_DESC)).to_be_visible()

    def test_combobox_visible(self, page: Page):
        expect(page.locator(PL.COMBOBOX_BRAND)).to_be_visible()


# ── Contact ────────────────────────────────────────────────────────────────────

class TestContactInfo:

    def test_email_link_has_mailto_intent(self, page: Page):
        """Verifies the email link is properly configured with a mailto: href."""
        expect(page.locator(PL.LINK_EMAIL)).to_be_visible()
        href = page.locator(PL.LINK_EMAIL).get_attribute("href")
        assert href is not None
        assert "mailto:press@momentgroup.ph" in href


# ── Filters & Articles ─────────────────────────────────────────────────────────

class TestPressFilters:

    def test_default_articles_visible(self, page: Page):
        """Verifies the default 'All Brands' articles appear on initial load."""
        for article_locator in PL.ARTICLES["All Brands"]:
            expect(page.locator(article_locator)).to_be_visible()

    @pytest.mark.parametrize("brand_filter", ["Manam", "Mama Nams"])
    def test_filter_updates_articles(self, page: Page, brand_filter: str):
        page.locator(PL.COMBOBOX_BRAND).select_option(brand_filter)
        for article_locator in PL.ARTICLES[brand_filter]:
            expect(page.locator(article_locator).first).to_be_visible()


# ── External Links (Sample Testing) ───────────────────────────────────────────

class TestPressArticleLinks:

    @pytest.mark.parametrize("brand_filter,article_locator", [
        ("All Brands", "role=link[name*='May 2026 | PhilStar Life']"),
        ("Manam",      "role=link[name*='May 2026 | PhilStar Life']"),
        ("Mama Nams",  "role=link[name*='October 2025 | Philippine']"),
    ])
    def test_article_opens_new_tab(self, page: Page, brand_filter: str, article_locator: str):
        """Changes the filter (if needed) and verifies the article opens a new tab."""
        if brand_filter != "All Brands":
            page.locator(PL.COMBOBOX_BRAND).select_option(brand_filter)
            page.wait_for_timeout(500)

        card = page.locator(article_locator).first
        card.scroll_into_view_if_needed()

        with page.expect_popup() as popup_info:
            card.click(force=True)

        popup = popup_info.value
        popup.wait_for_load_state("domcontentloaded", timeout=15000)
        assert popup.url != PL.PRESS_URL
        assert "http" in popup.url
        popup.close()