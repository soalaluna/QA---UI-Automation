import pytest
from playwright.sync_api import Page, expect
from locators.brands_locators import BrandsLocators as BL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_brands(page: Page):
    """Navigate to brands page before each test"""
    page.goto(BL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.get_by_role("link", name="BRANDS").first.click()
    page.wait_for_url("**/brands**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestBrandsNavigation:

    def test_brands_page_loads(self, page: Page):
        """Brands page should load at correct URL"""
        expect(page).to_have_url(BL.BRANDS_URL)


# ── Brand Click Tests ─────────────────────────────────────────────────────────

class TestBrandClicks:

    def test_brand_1_clickable(self, page: Page):
        """First brand item should be clickable and navigate away from brands page"""
        page.locator(BL.BRAND_1).first.click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_2_clickable(self, page: Page):
        """Brand 2 should navigate to its page"""
        page.locator(BL.BRAND_2).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_3_clickable(self, page: Page):
        """Brand 3 should navigate to its page"""
        page.locator(BL.BRAND_3).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_4_clickable(self, page: Page):
        """Brand 4 should navigate to its page"""
        page.locator(BL.BRAND_4).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_5_clickable(self, page: Page):
        """Brand 5 should navigate to its page"""
        page.locator(BL.BRAND_5).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_6_clickable(self, page: Page):
        """Brand 6 should navigate to its page"""
        page.locator(BL.BRAND_6).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_7_clickable(self, page: Page):
        """Brand 7 should navigate to its page"""
        page.goto(BL.BRANDS_URL)
        page.locator(BL.BRAND_7).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_8_clickable(self, page: Page):
        """Brand 8 should navigate to its page"""
        page.goto(BL.BRANDS_URL)
        page.locator(BL.BRAND_8).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_9_clickable(self, page: Page):
        """Brand 9 should navigate to its page"""
        page.goto(BL.BRANDS_URL)
        page.locator(BL.BRAND_9).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_10_clickable(self, page: Page):
        """Brand 10 should navigate to its page"""
        page.goto(BL.BRANDS_URL)
        page.locator(BL.BRAND_10).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)

    def test_brand_11_clickable(self, page: Page):
        """Brand 11 should navigate to its page"""
        page.goto(BL.BRANDS_URL)
        page.locator(BL.BRAND_11).click()
        expect(page).not_to_have_url(BL.BRANDS_URL)