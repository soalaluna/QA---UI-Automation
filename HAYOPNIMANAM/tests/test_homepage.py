import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import (
    BASE_URL,
    LOGO_HOMEPAGE,
    NAV_MENU, NAV_ABOUT, NAV_PRESS, NAV_CONTACT, NAV_RESERVATIONS, NAV_ORDER_ONLINE,
    HERO_HEADING, HERO_MAKE_RESERVATION, HERO_ORDER_ONLINE, HERO_SEE_MENU,
    IMG_INASAL, IMG_LAND, IMG_EAGLE, IMG_MIDNIGHT_ADOBO,
    IMG_YELLOW_FLOWER, IMG_TREE_BRANCH, IMG_FISH, IMG_BANANA_TREE,
    IMG_KALABAW, IMG_HEADLINE, IMG_LANDING_ARTWORK_10_3, IMG_PINK_FLOWER,
    FOOTER_SOCIALS_ICON, FOOTER_TAGLINE, FOOTER_ADDRESS,
    FOOTER_PRIVACY, FOOTER_TERMS,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Logo ──────────────────────────────────────────────────────────────────────

def test_logo_visible(page: Page):
    expect(page.locator(LOGO_HOMEPAGE)).to_be_visible()

def test_logo_navigates_to_homepage(page: Page):
    page.locator(LOGO_HOMEPAGE).click()
    page.wait_for_load_state("networkidle")
    assert page.url == BASE_URL, f"Expected homepage, got: {page.url}"


# ── Navigation Visibility ──────────────────────────────────────────────────────

def test_nav_menu_visible(page: Page):
    expect(page.locator(NAV_MENU)).to_be_visible()

def test_nav_about_visible(page: Page):
    expect(page.locator(NAV_ABOUT)).to_be_visible()

def test_nav_press_visible(page: Page):
    expect(page.locator(NAV_PRESS)).to_be_visible()

def test_nav_contact_visible(page: Page):
    expect(page.locator(NAV_CONTACT)).to_be_visible()

def test_nav_reservations_visible(page: Page):
    expect(page.locator(NAV_RESERVATIONS)).to_be_visible()

def test_nav_order_online_visible(page: Page):
    expect(page.locator(NAV_ORDER_ONLINE)).to_be_visible()


# ── Navigation Behavior ────────────────────────────────────────────────────────

def test_nav_menu_navigates(page: Page):
    page.locator(NAV_MENU).click()
    page.wait_for_load_state("networkidle")
    assert "menu" in page.url.lower(), f"Expected menu page, got: {page.url}"

def test_nav_about_navigates(page: Page):
    page.locator(NAV_ABOUT).click()
    page.wait_for_load_state("networkidle")
    assert "who-we-are" in page.url.lower(), f"Expected about page, got: {page.url}"

def test_nav_press_navigates(page: Page):
    page.locator(NAV_PRESS).click()
    page.wait_for_load_state("networkidle")
    assert "press" in page.url.lower(), f"Expected press page, got: {page.url}"

def test_nav_contact_navigates(page: Page):
    page.locator(NAV_CONTACT).click()
    page.wait_for_load_state("networkidle")
    assert "contact" in page.url.lower(), f"Expected contact page, got: {page.url}"

def test_nav_reservations_navigates(page: Page):
    page.locator(NAV_RESERVATIONS).click()
    page.wait_for_load_state("networkidle")
    assert "reservation" in page.url.lower(), f"Expected reservation page, got: {page.url}"

def test_nav_order_online_opens_new_tab(page: Page):
    with page.expect_popup() as popup_info:
        page.locator(NAV_ORDER_ONLINE).click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    assert "atlas.kitchen" in popup.url, f"Expected order online site, got: {popup.url}"


# ── Hero Section ──────────────────────────────────────────────────────────────

def test_hero_heading_visible(page: Page):
    expect(page.locator(HERO_HEADING)).to_be_visible()

def test_hero_make_reservation_visible(page: Page):
    expect(page.locator(HERO_MAKE_RESERVATION)).to_be_visible()

def test_hero_order_online_visible(page: Page):
    expect(page.locator(HERO_ORDER_ONLINE).first).to_be_visible()

def test_hero_see_menu_visible(page: Page):
    expect(page.locator(HERO_SEE_MENU)).to_be_visible()

def test_hero_make_reservation_navigates(page: Page):
    page.locator(HERO_MAKE_RESERVATION).click()
    page.wait_for_load_state("networkidle")
    assert "reservation" in page.url.lower(), f"Expected reservation page, got: {page.url}"

def test_hero_order_online_opens_new_tab(page: Page):
    with page.expect_popup() as popup_info:
        page.locator(HERO_ORDER_ONLINE).first.click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    assert "atlas.kitchen" in popup.url, f"Expected order online site, got: {popup.url}"

def test_hero_see_menu_navigates(page: Page):
    page.locator(HERO_SEE_MENU).click()
    page.wait_for_load_state("networkidle")
    assert "menu" in page.url.lower(), f"Expected menu page, got: {page.url}"


# ── Hero Decorative Images ────────────────────────────────────────────────────

def test_img_inasal_visible(page: Page):
    expect(page.locator(IMG_INASAL)).to_be_visible()

def test_img_land_visible(page: Page):
    expect(page.locator(IMG_LAND).first).to_be_visible()

def test_img_eagle_visible(page: Page):
    expect(page.locator(IMG_EAGLE)).to_be_visible()

def test_img_midnight_adobo_visible(page: Page):
    expect(page.locator(IMG_MIDNIGHT_ADOBO)).to_be_visible()

def test_img_yellow_flower_visible(page: Page):
    expect(page.locator(IMG_YELLOW_FLOWER).first).to_be_visible()

def test_img_tree_branch_visible(page: Page):
    expect(page.locator(IMG_TREE_BRANCH)).to_be_visible()

def test_img_fish_visible(page: Page):
    expect(page.locator(IMG_FISH).first).to_be_visible()

def test_img_banana_tree_visible(page: Page):
    expect(page.locator(IMG_BANANA_TREE)).to_be_visible()

def test_img_kalabaw_visible(page: Page):
    expect(page.locator(IMG_KALABAW)).to_be_visible()

def test_img_headline_visible(page: Page):
    expect(page.locator(IMG_HEADLINE)).to_be_visible()

def test_img_landing_artwork_10_3_visible(page: Page):
    expect(page.locator(IMG_LANDING_ARTWORK_10_3)).to_be_visible()

def test_img_pink_flower_visible(page: Page):
    expect(page.locator(IMG_PINK_FLOWER)).to_be_visible()


# ── Footer ────────────────────────────────────────────────────────────────────

def test_footer_socials_icon_visible(page: Page):
    expect(page.locator(FOOTER_SOCIALS_ICON)).to_be_visible()

def test_footer_socials_icon_opens_new_tab(page: Page):
    with page.expect_popup() as popup_info:
        page.locator(FOOTER_SOCIALS_ICON).click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    assert "instagram.com" in popup.url, f"Expected Instagram, got: {popup.url}"

def test_footer_tagline_visible(page: Page):
    expect(page.locator(FOOTER_TAGLINE)).to_be_visible()

def test_footer_address_visible(page: Page):
    expect(page.locator(FOOTER_ADDRESS)).to_be_visible()

def test_footer_privacy_visible(page: Page):
    expect(page.locator(FOOTER_PRIVACY)).to_be_visible()

def test_footer_terms_visible(page: Page):
    expect(page.locator(FOOTER_TERMS)).to_be_visible()

def test_footer_privacy_navigates(page: Page):
    page.locator(FOOTER_PRIVACY).click()
    page.wait_for_load_state("networkidle")
    assert "privacy-policy" in page.url.lower(), f"Expected privacy policy page, got: {page.url}"

def test_footer_terms_navigates(page: Page):
    page.locator(FOOTER_TERMS).click()
    page.wait_for_load_state("networkidle")
    assert "terms-conditions" in page.url.lower(), f"Expected terms page, got: {page.url}"