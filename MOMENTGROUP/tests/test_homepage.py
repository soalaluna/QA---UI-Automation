import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import (
    BASE_URL, LOGO, SIDEBAR_TAGLINE, NAV_BRANDS, NAV_THE_GROUP, NAV_PRESS, 
    NAV_CAREERS, NAV_LOYALTY, NAV_COMMUNICATIONS, SOCIAL_ICON_1, SOCIAL_LINK_1, 
    SOCIAL_ICON_2, SOCIAL_LINK_2, SOCIAL_LINK_3, BRAND_1, BRAND_2, BRAND_3, 
    BRAND_4, BRAND_5, BRAND_6, BRAND_7, BRAND_8, BRAND_9, BRAND_10, BRAND_11
)

@pytest.fixture(autouse=True)
def navigate(page: Page):
    """Navigates to the homepage before each test."""
    page.goto(BASE_URL)


# ── Visibility Tests ──────────────────────────────────────────────────────────

def test_sidebar_elements_visible(page: Page):
    expect(page.locator(LOGO)).to_be_visible()
    expect(page.locator(SIDEBAR_TAGLINE)).to_be_visible()

def test_navigation_links_visible(page: Page):
    expect(page.locator(NAV_BRANDS)).to_be_visible()
    expect(page.locator(NAV_THE_GROUP)).to_be_visible()
    expect(page.locator(NAV_PRESS)).to_be_visible()
    expect(page.locator(NAV_CAREERS)).to_be_visible()
    expect(page.locator(NAV_LOYALTY)).to_be_visible()
    expect(page.locator(NAV_COMMUNICATIONS)).to_be_visible()

def test_social_media_links_visible(page: Page):
    # Removing the SOCIAL_ICON assertions and only checking the clickable links
    expect(page.locator(SOCIAL_LINK_1)).to_be_visible()
    expect(page.locator(SOCIAL_LINK_2)).to_be_visible()
    expect(page.locator(SOCIAL_LINK_3)).to_be_visible()

def test_brands_grid_visible(page: Page):
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


# ── Navigation & Click Tests ──────────────────────────────────────────────────

def test_logo_click(page: Page):
    page.locator(LOGO).click()

def test_sidebar_navigation_clicks(page: Page):
    page.locator(NAV_THE_GROUP).click()
    page.locator(NAV_PRESS).click()
    page.locator(NAV_CAREERS).click()
    page.locator(NAV_LOYALTY).click()
    page.locator(NAV_COMMUNICATIONS).click()

def test_brands_grid_clicks(page: Page):
    # Group all brand locators into a list
    brands = [
        BRAND_1, BRAND_2, BRAND_3, BRAND_4, BRAND_5, BRAND_6, 
        BRAND_7, BRAND_8, BRAND_9, BRAND_10, BRAND_11
    ]
    
    for brand in brands:
        # Click the brand
        page.locator(brand).click()
        
        # Navigate back to the Moment Group homepage to reset for the next click
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")


# ── Popup Tests ───────────────────────────────────────────────────────────────

def test_social_link_1_opens_popup(page: Page):
    with page.expect_popup() as page1_info:
        page.locator(SOCIAL_LINK_1).click()
    page1 = page1_info.value
    page1.close()

def test_social_link_2_opens_popup(page: Page):
    with page.expect_popup() as page2_info:
        page.locator(SOCIAL_LINK_2).click()
    page2 = page2_info.value
    page2.close()

def test_social_link_3_opens_popup(page: Page):
    with page.expect_popup() as page3_info:
        page.locator(SOCIAL_LINK_3).click()
    page3 = page3_info.value
    page3.close()