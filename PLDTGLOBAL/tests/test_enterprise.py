import re
import pytest
from playwright.sync_api import Page, expect
from locators.enterprise_locators import EnterpriseLocators as EL

# ... keep the rest of your file exactly as it is ...

# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_enterprise_page(page: Page):
    page.goto(EL.URL, wait_until="domcontentloaded", timeout=60000)
    
    # Smoothly dismiss the cookie banner if it renders so it doesn't intercept clicks
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=3000)
    except Exception:
        pass 
        
    yield


# ── Hero Section ──────────────────────────────────────────────────────────────

class TestEnterpriseHero:

    def test_hero_section_visible(self, page: Page):
        expect(page.locator(EL.IMG_HERO)).to_be_visible()
        expect(page.locator(EL.HEADING_SUB)).to_be_visible()
        expect(page.locator(EL.HEADING_MAIN)).to_be_visible()
        expect(page.locator(EL.TEXT_HERO_DESC)).to_be_visible()


# ── Solutions Grid ────────────────────────────────────────────────────────────

class TestSolutionsGrid:

    @pytest.fixture(autouse=True)
    def load_all_solutions(self, page: Page):
        """Clicks 'Load More Solutions' if it exists to ensure all cards are in the DOM."""
        load_more = page.locator(EL.BTN_LOAD_MORE)
        # Using a quick timeout to check if the button is there
        try:
            expect(load_more).to_be_visible(timeout=3000)
            load_more.click()
            page.wait_for_timeout(500) # Give grid time to expand
        except AssertionError:
            pass # Button isn't there, all cards are likely already loaded

    @pytest.mark.parametrize("solution_name, details", EL.SOLUTIONS.items())
    def test_solution_cards_visible(self, page: Page, solution_name: str, details: dict):
        """Iterates through the dictionary to verify all solution headings and descriptions."""
        expect(page.locator(details["heading"])).to_be_visible()
        expect(page.locator(details["desc"])).to_be_visible()

    def test_learn_more_button_navigates(self, page: Page):
        """Tests the first 'Learn More' button to verify solution routing works."""
        page.locator(EL.BTN_LEARN_MORE).first.click()
        
        # Playwright auto-retries until the URL changes
        expect(page).not_to_have_url(EL.URL)


# ── Bottom CTA Section ────────────────────────────────────────────────────────

class TestEnterpriseCTA:

    def test_cta_section_visible(self, page: Page):
        expect(page.locator(EL.HEADING_CTA)).to_be_visible()
        expect(page.locator(EL.TEXT_CTA_DESC)).to_be_visible()
        expect(page.locator(EL.BTN_INQUIRY)).to_be_visible()

    def test_send_inquiry_navigates(self, page: Page):
        page.locator(EL.BTN_INQUIRY).click()
        
        expect(page).not_to_have_url(EL.URL)
        # Verify it routes to the contact page
        expect(page).to_have_url(re.compile(r".*/contact-us.*"))