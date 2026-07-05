import pytest
from playwright.sync_api import Page, expect
from locators.communications_locators import (
    BASE_URL,
    HEADING_SAY_HELLO, HEADING_HEADQUARTERS, HEADING_EMAIL_ADDRESS,
    HEADING_PHONE, HEADING_SPEAK_FREELY,
    TEXT_MOPLEX, TEXT_ADDRESS,
    TEXT_JOB_INQUIRIES, TEXT_BUSINESS_INQUIRIES, TEXT_PRESS_INQUIRIES,
    TEXT_PRODUCT_INQUIRIES, TEXT_EVENTS_INQUIRIES,
    LINK_JOINUS, LINK_PARTNER, LINK_PRESS, LINK_SCM, LINK_EVENTS,
    LINK_LANDLINE, LINK_FAX,
    TEXT_SPEAK_FREELY,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Page Headings ──────────────────────────────────────────────────────────────

def test_heading_say_hello_visible(page: Page):
    expect(page.locator(HEADING_SAY_HELLO)).to_be_visible()

def test_heading_headquarters_visible(page: Page):
    expect(page.locator(HEADING_HEADQUARTERS)).to_be_visible()

def test_heading_email_address_visible(page: Page):
    expect(page.locator(HEADING_EMAIL_ADDRESS)).to_be_visible()

def test_heading_phone_visible(page: Page):
    expect(page.locator(HEADING_PHONE)).to_be_visible()

def test_heading_speak_freely_visible(page: Page):
    expect(page.locator(HEADING_SPEAK_FREELY)).to_be_visible()


# ── Headquarters ───────────────────────────────────────────────────────────────

def test_text_moplex_visible(page: Page):
    expect(page.locator(TEXT_MOPLEX)).to_be_visible()

def test_text_address_visible(page: Page):
    expect(page.locator(TEXT_ADDRESS)).to_be_visible()


# ── Email Inquiry Labels ───────────────────────────────────────────────────────

def test_text_job_inquiries_visible(page: Page):
    expect(page.locator(TEXT_JOB_INQUIRIES)).to_be_visible()

def test_text_business_inquiries_visible(page: Page):
    expect(page.locator(TEXT_BUSINESS_INQUIRIES)).to_be_visible()

def test_text_press_inquiries_visible(page: Page):
    expect(page.locator(TEXT_PRESS_INQUIRIES)).to_be_visible()

def test_text_product_inquiries_visible(page: Page):
    expect(page.locator(TEXT_PRODUCT_INQUIRIES)).to_be_visible()

def test_text_events_inquiries_visible(page: Page):
    expect(page.locator(TEXT_EVENTS_INQUIRIES)).to_be_visible()


# ── Email Links Visible ────────────────────────────────────────────────────────

def test_link_joinus_visible(page: Page):
    expect(page.locator(LINK_JOINUS)).to_be_visible()

def test_link_partner_visible(page: Page):
    expect(page.locator(LINK_PARTNER)).to_be_visible()

def test_link_press_visible(page: Page):
    expect(page.locator(LINK_PRESS)).to_be_visible()

def test_link_scm_visible(page: Page):
    expect(page.locator(LINK_SCM)).to_be_visible()

def test_link_events_visible(page: Page):
    expect(page.locator(LINK_EVENTS)).to_be_visible()


# ── Email Links href Checks ────────────────────────────────────────────────────

def test_link_joinus_href(page: Page):
    href = page.locator(LINK_JOINUS).get_attribute("href")
    assert "joinus@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_link_partner_href(page: Page):
    href = page.locator(LINK_PARTNER).get_attribute("href")
    assert "partnerwithus@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_link_press_href(page: Page):
    href = page.locator(LINK_PRESS).get_attribute("href")
    assert "press@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_link_scm_href(page: Page):
    href = page.locator(LINK_SCM).get_attribute("href")
    assert "scm.sourcing@momentgroup.ph" in href, f"Unexpected href: {href}"

def test_link_events_href(page: Page):
    href = page.locator(LINK_EVENTS).get_attribute("href")
    assert "events@momentgroup.ph" in href, f"Unexpected href: {href}"


# ── Phone Links Visible ────────────────────────────────────────────────────────

def test_link_landline_visible(page: Page):
    expect(page.locator(LINK_LANDLINE)).to_be_visible()

def test_link_fax_visible(page: Page):
    expect(page.locator(LINK_FAX)).to_be_visible()


# ── Phone Links href Checks ────────────────────────────────────────────────────

def test_link_landline_href(page: Page):
    href = page.locator(LINK_LANDLINE).get_attribute("href")
    assert "tel:" in href, f"Expected tel: href, got: {href}"

def test_link_fax_href(page: Page):
    href = page.locator(LINK_FAX).get_attribute("href")
    assert "tel:" in href or "fax:" in href, f"Unexpected href: {href}"


# ── Speak Freely Section ───────────────────────────────────────────────────────

def test_text_speak_freely_visible(page: Page):
    expect(page.locator(TEXT_SPEAK_FREELY)).to_be_visible()