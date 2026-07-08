import pytest
from playwright.sync_api import Page, expect
from locators.enterprise_vortex_international import EnterpriseVortexInternationalLocators as PLDT


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_vortex_page(page: Page):
    page.goto(PLDT.URL, wait_until="domcontentloaded", timeout=60000)
    
    # Pre-emptively clear cookie overlays to prevent hidden element blocking
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=3000)
    except Exception:
        pass 
        
    yield


# ── Breadcrumbs ────────────────────────────────────────────────────────────────

class TestVortexBreadcrumbs:

    def test_breadcrumb_trail_visible(self, page: Page):
        """Verifies navigational trail layout at the top of the page workspace."""
        expect(page.locator(PLDT.LINK_ENTERPRISE)).to_be_visible()
        expect(page.locator(PLDT.TEXT_BREADCRUMB).first).to_be_visible()


# ── Hero & Content ─────────────────────────────────────────────────────────────

class TestVortexHero:

    def test_hero_and_assets_visible(self, page: Page):
        """Validates primary descriptive elements, headings, and supporting image assets."""
        expect(page.locator(PLDT.HEADING_MAIN)).to_be_visible()
        expect(page.locator(PLDT.TEXT_HERO_DESC)).to_be_visible()
        expect(page.locator(PLDT.IMG_BACK_TO).first).to_be_visible()

    def test_learn_more_link_interaction(self, page: Page):
        """Confirms actionable CTA links successfully reroute context away from current page."""
        learn_more_btn = page.locator(PLDT.LINK_LEARN_MORE)
        expect(learn_more_btn).to_be_visible()
        
        # Act and track changing location context safely using auto-retry assertions
        learn_more_btn.click()
        expect(page).not_to_have_url(PLDT.URL)