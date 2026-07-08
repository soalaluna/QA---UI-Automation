import pytest
from playwright.sync_api import Page, expect
from locators.consumer_epadala_locators import (
    BASE_URL,
    LINK_CONSUMER, SPAN_EPADALA,
    HEADING_EPADALA, TEXT_INTRO,
    LINK_LEARN_MORE,
    IMG_BACK_SECTION,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Breadcrumbs ────────────────────────────────────────────────────────────────

def test_consumer_breadcrumb_visible(page: Page):
    expect(page.locator(LINK_CONSUMER).first).to_be_visible()

def test_epadala_breadcrumb_span_visible(page: Page):
    expect(page.locator(SPAN_EPADALA)).to_be_visible()


# ── Page Content ───────────────────────────────────────────────────────────────

def test_heading_epadala_visible(page: Page):
    expect(page.locator(HEADING_EPADALA)).to_be_visible()

def test_intro_text_visible(page: Page):
    expect(page.locator(TEXT_INTRO)).to_be_visible()


# ── Learn More Link ────────────────────────────────────────────────────────────

def test_learn_more_link_visible(page: Page):
    expect(page.locator(LINK_LEARN_MORE)).to_be_visible()

def test_learn_more_link_navigates(page: Page):
    page.locator(LINK_LEARN_MORE).click()
    # tinbo.ph is a SPA that never reaches networkidle —
    # domcontentloaded and load both fire, so just verify URL changed
    page.wait_for_load_state("domcontentloaded", timeout=15000)
    assert page.url != BASE_URL, f"Expected navigation away from page, got: {page.url}"


# ── Back Section Image ─────────────────────────────────────────────────────────

def test_back_section_image_visible(page: Page):
    expect(page.locator(IMG_BACK_SECTION)).to_be_visible()