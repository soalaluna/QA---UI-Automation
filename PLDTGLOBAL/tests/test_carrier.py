import pytest
from playwright.sync_api import Page, expect
from locators.carrier_locators import PldtCarrierLocators as PL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_carrier(page: Page):
    page.goto(PL.CARRIER_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Hero Section ───────────────────────────────────────────────────────────────

class TestCarrierHero:

    def test_heading_visible(self, page: Page):
        expect(PL.heading_carrier_grade(page)).to_be_visible()

    def test_description_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_RELIABLE_VOICE)).to_be_visible()

    def test_learn_more_link_visible(self, page: Page):
        expect(page.get_by_role("link", name="Learn More").first).to_be_visible()

    def test_learn_more_link_clickable(self, page: Page):
        # Codegen clicked .first twice — reduced to one meaningful click
        page.get_by_role("link", name="Learn More").first.click()
        # Navigate back to keep page state clean for subsequent assertions
        page.goto(PL.CARRIER_URL, wait_until="domcontentloaded", timeout=60000)


# ── Built for Global Carrier Section ──────────────────────────────────────────

class TestBuiltForGlobal:

    def test_img_visible(self, page: Page):
        expect(page.locator(PL.IMG_BUILT_FOR_GLOBAL)).to_be_visible()

    def test_overlay_element_visible(self, page: Page):
        # Positional CSS class selector; use .first to avoid strict-mode violation
        expect(page.locator(PL.OVERLAY_TOP_LEFT).first).to_be_visible()

    def test_carrier_heading_exact_visible(self, page: Page):
        expect(PL.heading_carrier_exact(page)).to_be_visible()


# ── Carrier Solutions Portfolio ────────────────────────────────────────────────

class TestCarrierSolutionsPortfolio:

    def test_heading_visible(self, page: Page):
        expect(PL.heading_carrier_solutions(page)).to_be_visible()

    def test_description_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_FOCUSED_SUITE)).to_be_visible()

    def test_section_image_visible(self, page: Page):
        expect(PL.section_carrier_img(page)).to_be_visible()


# ── Wholesale Voice ────────────────────────────────────────────────────────────

class TestWholesaleVoice:

    def test_heading_visible(self, page: Page):
        expect(PL.heading_wholesale_voice(page)).to_be_visible()

    def test_description_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_HIGH_QUALITY)).to_be_visible()

    def test_learn_more_exact_visible(self, page: Page):
        expect(PL.link_learn_more_exact(page)).to_be_visible()

    def test_div_toggle_and_learn_more_still_visible(self, page: Page):
        """
        Codegen clicks div.nth(5) then re-asserts the Learn More link.
        This likely toggles a tab or accordion section.
        NOTE: div.nth(5) is positional and fragile -- see locator docstring.
        """
        PL.div_nth_5(page).click()
        expect(PL.link_learn_more_exact(page)).to_be_visible()