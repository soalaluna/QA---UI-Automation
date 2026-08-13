import re
import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import EarnestHomepageLocators as HL

# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_homepage(page: Page):
    """Navigates to the homepage with standard retry logic."""
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(HL.URL, wait_until="domcontentloaded", timeout=30000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(2000)
    yield


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestEarnestHomePage:

    def test_homepage_headings_and_descriptions(self, page: Page):
        """Groups core text blocks and headings to verify content structure without padding."""
        
        # 1. Grouped Core Headings (.first is usually fine for headings, but let's keep it clean)
        expected_headings = [
            "Your trusted financial",
            "Let’s talk about money",
            "A practical guide to navigate",
            "Ready to invest?",
            "Get trusted advice on"
        ]
        for heading_text in expected_headings:
            expect(page.get_by_role("heading", name=re.compile(heading_text, re.IGNORECASE)).first).to_be_visible()

        # 2. Grouped Descriptive Text Substrings
        expected_texts = [
            "Earnest by Metrobank offers",
            "Pagdating sa pera, moneygurado muna",
            "Earnest Learning",
            "Get better with money",
            "Find out how culture and society shape Filipinos' finances",
            "Put Earnest in your pocket",
            "All the practical personal",
            "Straightforward financial",
            "Get the help you need every",
            "Take charge of your financial"
        ]
        for text_snippet in expected_texts:
            # Fixed: Using .last avoids grabbing hidden mobile paragraphs on desktop runs
            expect(page.get_by_text(text_snippet).last).to_be_visible()

    def test_topic_cards_and_routing_intents(self, page: Page):
        """Verifies the three main educational pillars (Manage, Grow, Protect) and their routing."""
        topic_cards = page.locator(HL.TOPIC_CARDS)
        expect(topic_cards.first).to_be_visible()

        for topic in HL.TOPIC_NAMES:
            # Check card heading and icon
            expect(page.get_by_role("heading", name=topic)).to_be_visible()
            expect(page.get_by_role("img", name=re.compile(f"icons {topic}", re.IGNORECASE))).to_be_visible()
            
            # Verify card's "Learn More" link routes to correct topic hub
            card_link = page.locator(HL.TOPIC_CARDS).filter(has_text=topic).get_by_role("link", name="Learn More")
            expect(card_link).to_have_attribute("href", re.compile(f"/topics/{topic.lower()}", re.IGNORECASE))

    def test_embedded_video_player_interaction(self, page: Page):
        """Interacts with the embedded Moneygurado video frame securely."""
        video_frame = page.frame_locator(HL.VIDEO_FRAME)
        
        # 1. Check initial overlay state
        expect(video_frame.locator(HL.VIDEO_OVERLAY)).to_be_visible()
        
        # 2. Click Play to start the stream
        play_btn = video_frame.locator(HL.BTN_PLAY)
        expect(play_btn).to_be_visible()
        play_btn.click()
        
        # 3. Give YouTube 1.5 seconds to buffer and transition its state
        page.wait_for_timeout(1500)
        
        # --- THE FIX ---
        # Instead of clicking the screen (which pauses it), we simply hover over 
        # the video area to wake up the control bar if it faded out!
        video_frame.locator("video").hover(force=True)
        
        # 4. Now the Pause button will be rendered and ready to click
        pause_btn = video_frame.locator(HL.BTN_PAUSE)
        expect(pause_btn).to_be_visible(timeout=10000)
        pause_btn.click()

    def test_external_conversion_link_intents(self, page: Page):
        """Instantly verifies outbound call-to-action buttons without opening browser tabs."""
        expect(page.locator(HL.LINK_EBOOK)).to_have_attribute("href", re.compile(r"eBook\.pdf", re.IGNORECASE))
        expect(page.locator(HL.LINK_INVEST)).to_have_attribute("href", re.compile(r"earnest\.ph/invest|metrobank\.com\.ph", re.IGNORECASE))
        expect(page.locator(HL.LINK_COMMUNITY)).to_have_attribute("href", re.compile(r"facebook\.com/groups|http", re.IGNORECASE))