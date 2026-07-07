import pytest
from playwright.sync_api import Page, expect
from MOMENTGROUP.locators.brands_manam_triangle_locators import (
    BASE_URL,
    IMG_BRAND,
    TEXT_ABOUT, HEADING_MUST_TRIES, TEXT_MUST_TRIES,
    LINK_BACK_BRANDS, LINK_HOURS_LOCATIONS, LINK_GALLERY,
    ICON_FACEBOOK, ICON_INSTAGRAM, BRAND_ICON_FIRST, SOCIAL_MEDIA_SECOND,
    HEADING_LOCATIONS_HOURS, HEADING_RESTAURANT_ARCADE, CARD_HOLDER,
    HEADING_GALLERY, IMG_GALLERY_FIRST, IMG_GALLERY_SECOND, PAGINATION_NUMBERS,
    SLIDE_01, SLIDE_02,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Brand Image ────────────────────────────────────────────────────────────────

def test_brand_image_visible(page: Page):
    expect(page.locator(IMG_BRAND)).to_be_visible()


# ── About Section ──────────────────────────────────────────────────────────────

def test_text_about_visible(page: Page):
    expect(page.locator(TEXT_ABOUT)).to_be_visible()

def test_heading_must_tries_visible(page: Page):
    expect(page.locator(HEADING_MUST_TRIES)).to_be_visible()

def test_text_must_tries_visible(page: Page):
    expect(page.locator(TEXT_MUST_TRIES)).to_be_visible()


# ── Navigation Links ───────────────────────────────────────────────────────────

def test_link_back_brands_visible(page: Page):
    expect(page.locator(LINK_BACK_BRANDS).first).to_be_attached()

def test_link_hours_locations_visible(page: Page):
    expect(page.locator(LINK_HOURS_LOCATIONS)).to_be_visible()

def test_link_gallery_visible(page: Page):
    expect(page.locator(LINK_GALLERY)).to_be_visible()


# ── Social Media ───────────────────────────────────────────────────────────────

def test_icon_facebook_visible(page: Page):
    expect(page.locator(ICON_FACEBOOK)).to_be_visible()

def test_icon_instagram_visible(page: Page):
    expect(page.locator(ICON_INSTAGRAM)).to_be_visible()

def test_brand_icon_first_visible(page: Page):
    expect(page.locator(BRAND_ICON_FIRST).first).to_be_visible()

def test_social_media_second_visible(page: Page):
    expect(page.locator(SOCIAL_MEDIA_SECOND)).to_be_visible()

def test_facebook_opens_new_tab(page: Page):
    with page.expect_popup() as popup_info:
        page.locator(ICON_FACEBOOK).click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    assert "facebook.com" in popup.url, f"Expected Facebook, got: {popup.url}"

def test_instagram_opens_new_tab(page: Page):
    with page.expect_popup() as popup_info:
        page.locator(ICON_INSTAGRAM).click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    assert "instagram.com" in popup.url, f"Expected Instagram, got: {popup.url}"


# ── Locations & Hours Section ──────────────────────────────────────────────────

def test_heading_locations_hours_visible(page: Page):
    expect(page.locator(HEADING_LOCATIONS_HOURS)).to_be_visible()

def test_heading_restaurant_arcade_visible(page: Page):
    expect(page.locator(HEADING_RESTAURANT_ARCADE).first).to_be_visible()

def test_card_holder_visible(page: Page):
    expect(page.locator(CARD_HOLDER)).to_be_visible()


# ── Gallery Section ────────────────────────────────────────────────────────────

def test_heading_gallery_visible(page: Page):
    expect(page.locator(HEADING_GALLERY)).to_be_visible()

def test_gallery_img_first_visible(page: Page):
    expect(page.locator(IMG_GALLERY_FIRST).first).to_be_visible()

def test_gallery_img_second_visible(page: Page):
    expect(page.locator(IMG_GALLERY_SECOND)).to_be_visible()

def test_pagination_numbers_visible(page: Page):
    expect(page.locator(PAGINATION_NUMBERS)).to_be_visible()

def test_slide_01_attached(page: Page):
    expect(page.locator(SLIDE_01)).to_be_attached()

def test_slide_02_attached(page: Page):
    expect(page.locator(SLIDE_02)).to_be_attached()

def test_slide_01_clickable(page: Page):
    page.locator(SLIDE_01).click()
    page.wait_for_timeout(300)

def test_slide_02_clickable(page: Page):
    page.locator(SLIDE_02).click()
    page.wait_for_timeout(300)