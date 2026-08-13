import re
import pytest
from playwright.sync_api import Page, expect
from locators.topics_grow_locators import TopicsGrowLocators as GL

# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_grow_topic(page: Page):
    """Navigates to the Grow Topic page before each test."""
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(GL.URL_GROW, wait_until="domcontentloaded", timeout=30000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(2000)
    yield


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestGrowTopicPage:

    def test_hero_and_breadcrumbs_visible(self, page: Page):
        """Verifies top-level navigation and page introduction."""
        expect(page.locator(GL.LINK_GO_BACK)).to_be_visible()
        expect(page.locator(GL.LINK_TOPICS)).to_be_visible()
        
        expect(page.locator(GL.HEADING_HERO)).to_be_visible()
        expect(page.locator(GL.TEXT_HERO_SUB)).to_be_visible()
        expect(page.locator(GL.TEXT_FAST_TRACK).first).to_be_visible()

    def test_internal_navigation_intents(self, page: Page):
        """Checks that internal routing buttons point to correct paths."""
        expect(page.locator(GL.LINK_TOPICS)).to_have_attribute("href", "")
        
        # Fixed: Added the '/tag/' segment to match the actual blog routing
        expect(page.locator(GL.LINK_READ_ALL)).to_have_attribute("href", re.compile(r"/topics/tag/grow", re.IGNORECASE))

    def test_conversion_modules_visible(self, page: Page):
        """Verifies the E-book and Investing call-to-action blocks."""
        # E-book block
        expect(page.locator(GL.HEADING_EBOOK).first).to_be_visible()
        expect(page.locator(GL.TEXT_EBOOK_SUB).first).to_be_visible()
        expect(page.locator(GL.LINK_GET_EBOOK)).to_be_visible()
        
        # Invest block
        expect(page.locator(GL.HEADING_INVEST).first).to_be_visible()
        expect(page.locator(GL.TEXT_INVEST_SUB).first).to_be_visible()
        expect(page.locator(GL.LINK_EXPLORE_INVEST)).to_be_visible()

    def test_external_conversion_link_intents(self, page: Page):
        """Instantly verifies outbound popup destinations without network overhead."""
        expect(page.locator(GL.LINK_GET_EBOOK)).to_have_attribute("href", re.compile(r"metrobank\.com\.ph", re.IGNORECASE))
        expect(page.locator(GL.LINK_EXPLORE_INVEST)).to_have_attribute("href", re.compile(r"metrobank\.com\.ph/invest", re.IGNORECASE))
        expect(page.locator(GL.LINK_SIGNUP)).to_have_attribute("href", re.compile(r"http"))

    def test_footer_compliance_and_seals(self, page: Page):
        """Ensures all legal text and regulatory seals render correctly."""
        expect(page.locator(GL.TEXT_PRESENTED_BY).first).to_be_visible()
        expect(page.locator(GL.FOOTER_LOGO).first).to_be_visible()
        
        # Compliance Text
        expect(page.locator(GL.TEXT_INQUIRIES).first).to_be_visible()
        expect(page.locator(GL.TEXT_REGULATED).first).to_be_visible()
        expect(page.locator(GL.TEXT_PDIC).first).to_be_visible()
        expect(page.locator(GL.TEXT_COPYRIGHT).first).to_be_visible()
        expect(page.locator(GL.TEXT_PROUD_MEMBER).first).to_be_visible()
        
        # --- THE FIX ---
        # 1. Force the browser to scroll to the bottom so lazy images render
        page.keyboard.press("End")
        
        # 2. Use .last to target the desktop UI seals instead of the hidden mobile ones
        expect(page.locator(GL.SEAL_DPO).last).to_be_visible()
        expect(page.locator(GL.SEAL_PDIC).last).to_be_visible()
        expect(page.locator(GL.SEAL_BIR).last).to_be_visible()

    def test_external_conversion_link_intents(self, page: Page):
        """Instantly verifies outbound popup destinations without network overhead."""
        expect(page.locator(GL.LINK_GET_EBOOK)).to_have_attribute("href", re.compile(r"metrobank\.com\.ph", re.IGNORECASE))
        
        # Fixed: Updated to the correct earnest.ph domain
        expect(page.locator(GL.LINK_EXPLORE_INVEST)).to_have_attribute("href", re.compile(r"earnest\.ph/invest", re.IGNORECASE))
        
        # Ensure all social icons are wired up
        social_links = page.locator(GL.SOCIAL_LINKS)
        count = social_links.count()
        assert count > 0, "No social media links found in the footer."
        for i in range(count):
            expect(social_links.nth(i)).to_have_attribute("href", re.compile(r"http"))