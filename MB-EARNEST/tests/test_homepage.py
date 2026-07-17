import re

import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import HomepageLocators as EL

# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_home(page: Page):
    """Navigates to the homepage with a robust wait and retry logic."""
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(EL.URL, wait_until="domcontentloaded", timeout=60000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(3000)
    yield


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestEarnestHomepage:

    def test_header_navigation_visible(self, page: Page):
        expect(page.locator(EL.LOGO_MAIN)).to_be_visible()
        expect(page.locator(EL.NAV_EXPLORE)).to_be_visible()
        expect(page.locator(EL.NAV_EBOOK)).to_be_visible()
        expect(page.locator(EL.NAV_MONEYGURADO)).to_be_visible()
        expect(page.locator(EL.NAV_HANDS)).to_be_visible()

    def test_hero_and_moneygurado_banner_visible(self, page: Page):
        expect(page.locator(EL.HERO_BANNER_IMG)).to_be_visible()
        expect(page.locator(EL.HERO_HEADING)).to_be_visible()
        expect(page.locator(EL.MONEYGURADO_BANNER).first).to_be_visible()

    def test_learning_topics_visible(self, page: Page):
        """Verifies the three main learning pillars and their icons."""
        expect(page.locator(EL.HEADING_LEARNING).first).to_be_visible()
        
        # Manage
        expect(page.locator(EL.TOPIC_MANAGE_HEADING)).to_be_visible()
        expect(page.locator(EL.TOPIC_MANAGE_ICON)).to_be_visible()
        
        # Grow
        expect(page.locator(EL.TOPIC_GROW_HEADING)).to_be_visible()
        expect(page.locator(EL.TOPIC_GROW_ICON)).to_be_visible()
        
        # Protect
        expect(page.locator(EL.TOPIC_PROTECT_HEADING)).to_be_visible()
        expect(page.locator(EL.TOPIC_PROTECT_ICON)).to_be_visible()

        # Ensure at least one 'Learn More' button renders in this section
        expect(page.locator(EL.BTN_LEARN_MORE).first).to_be_visible()

    def test_video_player_iframe_loads(self, page: Page):
        """Verifies the video iframe loads and interior buttons are accessible."""
        # We use frame_locator to safely peer inside the video iframe
        video_frame = page.frame_locator(EL.IFRAME_VIDEO)
        expect(video_frame.locator(EL.BTN_PLAY_VIDEO).first).to_be_visible()

    def test_articles_and_ebook_sections_visible(self, page: Page):
        # Money Talk
        expect(page.locator(EL.HEADING_MONEY_TALK)).to_be_visible()
        
        # E-book
        expect(page.locator(EL.HEADING_EBOOK)).to_be_visible()
        expect(page.locator(EL.BTN_GET_EBOOK)).to_be_visible()
        
        # H.A.N.D.S.
        expect(page.locator(EL.IMG_HANDS)).to_be_visible()
        expect(page.locator(EL.HEADING_HANDS)).to_be_visible()

    def test_ebook_download_functions(self, page: Page):
        """Tests the download mechanics without verifying the actual file contents."""
        with page.expect_download() as download_info:
            page.locator(EL.NAV_EBOOK).click()
        
        download = download_info.value
        assert download.url is not None
        # Cancel the download to save execution time and disk space
        download.cancel()

    def test_bottom_ctas_visible(self, page: Page):
        expect(page.locator(EL.HEADING_INVEST)).to_be_visible()
        expect(page.locator(EL.LINK_INVEST)).to_be_visible()
        expect(page.locator(EL.HEADING_COMMUNITY)).to_be_visible()
        expect(page.locator(EL.LINK_COMMUNITY)).to_be_visible()

    def test_footer_information_and_seals_visible(self, page: Page):
        expect(page.locator(EL.TEXT_PRESENTED_BY)).to_be_visible()
        expect(page.locator(EL.IMG_MB_LOGO_FOOTER)).to_be_visible()
        
        expect(page.locator(EL.TEXT_INQUIRIES)).to_be_visible()
        expect(page.locator(EL.TEXT_PDIC)).to_be_visible()
        
        expect(page.locator(EL.SEAL_DPO)).to_be_visible()
        expect(page.locator(EL.SEAL_PDIC)).to_be_visible()
        expect(page.locator(EL.SEAL_BIR)).to_be_visible()
        
        expect(page.locator(EL.TEXT_COPYRIGHT)).to_be_visible()

    def test_external_link_intents(self, page: Page):
        """
        Instead of clicking popups and risking anti-bot blocks, 
        we assert that the links are wired up to valid external destinations.
        """
        # Footer primary links
        expect(page.locator(EL.LINK_VISIT_MB)).to_have_attribute("href", re.compile(r"metrobank\.com\.ph"))
        expect(page.locator(EL.LINK_BSP)).to_have_attribute("href", re.compile(r"bsp\.gov\.ph"))
        expect(page.locator(EL.LINK_SIGN_UP)).to_have_attribute("href", re.compile(r"http"))

        # Social Media Icons - Ensure all social icons have an href destination
        social_links = page.locator(EL.SOCIAL_LINKS)
        count = social_links.count()
        assert count > 0, "No social links found in footer"
        
        for i in range(count):
            expect(social_links.nth(i)).to_have_attribute("href", re.compile(r"http"))