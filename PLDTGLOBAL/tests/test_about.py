"""
Test suite for the About Us page - pldtglobal.com/en/about-us
Covers: navigation, cable map filters (radio + checkbox), solutions CTAs,
        team accordion, and the location map controls.
"""

import pytest
from playwright.sync_api import Page, expect
from locators.about_locators import AboutLocators as AL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_about(page: Page):
    page.goto(AL.BASE_URL, wait_until="domcontentloaded", timeout=60000)
    page.locator(AL.NAV_ABOUT).click()
    # Accept cookies if the banner appears (only shows on first visit per session)
    try:
        page.locator(AL.BTN_ACCEPT_COOKIES).click(timeout=5000)
    except Exception:
        pass
    page.wait_for_url("**/about-us**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestAboutNavigation:

    def test_about_page_loads(self, page: Page):
        expect(page).to_have_url(AL.ABOUT_URL)


# ── Cable Map: Radio Filter Tests ─────────────────────────────────────────────

class TestCableMapRadioFilters:

    def test_aag_radio_selectable(self, page: Page):
        page.locator(AL.RADIO_AAG).check()
        expect(page.locator(AL.RADIO_AAG)).to_be_checked()

    def test_jupiter_radio_selectable(self, page: Page):
        page.locator(AL.RADIO_JUPITER).check()
        expect(page.locator(AL.RADIO_JUPITER)).to_be_checked()

    def test_faster_radio_selectable(self, page: Page):
        page.locator(AL.RADIO_FASTER).check()
        expect(page.locator(AL.RADIO_FASTER)).to_be_checked()

    def test_apricot_radio_selectable(self, page: Page):
        page.locator(AL.RADIO_APRICOT).check()
        expect(page.locator(AL.RADIO_APRICOT)).to_be_checked()

    def test_switching_radio_unchecks_previous(self, page: Page):
        """Radio buttons should be mutually exclusive within the group."""
        page.locator(AL.RADIO_AAG).check()
        page.locator(AL.RADIO_JUPITER).check()
        expect(page.locator(AL.RADIO_JUPITER)).to_be_checked()
        expect(page.locator(AL.RADIO_AAG)).not_to_be_checked()


# ── Cable Map: Segment Checkbox Tests ─────────────────────────────────────────

class TestCableMapCheckboxFilters:

    def test_enterprise_checkbox_toggle(self, page: Page):
        page.locator(AL.CHECKBOX_ENTERPRISE).check()
        expect(page.locator(AL.CHECKBOX_ENTERPRISE)).to_be_checked()
        page.locator(AL.CHECKBOX_ENTERPRISE).uncheck()
        expect(page.locator(AL.CHECKBOX_ENTERPRISE)).not_to_be_checked()

    def test_consumer_checkbox_toggle(self, page: Page):
        page.locator(AL.CHECKBOX_CONSUMER).check()
        expect(page.locator(AL.CHECKBOX_CONSUMER)).to_be_checked()
        page.locator(AL.CHECKBOX_CONSUMER).uncheck()
        expect(page.locator(AL.CHECKBOX_CONSUMER)).not_to_be_checked()

    def test_carrier_checkbox_toggle(self, page: Page):
        page.locator(AL.CHECKBOX_CARRIER).check()
        expect(page.locator(AL.CHECKBOX_CARRIER)).to_be_checked()
        page.locator(AL.CHECKBOX_CARRIER).uncheck()
        expect(page.locator(AL.CHECKBOX_CARRIER)).not_to_be_checked()

    def test_all_segment_checkboxes_can_be_checked_together(self, page: Page):
        """Checkboxes are independent — all three should be checkable at once."""
        page.locator(AL.CHECKBOX_ENTERPRISE).check()
        page.locator(AL.CHECKBOX_CONSUMER).check()
        page.locator(AL.CHECKBOX_CARRIER).check()
        expect(page.locator(AL.CHECKBOX_ENTERPRISE)).to_be_checked()
        expect(page.locator(AL.CHECKBOX_CONSUMER)).to_be_checked()
        expect(page.locator(AL.CHECKBOX_CARRIER)).to_be_checked()


# ── Solutions CTA Tests ───────────────────────────────────────────────────────

class TestSolutionsCTAs:

    def test_explore_enterprise_navigates(self, page: Page):
        page.locator(AL.LINK_EXPLORE_ENTERPRISE).click()
        expect(page).not_to_have_url(AL.ABOUT_URL)

    def test_explore_carrier_navigates(self, page: Page):
        page.goto(AL.ABOUT_URL)
        page.locator(AL.LINK_EXPLORE_CARRIER).click()
        expect(page).not_to_have_url(AL.ABOUT_URL)

    def test_explore_consumer_navigates(self, page: Page):
        page.goto(AL.ABOUT_URL)
        page.locator(AL.LINK_EXPLORE_CONSUMER).click()
        expect(page).not_to_have_url(AL.ABOUT_URL)


# ── Team Accordion Tests ──────────────────────────────────────────────────────

class TestTeamAccordion:

    def test_sales_team_expandable(self, page: Page):
        page.locator(AL.BTN_SALES_TEAM).click()
        expect(page.locator(AL.BTN_SALES_TEAM)).to_be_visible()

    def test_product_team_expandable(self, page: Page):
        page.locator(AL.BTN_PRODUCT_TEAM).click()
        expect(page.locator(AL.BTN_PRODUCT_TEAM)).to_be_visible()

    def test_leadership_team_expandable(self, page: Page):
        page.locator(AL.BTN_LEADERSHIP_TEAM).click()
        expect(page.locator(AL.BTN_LEADERSHIP_TEAM)).to_be_visible()


# ── Contact / Location Map Tests ──────────────────────────────────────────────

class TestLocationMap:

    @pytest.fixture(autouse=True)
    def open_connect_section(self, page: Page):
        page.locator(AL.LINK_LETS_CONNECT).click()
        page.wait_for_timeout(500)

    def test_uk_location_button_clickable(self, page: Page):
        page.locator(AL.BTN_UK_LOCATION).click()
        expect(page.locator(AL.BTN_UK_LOCATION)).to_be_visible()

    def test_zoom_in_clickable(self, page: Page):
        page.locator(AL.BTN_ZOOM_IN).click()
        expect(page.locator(AL.BTN_ZOOM_IN)).to_be_visible()

    def test_zoom_out_clickable(self, page: Page):
        page.locator(AL.BTN_ZOOM_OUT).click()
        expect(page.locator(AL.BTN_ZOOM_OUT)).to_be_visible()

    def test_reset_view_clickable(self, page: Page):
        page.locator(AL.BTN_ZOOM_IN).click()
        page.locator(AL.BTN_RESET_VIEW).click()
        expect(page.locator(AL.BTN_RESET_VIEW)).to_be_visible()