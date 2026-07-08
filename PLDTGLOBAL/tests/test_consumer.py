import re
import pytest
from playwright.sync_api import Page, expect
from locators.consumer_locators import ConsumerLocators as CL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_consumer_page(page: Page):
    page.goto(CL.URL, wait_until="domcontentloaded", timeout=60000)
    
    # Smoothly dismiss the cookie banner if it renders so it doesn't intercept clicks
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=3000)
    except Exception:
        pass 
        
    yield


# ── Hero Section ──────────────────────────────────────────────────────────────

class TestConsumerHero:

    def test_hero_section_visible(self, page: Page):
        expect(page.locator(CL.IMG_HERO)).to_be_visible()
        expect(page.locator(CL.HEADING_SUB)).to_be_visible()
        expect(page.locator(CL.HEADING_MAIN)).to_be_visible()
        expect(page.locator(CL.TEXT_HERO_DESC)).to_be_visible()


# ── Solutions Grid ────────────────────────────────────────────────────────────

class TestConsumerGrid:

    def test_grid_intro_visible(self, page: Page):
        expect(page.locator(CL.HEADING_GRID)).to_be_visible()
        expect(page.locator(CL.TEXT_GRID_DESC)).to_be_visible()

    @pytest.mark.parametrize("solution_name, details", CL.SOLUTIONS.items())
    def test_solution_cards_visible(self, page: Page, solution_name: str, details: dict):
        """Iterates through the dictionary to verify all solution headings and descriptions."""
        expect(page.locator(details["heading"])).to_be_visible()
        expect(page.locator(details["desc"])).to_be_visible()

    def test_learn_more_button_navigates(self, page: Page):
        """Tests the first 'Learn More' button to verify solution routing works."""
        # We use .first so Playwright doesn't crash from finding multiple 'Learn More' buttons
        page.locator(CL.BTN_LEARN_MORE).first.click()
        
        # Playwright auto-retries until the URL changes
        expect(page).not_to_have_url(CL.URL)


# ── Bottom CTA Section ────────────────────────────────────────────────────────

class TestConsumerCTA:

    def test_cta_section_visible(self, page: Page):
        expect(page.locator(CL.HEADING_CTA)).to_be_visible()
        expect(page.locator(CL.TEXT_CTA_DESC)).to_be_visible()
        expect(page.locator(CL.BTN_INQUIRY)).to_be_visible()

    def test_send_inquiry_navigates(self, page: Page):
        page.locator(CL.BTN_INQUIRY).click()
        
        expect(page).not_to_have_url(CL.URL)
        # Verify it routes to the contact page
        expect(page).to_have_url(re.compile(r".*/contact-us.*"))