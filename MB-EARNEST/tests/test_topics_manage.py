import re
import pytest
from playwright.sync_api import Page, expect

# --- Constants ---
BASE_URL = "https://earnest.metrobank.com.ph/topics/manage"

# --- Helper Components ---

def verify_structural_elements(page: Page) -> None:
    """Verifies the visibility of core structural and text elements securely."""
    expect(page.locator(".header")).to_be_visible()
    
    # Removed the brittle .nth(5) logic and replaced with robust heading checks
    headings = [
        "Manage",
        "Let us get better with money",
        "Everything starts with a budget",
        "Put Earnest in your pocket"
    ]
    for heading in headings:
        expect(page.get_by_role("heading", name=re.compile(heading, re.IGNORECASE)).first).to_be_visible()


def verify_article_links(page: Page) -> None:
    """Verifies that the article links are visible and interactable."""
    # 1. FIXED: Updated to the actual Top 3 articles currently on the live site
    article_links = [
        "What does hiya have to do",
        "Overcoming challenges as a breadwinner",
        "Small steps today",
        "Read all articles"
    ]

    for link_name in article_links:
        # 2. FIXED: Changed .first to .last
        # This bypasses the hidden mobile layout and targets the visible desktop layout!
        link = page.get_by_role("link", name=re.compile(link_name, re.IGNORECASE)).last
        expect(link).to_be_visible()


def verify_downloads_and_resources(page: Page) -> None:
    """Tests the download templates and E-book popup."""
    expect(page.get_by_role("link", name="Get the Earnest E-book").last).to_be_visible()

    # 1. Budget Template Download (which also triggers a popup)
    with page.expect_download() as download_info:
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Download budget template").last.click()
    
    # Assert download exists and close the generated popup to free memory
    assert download_info.value is not None
    popup_info.value.close()

    # 2. Earnest E-book Popup
    with page.expect_popup() as ebook_popup_info:
        page.get_by_role("link", name="Get the Earnest E-book").last.click()
    ebook_popup_info.value.close()


def verify_external_popups(page: Page) -> None:
    """Loops through social and external footer links that open in new tabs."""
    # Scroll down to ensure lazy-loaded footer links are interactive
    page.keyboard.press("End")
    page.wait_for_timeout(500)
    
    locators_to_click = [
        page.locator(".social-item > li > a").nth(0),
        page.locator(".social-item > li > a").nth(1),
        page.locator(".social-item > li > a").nth(2),
        page.locator(".social-item > li > a").nth(3),
        page.locator(".social-item > li > a").nth(4),
        page.get_by_role("link", name="Visit Metrobank site").last,
        page.get_by_role("link", name="www.bsp.gov.ph").last
    ]

    for locator in locators_to_click:
        with page.expect_popup() as popup_info:
            locator.click(force=True)
        # Instantly close the new tab so the browser doesn't consume excess RAM
        popup_info.value.close()


# --- Main Pytest Function ---

def test_metrobank_manage_page(page: Page) -> None:
    """
    Main test execution that calls inclusive component functions.
    """
    # Navigate to the page once
    page.goto(BASE_URL)

    # Verify UI components
    verify_structural_elements(page)

    # Interact with main articles
    verify_article_links(page)

    # Handle downloads & resources
    verify_downloads_and_resources(page)

    # Handle external social and footer popups
    verify_external_popups(page)