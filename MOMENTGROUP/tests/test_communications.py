import pytest
from playwright.sync_api import Page, expect
from locators.communications_locators import (
    BASE_URL, COMMUNICATIONS_URL,
    NAV_COMMUNICATIONS,
    EMAIL_JOINUS, EMAIL_PARTNER, EMAIL_PRESS, EMAIL_SCM, EMAIL_EVENTS,
)


# ── Nav to Communications ─────────────────────────────────────────────────────

def test_communications_nav_link_visible(page: Page):
    """Communications link should be visible in the navigation"""
    page.goto(BASE_URL)
    expect(page.locator(NAV_COMMUNICATIONS)).to_be_visible()

def test_communications_nav_link_navigates(page: Page):
    """Clicking Communications nav link should navigate to the communications page"""
    page.goto(BASE_URL)
    page.locator(NAV_COMMUNICATIONS).click()
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(COMMUNICATIONS_URL)


# ── Email Links Visible ───────────────────────────────────────────────────────

def test_email_joinus_visible(page: Page):
    """joinus@momentgroup.ph email link should be visible"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(EMAIL_JOINUS)).to_be_visible()

def test_email_partner_visible(page: Page):
    """partnerwithus@momentgroup.ph email link should be visible"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(EMAIL_PARTNER)).to_be_visible()

def test_email_press_visible(page: Page):
    """press@momentgroup.ph email link should be visible"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(EMAIL_PRESS)).to_be_visible()

def test_email_scm_visible(page: Page):
    """scm.sourcing@momentgroup.ph email link should be visible"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(EMAIL_SCM)).to_be_visible()

def test_email_events_visible(page: Page):
    """events@momentgroup.ph email link should be visible"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(EMAIL_EVENTS)).to_be_visible()


# ── Email Links href Checks ───────────────────────────────────────────────────

def test_email_joinus_href(page: Page):
    """joinus link should have correct mailto href"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(EMAIL_JOINUS).get_attribute("href")
    assert "joinus@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_email_partner_href(page: Page):
    """partnerwithus link should have correct mailto href"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(EMAIL_PARTNER).get_attribute("href")
    assert "partnerwithus@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_email_press_href(page: Page):
    """press link should have correct mailto href"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(EMAIL_PRESS).get_attribute("href")
    assert "press@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_email_scm_href(page: Page):
    """scm.sourcing link should have correct mailto href"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(EMAIL_SCM).get_attribute("href")
    assert "scm.sourcing@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_email_events_href(page: Page):
    """events link should have correct mailto href"""
    page.goto(COMMUNICATIONS_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(EMAIL_EVENTS).get_attribute("href")
    assert "events@momentgroup.ph" in href, f"Unexpected href: {href}"