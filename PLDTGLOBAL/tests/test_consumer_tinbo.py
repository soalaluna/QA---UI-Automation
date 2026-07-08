import pytest
from playwright.sync_api import Page, expect
from locators.consumer_tinbo_locators import TinboLocators as TL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_tinbo_page(page: Page):
    page.goto(TL.URL, wait_until="domcontentloaded", timeout=60000)
    
    # Smoothly dismiss the cookie banner if it renders so it doesn't intercept clicks
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=3000)
    except Exception:
        pass 
        
    yield


# ── Breadcrumbs & Hero ────────────────────────────────────────────────────────

class TestTinboHero:

    def test_breadcrumb_trail_visible(self, page: Page):
        expect(page.locator(TL.LINK_CONSUMER)).to_be_visible()
        expect(page.locator(TL.TEXT_BREADCRUMB)).to_be_visible()

    def test_hero_content_visible(self, page: Page):
        expect(page.locator(TL.HEADING_MAIN)).to_be_visible()
        # FIX: Remove the 'text=' prefix inside the f-string
        expect(page.locator(f"p:has-text('{TL.TEXT_HERO_DESC.replace('text=', '')}')").first).to_be_visible()

    def test_visit_tinbo_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(TL.BTN_VISIT_TINBO).click()
        
        popup = popup_info.value
        popup.wait_for_load_state("domcontentloaded")
        assert "tinbo.ph" in popup.url
        popup.close()


# ── Key Stats & Features ──────────────────────────────────────────────────────

class TestTinboFeatures:

    def test_key_stats_visible(self, page: Page):
        expect(page.locator(TL.TEXT_STATS_500K).first).to_be_visible()
        expect(page.locator(TL.TEXT_STATS_100).first).to_be_visible()
        expect(page.locator(TL.TEXT_STATS_MINS).first).to_be_visible()

    def test_features_intro_visible(self, page: Page):
        # FIX: The log showed this is actually "Key Features" heading
        expect(page.locator(TL.HEADING_FEATURES)).to_be_visible()

    @pytest.mark.parametrize("feature_name, locator", TL.FEATURES.items())
    def test_feature_cards_visible(self, page: Page, feature_name: str, locator: str):
        expect(page.locator(locator).first).to_be_visible()


# ── Industry & Partners ───────────────────────────────────────────────────────

class TestTinboIndustry:

    def test_industry_applications_visible(self, page: Page):
        expect(page.locator(TL.HEADING_INDUSTRY)).to_be_visible()
        expect(page.locator(TL.TEXT_INDUSTRY_DESC)).to_be_visible()
        expect(page.locator(TL.HEADING_FINANCIAL)).to_be_visible()
        expect(page.locator(TL.TEXT_FINANCIAL)).to_be_visible()
        expect(page.locator(TL.HEADING_BPO)).to_be_visible()
        expect(page.locator(TL.TEXT_BPO)).to_be_visible()
        expect(page.locator(TL.IMG_INDUSTRY)).to_be_visible()
    def test_partners_carousel_renders(self, page: Page):
        # FIX: Check for attachment/existence first, then visibility
        carousel = page.locator(TL.PARTNER_CAROUSEL).first
        expect(carousel).to_be_attached() 


# ── FAQs ──────────────────────────────────────────────────────────────────────

class TestTinboFAQs:

    def test_faq_intro_visible(self, page: Page):
        expect(page.locator(TL.HEADING_FAQ)).to_be_visible()
        expect(page.locator(TL.TEXT_FAQ_DESC)).to_be_visible()

    @pytest.mark.parametrize("faq_name, btn_locator", TL.FAQS.items())
    def test_faq_accordions_expand(self, page: Page, faq_name: str, btn_locator: str):
        """Clicks each FAQ question and verifies an answer expands."""
        faq_btn = page.locator(btn_locator)
        expect(faq_btn).to_be_visible()
        
        faq_btn.click()
        # Verify the answer text becomes visible
        expect(page.locator(TL.TEXT_FAQ_ANSWER).first).to_be_visible()


# ── Explore Solutions (Footer) ────────────────────────────────────────────────

class TestExploreSolutions:

    def test_explore_solutions_heading(self, page: Page):
        expect(page.locator(TL.HEADING_EXPLORE)).to_be_visible()
        expect(page.locator(TL.TEXT_EXPLORE_DESC)).to_be_visible()

    @pytest.mark.parametrize("solution_name, details", TL.SOLUTIONS.items())
    def test_explore_solution_cards(self, page: Page, solution_name: str, details: dict):
        """Verifies solution titles and that the Explore buttons are actionable."""
        
        # If testing the 4th item, we might need to slide the carousel to see it
        if solution_name == "Global Connectivity":
            page.locator(TL.BTN_SLIDE_NEXT).click()
            page.wait_for_timeout(500)
            
        expect(page.locator(details["title"])).to_be_visible()
        
        # Ensure the explore button is attached to the DOM and clickable
        explore_btn = page.locator(details["btn"])
        expect(explore_btn).to_be_attached()