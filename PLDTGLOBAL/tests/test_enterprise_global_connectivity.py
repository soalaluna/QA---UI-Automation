import pytest
from playwright.sync_api import Page, expect
from locators.enterprise_global_connectivity_locators import PLDTConnectivityLocators as PLDT


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_connectivity_page(page: Page):
    page.goto(PLDT.URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Breadcrumbs ────────────────────────────────────────────────────────────────

class TestBreadcrumbs:

    def test_breadcrumb_navigation_visible(self, page: Page):
        """Verifies the breadcrumb trail renders correctly at the top of the page."""
        expect(page.locator(PLDT.LINK_ENTERPRISE)).to_be_visible()
        expect(page.locator(PLDT.ICON_CHEVRON).first).to_be_visible()
        expect(page.locator(PLDT.TEXT_BREADCRUMB)).to_be_visible()


# ── Hero & Intro Section ───────────────────────────────────────────────────────

class TestConnectivityHero:

    def test_hero_content_visible(self, page: Page):
        expect(page.locator(PLDT.HEADING_MAIN)).to_be_visible()
        expect(page.locator(PLDT.TEXT_HERO_DESC)).to_be_visible()
        expect(page.locator(PLDT.IMG_BACK_TO).first).to_be_visible()

    def test_portfolio_intro_visible(self, page: Page):
        expect(page.locator(PLDT.HEADING_PORTFOLIO)).to_be_visible()
        expect(page.locator(PLDT.TEXT_PORTFOLIO)).to_be_visible()


# ── Product Portfolio Cards ────────────────────────────────────────────────────

class TestProductPortfolio:

    def test_product_card_icons_load(self, page: Page):
        """Verifies that the gradient border cards with icons are rendering."""
        # Using .first prevents strict mode errors while confirming the UI components load
        expect(page.locator(PLDT.CARD_ICONS).first).to_be_visible()

    @pytest.mark.parametrize("product_name, details", PLDT.PRODUCTS.items())
    def test_product_cards_content(self, page: Page, product_name: str, details: dict):
        """Iterates through the dictionary to verify all product headings and descriptions."""
        
        # 1. Assert Heading
        expect(page.locator(details["heading"])).to_be_visible()
        
        # 2. Assert Description
        expect(page.locator(details["desc"])).to_be_visible()