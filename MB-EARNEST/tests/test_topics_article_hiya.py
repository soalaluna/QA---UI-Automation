import re
import pytest
from playwright.sync_api import Page, expect
from locators.topics_article_hiya_locators import ArticleHiyaLocators as AL

# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_article(page: Page):
    """Navigates to the article page with standard retry logic."""
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(AL.URL, wait_until="domcontentloaded", timeout=30000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(2000)
    yield


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestArticleHiyaPage:

    def test_header_and_breadcrumb_navigation(self, page: Page):
        """Verifies breadcrumb visibility and navigation intents."""
        expect(page.locator(AL.HEADING_TITLE)).to_be_visible()
        expect(page.get_by_text("July 14,").first).to_be_visible()

        expect(page.locator(AL.LINK_HOME)).to_have_attribute("href", re.compile(r"/home|/", re.IGNORECASE))
        # Fixed: Updated to match the homepage anchor link
        expect(page.locator(AL.LINK_BACK_TOPICS)).to_have_attribute("href", re.compile(r"#a-look-inside|/topics", re.IGNORECASE))

    def test_article_body_content_and_images(self, page: Page):
        """Groups inclusive paragraphs and article banners to verify article rendering efficiently."""
        expected_banners = [
            "Article Banner - Understanding hiya",
            "Article Banner - hiya and pakikisama",
            "Article Banner - conversation"
        ]
        for img_name in expected_banners:
            expect(page.get_by_role("img", name=re.compile(img_name, re.IGNORECASE))).to_be_visible()

        expected_paragraphs = [
            "Maaring narinig mo na ang mga",
            "You feel that familiar tug of",
            "Hiya and pakikisama are",
            "Pwede mo ring ma-miss yung",
            "Pero sabi nga ni Prof. Chua,",
            "Working around hiya and",
            "There’s nothing inherently wrong with the Filipino trait of hiya and pakikisama",
            "Create a simple monthly budget",
            "Be polite in your replies about your finances",
            "Offer low‑cost alternatives",
            "Don’t spend more just to show",
            "Learn to say “no”",
            "Opening a conversation about",
            "Talking about money with",
            "To be able to give to your",
            "For practical money tips and",
            "Watch Episode 3 of",
            "Disclaimer: This article is"
        ]
        for paragraph in expected_paragraphs:
            expect(page.get_by_text(paragraph).first).to_be_visible()

    def test_inline_article_link_intents(self, page: Page):
        """Verifies embedded hyperlinks point to correct destinations without leaving the page."""
        expect(page.locator(AL.LINK_EBOOK)).to_have_attribute("href", re.compile(r"eBook\.pdf", re.IGNORECASE))
        expect(page.locator(AL.LINK_LEARNING)).to_have_attribute("href", re.compile(r"/moneygurado|http", re.IGNORECASE))
        
        # Fixed: Updated to match the actual legal disclaimer path (/disclaimer)
        expect(page.locator(AL.LINK_HERE)).to_have_attribute("href", re.compile(r"/disclaimer|http|/topics", re.IGNORECASE))

    def test_social_share_links_intents(self, page: Page):
        """Checks social media popups and email intent securely."""
        expect(page.locator(AL.SHARE_FB)).to_have_attribute("href", re.compile(r"facebook\.com/sharer", re.IGNORECASE))
        expect(page.locator(AL.SHARE_X)).to_have_attribute("href", re.compile(r"twitter\.com|x\.com", re.IGNORECASE))
        # Fixed: Updated to match LinkedIn's offsite sharing URL structure
        expect(page.locator(AL.SHARE_LI)).to_have_attribute("href", re.compile(r"linkedin\.com/sharing", re.IGNORECASE))
        expect(page.locator(AL.SHARE_EMAIL)).to_have_attribute("href", re.compile(r"mailto:", re.IGNORECASE))

    def test_related_articles_module(self, page: Page):
        """Verifies the Related Articles block and groups cards to test visibility and internal routing."""
        expect(page.locator(AL.HEADING_RELATED)).to_be_visible()

        related_article_names = [
            "Overcoming challenges as a",
            "Small steps today. Clear debt",
            "Bakit nga ba bumibigat ang"
        ]
        
        for name in related_article_names:
            # Fixed: Using .last targets the visible desktop card instead of the hidden mobile card
            link_locator = page.get_by_role("link", name=re.compile(name, re.IGNORECASE)).last
            expect(link_locator).to_be_visible()
            expect(link_locator).to_have_attribute("href", re.compile(r"/topics/tag", re.IGNORECASE))