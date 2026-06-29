import pytest
from playwright.sync_api import Page, expect
from locators.carrier_locators import *

BASE_URL = "https://www.pldtglobal.com/en"


@pytest.fixture(autouse=True)
def navigate_to_carrier(page: Page):
    """Navigate to Carrier page before each test"""
    page.goto(CARRIER_URL)
    page.wait_for_load_state("networkidle")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

def test_carrier_page_loads(page: Page):
    """Carrier page should load at correct URL"""
    expect(page).to_have_url(CARRIER_URL)


# ── Learn More Links ──────────────────────────────────────────────────────────

def test_learn_more_first_visible(page: Page):
    """First Learn More button should be visible"""
    expect(page.get_by_role("link", name="Learn More").first).to_be_visible()

def test_learn_more_first_does_not_navigate(page: Page):
    """First Learn More button is non-functional — clicking should keep the user on the carrier page"""
    page.get_by_role("link", name="Learn More").first.click()
    page.wait_for_timeout(1000)
    assert page.url == CARRIER_URL, f"Expected to stay on carrier page, got: {page.url}"

def test_learn_more_second_visible(page: Page):
    """Second Learn More button should be visible"""
    expect(page.get_by_role("link", name="Learn More").nth(1)).to_be_visible()

def test_learn_more_second_navigates_to_wholesale_voice(page: Page):
    """Second Learn More button should navigate to Wholesale Voice page"""
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_role("link", name="Learn More").nth(1).click()
    assert "wholesale-voice" in page.url.lower(), f"Expected wholesale-voice page, got: {page.url}"


# ── Sub-page Carrier Link ─────────────────────────────────────────────────────

def test_carrier_link_in_main_navigates_back(page: Page):
    """Carrier link in main content (on Wholesale Voice page) should navigate back to Carrier page"""
    page.get_by_role("link", name="Learn More").nth(1).click()
    page.wait_for_load_state("networkidle")
    page.locator(CARRIER_LINK_MAIN).click()
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(CARRIER_URL)