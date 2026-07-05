import pytest
from playwright.sync_api import Page, expect
from locators.loyalty_locators import (
    BASE_URL,
    HEADING_MOMENT_CARD,
    TEXT_INTRO,
    LINK_MOMENT_CARD, IMG_MOMENT_CARD,
    LOYALTY_FRAME,
    HEADING_DISCOUNT_COUPON, TEXT_DISCOUNT_COUPON,
    HEADING_DISCOUNTS_POINTS, TEXT_DISCOUNTS_POINTS,
    HEADING_EXCLUSIVE_REWARDS, TEXT_EXCLUSIVE_REWARDS,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Page Heading ───────────────────────────────────────────────────────────────

def test_heading_moment_card_visible(page: Page):
    expect(page.locator(HEADING_MOMENT_CARD)).to_be_visible()


# ── Intro Text ─────────────────────────────────────────────────────────────────

def test_intro_text_visible(page: Page):
    expect(page.locator(TEXT_INTRO)).to_be_visible()


# ── Moment Card Link ───────────────────────────────────────────────────────────

def test_moment_card_link_visible(page: Page):
    expect(page.locator(LINK_MOMENT_CARD)).to_be_visible()

def test_moment_card_link_has_href(page: Page):
    href = page.locator(LINK_MOMENT_CARD).get_attribute("href")
    assert "momentcard.ph" in href, f"Unexpected href: {href}"

def test_moment_card_link_navigates(page: Page):
    page.locator(LINK_MOMENT_CARD).click()
    page.wait_for_timeout(2000)
    assert "momentcard.ph" in page.url, f"Expected momentcard.ph, got: {page.url}"


# ── Moment Card Image ──────────────────────────────────────────────────────────

def test_moment_card_image_visible(page: Page):
    expect(page.locator(IMG_MOMENT_CARD)).to_be_visible()


# ── Loyalty Frame ──────────────────────────────────────────────────────────────

def test_loyalty_frame_visible(page: Page):
    expect(page.locator(LOYALTY_FRAME)).to_be_visible()


# ── Discount Coupon Section ────────────────────────────────────────────────────

def test_heading_discount_coupon_visible(page: Page):
    expect(page.locator(HEADING_DISCOUNT_COUPON)).to_be_visible()

def test_text_discount_coupon_visible(page: Page):
    expect(page.locator(TEXT_DISCOUNT_COUPON)).to_be_visible()


# ── Discounts & Points Section ─────────────────────────────────────────────────

def test_heading_discounts_points_visible(page: Page):
    expect(page.locator(HEADING_DISCOUNTS_POINTS)).to_be_visible()

def test_text_discounts_points_visible(page: Page):
    expect(page.locator(TEXT_DISCOUNTS_POINTS)).to_be_visible()


# ── Exclusive Rewards Section ──────────────────────────────────────────────────

def test_heading_exclusive_rewards_visible(page: Page):
    expect(page.locator(HEADING_EXCLUSIVE_REWARDS)).to_be_visible()

def test_text_exclusive_rewards_visible(page: Page):
    expect(page.locator(TEXT_EXCLUSIVE_REWARDS)).to_be_visible()