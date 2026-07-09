import re
import pytest
from playwright.sync_api import Page, expect
from locators.global_components_locators import GlobalLocators as GL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def navigate_base_page(page: Page):
    """Navigates to the page without dismissing the cookie banner."""
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(GL.URL, wait_until="domcontentloaded", timeout=60000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(3000)
    yield

@pytest.fixture
def navigate_and_clear_cookies(page: Page, navigate_base_page):
    """Navigates to the page and explicitly clears the cookie banner."""
    try:
        page.locator(GL.BTN_ACCEPT_ALL).click(timeout=5000)
        page.wait_for_timeout(1000) # Wait for animation to clear
    except Exception:
        pass
    yield


# ── Global Header ─────────────────────────────────────────────────────────────

class TestGlobalHeader:

    def test_header_elements_visible(self, page: Page, navigate_and_clear_cookies):
        expect(page.locator(GL.HEADER_LOGO)).to_be_visible()
        expect(page.locator(GL.LINK_HOME)).to_be_visible()
        expect(page.locator(GL.LINK_ABOUT)).to_be_visible()
        expect(page.locator(GL.LINK_NEWS)).to_be_visible()
        expect(page.locator(GL.LINK_CAREERS)).to_be_visible()
        expect(page.locator(GL.BTN_SEARCH)).to_be_visible()
        expect(page.locator(GL.BTN_CONTACT_US)).to_be_visible()


# ── Cookie Banner & Preferences ───────────────────────────────────────────────

class TestCookieBanner:

    def test_cookie_banner_initial_state(self, page: Page, navigate_base_page):
        """Verifies the initial banner appears before interaction."""
        expect(page.locator(GL.BANNER_TEXT).first).to_be_visible()
        expect(page.locator(GL.BTN_ACCEPT_ALL)).to_be_visible()
        expect(page.locator(GL.BTN_PREFERENCES)).to_be_visible()

    def test_cookie_preference_center_accordions(self, page: Page, navigate_base_page):
        """Opens the Preference Center and validates the inner accordion text."""
        page.locator(GL.BTN_PREFERENCES).click()
        expect(page.locator(GL.MODAL_HEADING)).to_be_visible()
        
        # Test Strictly Necessary
        page.locator(GL.BTN_STRICTLY_NEC).click()
        expect(page.locator(GL.TEXT_STRICTLY_DESC).first).to_be_visible()
        
        # Test Functional
        page.locator(GL.BTN_FUNCTIONAL).click()
        expect(page.locator(GL.TEXT_FUNCT_DESC).first).to_be_visible()
        
        # Test Performance
        page.locator(GL.BTN_PERFORMANCE).click()
        expect(page.locator(GL.TEXT_PERF_DESC).first).to_be_visible()
        
        # Test Targeting
        page.locator(GL.BTN_TARGETING).click()
        expect(page.locator(GL.TEXT_TARGET_DESC).first).to_be_visible()

        # Ensure the save button exists
        expect(page.locator(GL.BTN_SAVE_PREFS)).to_be_visible()


# ── Global Footer ─────────────────────────────────────────────────────────────

class TestGlobalFooter:

    def test_footer_contact_info_visible(self, page: Page, navigate_and_clear_cookies):
        expect(page.locator(GL.FOOTER_LOGO)).to_be_visible()
        expect(page.locator(GL.FOOTER_HEADING)).to_be_visible()
        expect(page.locator(GL.LINK_EMAIL)).to_be_visible()
        expect(page.locator(GL.LINK_PHONE)).to_be_visible()
        expect(page.locator(GL.LINK_LINKEDIN)).to_be_visible()

    def test_footer_contact_intents(self, page: Page, navigate_and_clear_cookies):
        """Verifies mailto: and tel: links without triggering system default apps."""
        expect(page.locator(GL.LINK_EMAIL)).to_have_attribute("href", re.compile(r"mailto:askus@pldtglobal\.com"))
        expect(page.locator(GL.LINK_PHONE)).to_have_attribute("href", re.compile(r"tel:"))

    def test_linkedin_link_intent(self, page: Page, navigate_and_clear_cookies):
        """Verifies the LinkedIn link destination without clicking to avoid 3rd-party bot blockers."""
        expect(page.locator(GL.LINK_LINKEDIN)).to_have_attribute("href", re.compile(r"linkedin\.com/company/pldtglobal", re.IGNORECASE))

    @pytest.mark.parametrize("category, links", GL.FOOTER_SITEMAP.items())
    def test_footer_sitemap_categories(self, page: Page, navigate_and_clear_cookies, category: str, links: list):
        """Iterates through the dictionary to ensure all sitemap columns render correctly."""
        for link in links:
            expect(page.locator(link)).to_be_visible()

    def test_footer_legal_section_visible(self, page: Page, navigate_and_clear_cookies):
        expect(page.locator(GL.TEXT_COPYRIGHT).first).to_be_visible()
        expect(page.locator(GL.LINK_COOKIE_POL)).to_be_visible()
        expect(page.locator(GL.LINK_PRIVACY_POL)).to_be_visible()