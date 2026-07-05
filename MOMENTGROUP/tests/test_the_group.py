import pytest
from playwright.sync_api import Page, expect
from locators.the_group_locators import *

@pytest.fixture(autouse=True)
def navigate(page: Page):
    """Navigates to the base page before each test."""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


def test_hero_and_breadcrumbs_visible(page: Page):
    expect(page.locator(HEADING_MAIN)).to_be_visible()
    expect(page.locator(TEXT_QUOTE)).to_be_visible()
    expect(page.locator(BREADCRUMB_THE_GROUP)).to_be_visible()
    expect(page.locator(BREADCRUMB_ABOUT)).to_be_visible()
    expect(page.locator(BREADCRUMB_PARTNERSHIPS)).to_be_visible()
    expect(page.locator(BREADCRUMB_MILESTONES)).to_be_visible()


def test_founders_section_visible(page: Page):
    page.goto(f"{BASE_URL}#founders")
    
    expect(page.locator(HEADING_FOUNDERS)).to_be_visible()
    
    # Abba Napa
    expect(page.locator(HEADING_ABBA)).to_be_visible()
    expect(page.locator(TEXT_ABBA_TITLE)).to_be_visible()
    expect(page.locator(TEXT_ABBA_DESC_1)).to_be_visible()
    expect(page.locator(TEXT_ABBA_DESC_2)).to_be_visible()
    expect(page.locator(TEXT_ABBA_DESC_3)).to_be_visible()
    
    # Eliza Antonino
    expect(page.locator(HEADING_ELIZA)).to_be_visible()
    expect(page.locator(TEXT_ELIZA_TITLE)).to_be_visible()
    expect(page.locator(TEXT_ELIZA_DESC_1)).to_be_visible()
    expect(page.locator(TEXT_ELIZA_DESC_2)).to_be_visible()
    expect(page.locator(TEXT_ELIZA_DESC_3).locator("span")).to_be_visible()
    
    # Jon Syjuco
    expect(page.locator(HEADING_JON)).to_be_visible()
    expect(page.locator(TEXT_JON_TITLE)).to_be_visible()
    expect(page.locator(TEXT_JON_DESC_1)).to_be_visible()
    expect(page.locator(TEXT_JON_DESC_2)).to_be_visible()


def test_about_section_visible(page: Page):
    page.goto(f"{BASE_URL}#about")
    
    expect(page.locator(HEADING_ABOUT)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_1)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_2)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_3)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_4)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_5)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_6)).to_be_visible()
    expect(page.locator(TEXT_ABOUT_7)).to_be_visible()


def test_partnerships_section_visible(page: Page):
    page.goto(f"{BASE_URL}#partnerships")
    
    expect(page.locator(HEADING_PARTNERSHIPS)).to_be_visible()
    expect(page.locator(TEXT_PARTNERSHIPS)).to_be_visible()


def test_milestones_slider_interactions(page: Page):
    page.goto(f"{BASE_URL}#milestones")
    
    expect(page.locator(HEADING_MILESTONES)).to_be_visible()
    expect(page.locator(BTN_PREVIOUS)).to_be_visible()
    expect(page.locator(BTN_NEXT)).to_be_visible()
    
    # Check 2012
    expect(page.locator(YEAR_2012)).to_be_visible()
    expect(page.locator(IMG_2012)).to_be_visible()
    expect(page.locator(TEXT_2012)).to_be_visible()
    
    # Check 2013
    expect(page.locator(YEAR_2013)).to_be_visible()
    expect(page.locator(IMG_2013)).to_be_visible()
    expect(page.locator(TEXT_2013)).to_be_visible()

    # Click Next and Check 2016
    page.locator(BTN_NEXT).click()
    expect(page.locator(YEAR_2016)).to_be_visible()
    expect(page.locator(IMG_2016)).to_be_visible()
    expect(page.locator(TEXT_2016)).to_be_visible()
    
# Navigate deeply into the slider
    for _ in range(5):
        # force=True ensures the click registers even if the button is animating
        page.locator(BTN_NEXT).click(force=True)
        page.wait_for_timeout(800) # Give the slider ample time to settle
    
    # Check 2021
    expect(page.locator(YEAR_2021)).to_be_visible()
    expect(page.locator(TEXT_2021)).to_be_visible()

    # Test Previous button functionality
    for _ in range(3):
        page.locator(BTN_PREVIOUS).click(force=True)
        page.wait_for_timeout(800)