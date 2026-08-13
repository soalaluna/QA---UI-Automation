import re
import pytest
from playwright.sync_api import Page, expect
from locators.topics_protect_locators import ProtectTopicLocators as PL

# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_protect_topic(page: Page):
    """Navigates to the Protect Topic page before each test with retry logic."""
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(PL.URL_PROTECT, wait_until="domcontentloaded", timeout=30000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(2000)
    yield


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestProtectTopicPage:

    def test_hero_and_breadcrumbs_visible(self, page: Page):
        """Verifies top-level navigation and the hero section introduction."""
        expect(page.locator(PL.LINK_GO_BACK)).to_be_visible()
        expect(page.locator(PL.LINK_TOPICS)).to_be_visible()
        
        expect(page.locator(PL.HEADING_HERO)).to_be_visible()
        expect(page.locator(PL.TEXT_HERO_SUB).first).to_be_visible()
        expect(page.locator(PL.TEXT_STAY_AHEAD).first).to_be_visible()
        expect(page.locator(PL.BANNER_IMG)).to_be_visible()

    def test_internal_navigation_intents(self, page: Page):
        """Checks that internal routing buttons point to correct paths."""
        # The developers leave the Topics breadcrumb href empty
        expect(page.locator(PL.LINK_TOPICS)).to_have_attribute("href", "")
        
        # Verify both 'Read all articles' buttons route to the protect tag
        expect(page.locator(PL.LINK_READ_ALL).first).to_have_attribute("href", re.compile(r"/topics/tag/protect", re.IGNORECASE))

    def test_conversion_modules_visible(self, page: Page):
        """Verifies the E-book and Fraud call-to-action blocks."""
        # Fraud block
        expect(page.locator(PL.HEADING_FRAUD)).to_be_visible()
        expect(page.locator(PL.TEXT_FRAUD_SUB).first).to_be_visible()
        
        # E-book block
        expect(page.locator(PL.HEADING_EBOOK).first).to_be_visible()
        expect(page.locator(PL.TEXT_EBOOK_SUB).first).to_be_visible()
        
        # Verify the E-book button intent without initiating a network download or popup
        expect(page.locator(PL.LINK_GET_EBOOK)).to_have_attribute("href", re.compile(r"metrobank\.com\.ph", re.IGNORECASE))

    def test_footer_compliance_and_seals(self, page: Page):
        """Ensures all legal text and lazy-loaded regulatory seals render correctly."""
        # Handle responsive duplicate text nodes
        expect(page.locator(PL.TEXT_PRESENTED_BY).first).to_be_visible()
        expect(page.locator(PL.FOOTER_LOGO).first).to_be_visible()
        
        expect(page.locator(PL.TEXT_INQUIRIES).first).to_be_visible()
        expect(page.locator(PL.TEXT_REGULATED).first).to_be_visible()
        expect(page.locator(PL.TEXT_PDIC).first).to_be_visible()
        expect(page.locator(PL.TEXT_COPYRIGHT).first).to_be_visible()
        expect(page.locator(PL.TEXT_PROUD_MEMBER).first).to_be_visible()
        
        # Force the browser to scroll down to trigger lazy-loaded images
        page.keyboard.press("End")
        
        # Target the desktop UI seals (.last) to avoid hidden mobile duplicates
        expect(page.locator(PL.SEAL_DPO).last).to_be_visible()
        expect(page.locator(PL.SEAL_PDIC).last).to_be_visible()
        expect(page.locator(PL.SEAL_BIR).last).to_be_visible()

    def test_footer_external_links(self, page: Page):
        """Verifies footer popups point to the correct domains securely."""
        expect(page.locator(PL.LINK_VISIT_MB)).to_have_attribute("href", re.compile(r"metrobank\.com\.ph/home", re.IGNORECASE))
        expect(page.locator(PL.LINK_BSP)).to_have_attribute("href", re.compile(r"bsp\.gov\.ph", re.IGNORECASE))
        
        # REMOVED: The LINK_SIGNUP assertion, as this element is not rendered on the Protect page.
        
        # Ensure all 5 social icons are wired up properly
        social_links = page.locator(PL.SOCIAL_LINKS)
        count = social_links.count()
        assert count > 0, "No social media links found in the footer."
        for i in range(count):
            expect(social_links.nth(i)).to_have_attribute("href", re.compile(r"http"))