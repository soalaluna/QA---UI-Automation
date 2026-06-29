import pytest
from playwright.sync_api import Page, expect
from locators.loyalty_locators import (
    BASE_URL, LOYALTY_URL,
    NAV_LOYALTY,
    MOMENT_CARD_IMG, MOMENT_CARD_LINK,
)


# ── Nav to Loyalty ────────────────────────────────────────────────────────────

def test_loyalty_nav_link_visible(page: Page):
    """Loyalty link should be visible in the navigation"""
    page.goto(BASE_URL)
    expect(page.locator(NAV_LOYALTY)).to_be_visible()

def test_loyalty_nav_link_navigates(page: Page):
    """Clicking Loyalty nav link should navigate to the loyalty page"""
    page.goto(BASE_URL)
    page.locator(NAV_LOYALTY).click()
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(LOYALTY_URL)


# ── Loyalty Page Content ──────────────────────────────────────────────────────

def test_moment_card_image_visible(page: Page):
    """Moment Card image should be visible on the loyalty page"""
    page.goto(LOYALTY_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(MOMENT_CARD_IMG)).to_be_visible()

def test_moment_card_image_attached(page: Page):
    """Moment Card image should be attached to the DOM"""
    page.goto(LOYALTY_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(MOMENT_CARD_IMG)).to_be_attached()

def test_moment_card_link_visible(page: Page):
    """momentcard.ph link should be visible on the loyalty page"""
    page.goto(LOYALTY_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(MOMENT_CARD_LINK)).to_be_visible()

def test_moment_card_link_has_correct_href(page: Page):
    """momentcard.ph link should point to the correct URL"""
    page.goto(LOYALTY_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(MOMENT_CARD_LINK).get_attribute("href")
    assert "momentcard.ph" in href, f"Expected momentcard.ph link, got: {href}"

def test_moment_card_link_navigates(page: Page):
    """momentcard.ph link should navigate to momentcard.ph"""
    page.goto(LOYALTY_URL)
    page.wait_for_load_state("networkidle")
    page.locator(MOMENT_CARD_LINK).click()
    page.wait_for_load_state("networkidle")
    assert "momentcard.ph" in page.url, f"Expected momentcard.ph in URL, got: {page.url}"