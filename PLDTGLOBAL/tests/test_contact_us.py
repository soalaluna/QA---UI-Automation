import re
import pytest
from playwright.sync_api import Page, expect
from locators.contact_us_locators import ContactUsLocators as CU


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_contact_page(page: Page):
    page.goto(CU.URL, wait_until="domcontentloaded", timeout=60000)
    
    # Defeat the cookie banner the right way!
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=3000)
    except Exception:
        pass # If the banner doesn't appear, just move on smoothly


# ── Hero & Layout ─────────────────────────────────────────────────────────────

class TestContactLayout:

    def test_hero_section_visible(self, page: Page):
        expect(page.locator(CU.HEADING_MAIN)).to_be_visible()
        expect(page.locator(CU.TEXT_INTRO)).to_be_visible()
        expect(page.locator(CU.IMG_HERO)).to_be_visible()

    def test_form_tabs_visible(self, page: Page):
        expect(page.locator(CU.HEADING_EXPLORE)).to_be_visible()
        expect(page.locator(CU.TEXT_EXPLORE_DESC)).to_be_visible()
        expect(page.locator(CU.TAB_CONSUMER)).to_be_visible()
        expect(page.locator(CU.TAB_ENTERPRISE)).to_be_visible()
        expect(page.locator(CU.TAB_CARRIER)).to_be_visible()


# ── Dynamic Form Tabs ─────────────────────────────────────────────────────────

class TestContactForms:

    def test_consumer_form_fields_visible(self, page: Page):
        """Verifies the default Consumer form loads correctly."""
        expect(page.locator(CU.TEXT_CONSUMER_TITLE)).to_be_visible()
        
        for field in CU.FIELDS_CONSUMER:
            expect(page.locator(field).first).to_be_visible()
            
        expect(page.locator(CU.BTN_SUBMIT).first).to_be_visible()

    def test_enterprise_form_fields_visible(self, page: Page):
        """Switches to the Enterprise tab and verifies its specific fields."""
        # We can remove force=True now that the cookie banner is gone!
        page.locator(CU.TAB_ENTERPRISE).click()
        page.wait_for_timeout(500) 
        
        expect(page.locator(CU.TEXT_ENTERPRISE_TITLE)).to_be_visible()
        
        for field in CU.FIELDS_ENTERPRISE:
            expect(page.locator(field).first).to_be_visible()
            
        expect(page.locator(CU.BTN_SUBMIT).first).to_be_visible()

    def test_carrier_form_fields_visible(self, page: Page):
        """Switches to the Carrier tab and verifies its specific fields."""
        page.locator(CU.TAB_CARRIER).click()
        page.wait_for_timeout(500)
        
        expect(page.locator(CU.TEXT_CARRIER_TITLE)).to_be_visible()
        
        for field in CU.FIELDS_CARRIER:
            expect(page.locator(field).first).to_be_visible()
            
        expect(page.locator(CU.BTN_SUBMIT).first).to_be_visible()

    def test_data_collection_disclaimer_visible(self, page: Page):
        expect(page.locator(CU.HEADING_DATA)).to_be_visible()
        expect(page.locator(CU.TEXT_DATA_DESC)).to_be_visible()


# ── Direct Contact & Map Section ──────────────────────────────────────────────

class TestDirectContact:

    def test_direct_contact_info_visible(self, page: Page):
        expect(page.locator(CU.HEADING_DIRECTLY)).to_be_visible()
        expect(page.locator(CU.TEXT_DIRECTLY_DESC)).to_be_visible()
        expect(page.locator(CU.LINK_EMAIL)).to_be_visible()
        expect(page.locator(CU.LINK_PHONE)).to_be_visible()
        expect(page.locator(CU.LINK_ADDRESS)).to_be_visible()
        expect(page.locator(CU.LINK_LINKEDIN)).to_be_visible()
        expect(page.locator(CU.MAP_IFRAME)).to_be_visible()

    def test_direct_contact_intents(self, page: Page):
        """Verifies mailto: and tel: links without actually triggering system prompts."""
        expect(page.locator(CU.LINK_EMAIL)).to_have_attribute("href", re.compile(r"mailto:askus@pldtglobal\.com"))
        expect(page.locator(CU.LINK_PHONE)).to_have_attribute("href", re.compile(r"tel:"))

    def test_address_opens_google_maps(self, page: Page):
        with page.expect_popup() as map_popup_info:
            page.locator(CU.LINK_ADDRESS).click()
        
        map_popup = map_popup_info.value
        map_popup.wait_for_load_state()
        assert "google.com/maps" in map_popup.url
        map_popup.close()

    def test_linkedin_opens_new_tab(self, page: Page):
        with page.expect_popup() as li_popup_info:
            page.locator(CU.LINK_LINKEDIN).click()
        
        li_popup = li_popup_info.value
        li_popup.wait_for_load_state()
        assert "linkedin.com" in li_popup.url
        li_popup.close()