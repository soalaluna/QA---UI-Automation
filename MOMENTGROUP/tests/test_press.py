import pytest
from playwright.sync_api import Page, expect
from locators.press_locators import *

@pytest.fixture(autouse=True)
def navigate(page: Page):
    """Navigates to the press page before each test."""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Core Layout & Visibility Tests ────────────────────────────────────────────

def test_press_page_layout_visible(page: Page):
    """Verifies all static text, headings, and dropdowns load correctly."""
    expect(page.locator(HEADING_PRESS_COL1)).to_be_visible()
    expect(page.locator(HEADING_PRESS_COL2)).to_be_visible()
    expect(page.locator(HEADING_INQUIRIES)).to_be_visible()
    expect(page.locator(TEXT_INQUIRIES)).to_be_visible()
    expect(page.locator(LINK_EMAIL)).to_be_visible()
    expect(page.locator(DROPDOWN_BRANDS)).to_be_visible()

def test_default_articles_visible(page: Page):
    """Verifies a sample of the default loaded articles are visible."""
    default_articles = [
        "role=link[name*='May 2026 | PhilStar']",
        "role=link[name*='April 2026 | Metro.style']",
        "role=link[name*='March 2026 | Nikkei Asia']",
        "role=link[name*='December 2025 | Rolling Stone']",
        "role=link[name*='November 2025 | Business World']",
        "role=link[name*='October 2025 | Spot.ph']",
        "role=link[name*='August 2025 | Spot.ph Ooma']"
    ]
    for article in default_articles:
        expect(page.locator(article).first).to_be_visible()


# ── Brand Filtering & Popup Tests ─────────────────────────────────────────────

def test_filter_8cuts(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("8Cuts")
    expect(page.locator("role=link[name*='September 2025 | ABS-CBN News']")).to_be_visible()
    expect(page.locator("role=link[name*='July 2025 | Spot.ph']")).to_be_visible()

def test_filter_and_click_ooma(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("Ooma")
    
    links_to_test = [LINK_OOMA_SPOT, LINK_OOMA_PHILSTAR, LINK_OOMA_ABSCBN]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close() # Close tab to save memory

def test_filter_and_click_din_tai_fung(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("Din Tai Fung")
    
    links_to_test = [LINK_DTF_INQUIRER, LINK_DTF_GMA, LINK_DTF_BIZWORLD]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_filter_and_click_mo_cookies(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("Mo’ Cookies")
    
    links_to_test = [LINK_MO_ABSCBN, LINK_MO_SPOT_APR, LINK_MO_SPOT_JUN]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_filter_and_click_the_moment_group(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("The Moment Group")
    
    links_to_test = [LINK_TMG_RAPPLER, LINK_TMG_PHILIPPINE, LINK_TMG_LIFESTYLE]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_filter_and_click_pancit_pancitan(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("Pancit Pancitan")
    
    links_to_test = [LINK_PP_GENZ, LINK_PP_ABSCBN, LINK_PP_GENERIC]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_filter_and_click_mama_nams(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("Mama Nams")
    
    links_to_test = [LINK_MAMA_PHIL, LINK_MAMA_TATLER, LINK_MAMA_TATLER_ASIA]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_filter_and_click_hayop(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("hayop")
    
    links_to_test = [LINK_HAYOP_IWANDER, LINK_HAYOP_MICHELIN, LINK_HAYOP_PHILSTAR]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_filter_and_click_mess_hall(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("The Mess Hall")
    
    expect(page.locator(LINK_MESS_HALL)).to_be_visible()
    with page.expect_popup() as popup_info:
        page.locator(LINK_MESS_HALL).click()
    popup_info.value.close()

def test_filter_and_click_moment_catering(page: Page):
    page.locator(DROPDOWN_BRANDS).select_option("Moment Catering")
    
    expect(page.locator(LINK_CATERING_RAPPLER)).to_be_visible()
    expect(page.locator(LINK_CATERING_TATLER)).to_be_visible()
    
    links_to_test = [LINK_CATERING_RAPPLER, LINK_CATERING_TATLER]
    for link in links_to_test:
        with page.expect_popup() as popup_info:
            page.locator(link).click()
        popup_info.value.close()

def test_email_link_opens_popup(page: Page):
    """Verifies clicking the inquiries email address triggers the mailto intent/popup."""
    with page.expect_popup() as popup_info:
        page.locator(LINK_EMAIL).click()
    popup_info.value.close()