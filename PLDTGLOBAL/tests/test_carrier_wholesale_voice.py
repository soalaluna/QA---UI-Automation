import pytest
from playwright.sync_api import Page, expect
from locators.carrier_wholesale_voice_locators import (
    BASE_URL,
    LINK_CARRIER, SPAN_WHOLESALE_VOICE,
    HEADING_WHOLESALE_VOICE, TEXT_INTRO,
    IMG_BACK_SECTION,
    TEXT_PRODUCTS_LABEL,
    TEXT_INTL_VOICE, TEXT_VOICE_VAS_TOLL_FREE, TEXT_VOICE_VAS_LNS,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Breadcrumbs ────────────────────────────────────────────────────────────────

def test_carrier_breadcrumb_visible(page: Page):
    expect(page.locator(LINK_CARRIER)).to_be_visible()

def test_wholesale_voice_breadcrumb_span_visible(page: Page):
    expect(page.locator(SPAN_WHOLESALE_VOICE)).to_be_visible()


# ── Page Content ───────────────────────────────────────────────────────────────

def test_heading_wholesale_voice_visible(page: Page):
    expect(page.locator(HEADING_WHOLESALE_VOICE)).to_be_visible()

def test_intro_text_visible(page: Page):
    expect(page.locator(TEXT_INTRO)).to_be_visible()


# ── Back Section Image ─────────────────────────────────────────────────────────

def test_back_section_image_visible(page: Page):
    expect(page.locator(IMG_BACK_SECTION)).to_be_visible()


# ── Products & Services Section ────────────────────────────────────────────────

def test_products_label_visible(page: Page):
    expect(page.locator(TEXT_PRODUCTS_LABEL).first).to_be_visible()

def test_international_voice_termination_visible(page: Page):
    expect(page.locator(TEXT_INTL_VOICE)).to_be_visible()

def test_voice_vas_toll_free_visible(page: Page):
    expect(page.locator(TEXT_VOICE_VAS_TOLL_FREE)).to_be_visible()

def test_voice_vas_lns_visible(page: Page):
    expect(page.locator(TEXT_VOICE_VAS_LNS)).to_be_visible()