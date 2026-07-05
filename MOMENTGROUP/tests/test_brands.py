import pytest
from playwright.sync_api import Page, expect
from locators.brands_locators import (
    BASE_URL, BRAND_1, BRAND_2, BRAND_3, BRAND_4, BRAND_5, 
    BRAND_6, BRAND_7, BRAND_8, BRAND_9, BRAND_10, BRAND_11
)

@pytest.fixture(autouse=True)
def navigate(page: Page):
    """Navigates to the brands page before each test."""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Visibility Tests ──────────────────────────────────────────────────────────

def test_brands_grid_visible(page: Page):
    """Asserts that every brand item is physically visible on the screen."""
    expect(page.locator(BRAND_1)).to_be_visible()
    expect(page.locator(BRAND_2)).to_be_visible()
    expect(page.locator(BRAND_3)).to_be_visible()
    expect(page.locator(BRAND_4)).to_be_visible()
    expect(page.locator(BRAND_5)).to_be_visible()
    expect(page.locator(BRAND_6)).to_be_visible()
    expect(page.locator(BRAND_7)).to_be_visible()
    expect(page.locator(BRAND_8)).to_be_visible()
    expect(page.locator(BRAND_9)).to_be_visible()
    expect(page.locator(BRAND_10)).to_be_visible()
    expect(page.locator(BRAND_11)).to_be_visible()


# ── Click & Navigation Tests ──────────────────────────────────────────────────

def test_brands_grid_clicks(page: Page):
    """
    Tests clicking each brand and returning to the base URL 
    to prevent navigation timeouts.
    """
    brands = [
        BRAND_1, BRAND_2, BRAND_3, BRAND_4, BRAND_5, 
        BRAND_6, BRAND_7, BRAND_8, BRAND_9, BRAND_10, BRAND_11
    ]
    
    for brand in brands:
        # Click the individual brand
        page.locator(brand).click()
        
        # Navigate back to the brands page to reset the DOM for the next click
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")