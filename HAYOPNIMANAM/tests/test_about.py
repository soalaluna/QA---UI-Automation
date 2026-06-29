import pytest
from playwright.sync_api import Page, expect
from locators.about_locators import (
    BASE_URL,
    IMG_HEADLINE, IMG_LEAVES, IMG_TOMATO,
    INTRO_TEXT, INTRO_KAIN_NA, INTRO_SIGN_OFF, LABEL_HAYOP,
    TAB_ABOUT_US, TAB_THE_MOMENT_GROUP, TAB_OUR_FOUNDERS,
    TAB_PARTNERS, TAB_ABOUT_SINGAPORE,
    IMG_HAYOP, IMG_BG, IMG_BAKA, IMG_SUN,
    HEADING_ABOUT_US, ABOUT_US_TEXT,
    IMG_ABOUT_ARTWORK, HEADING_MOMENT_GROUP, MOMENT_GROUP_TEXT,
    IMG_PAPER, IMG_05, IMG_02, IMG_LEAF,
    HEADING_SINGAPORE_PARTNERS, PARTNER_RUSSEL_TEXT,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Intro Section ──────────────────────────────────────────────────────────────

def test_img_headline_visible(page: Page):
    expect(page.locator(IMG_HEADLINE)).to_be_visible()

def test_img_leaves_visible(page: Page):
    expect(page.locator(IMG_LEAVES)).to_be_visible()

def test_img_tomato_visible(page: Page):
    expect(page.locator(IMG_TOMATO)).to_be_visible()

def test_intro_text_visible(page: Page):
    expect(page.locator(INTRO_TEXT)).to_be_visible()

def test_intro_kain_na_visible(page: Page):
    expect(page.locator(INTRO_KAIN_NA)).to_be_visible()

def test_intro_sign_off_visible(page: Page):
    expect(page.locator(INTRO_SIGN_OFF)).to_be_visible()

def test_label_hayop_visible(page: Page):
    expect(page.locator(LABEL_HAYOP)).to_be_visible()


# ── Tab Navigation ─────────────────────────────────────────────────────────────

def test_tab_about_us_visible(page: Page):
    expect(page.locator(TAB_ABOUT_US)).to_be_visible()

def test_tab_the_moment_group_visible(page: Page):
    expect(page.locator(TAB_THE_MOMENT_GROUP)).to_be_visible()

def test_tab_our_founders_visible(page: Page):
    expect(page.locator(TAB_OUR_FOUNDERS)).to_be_visible()

def test_tab_partners_visible(page: Page):
    expect(page.locator(TAB_PARTNERS)).to_be_visible()

def test_tab_about_singapore_visible(page: Page):
    expect(page.locator(TAB_ABOUT_SINGAPORE)).to_be_visible()


# ── About Us Section (default tab) ────────────────────────────────────────────

def test_img_hayop_visible(page: Page):
    expect(page.locator(IMG_HAYOP)).to_be_visible()

def test_img_bg_visible(page: Page):
    expect(page.locator(IMG_BG)).to_be_visible()

def test_img_baka_visible(page: Page):
    expect(page.locator(IMG_BAKA)).to_be_visible()

def test_img_sun_visible(page: Page):
    expect(page.locator(IMG_SUN)).to_be_visible()

def test_heading_about_us_visible(page: Page):
    expect(page.locator(HEADING_ABOUT_US)).to_be_visible()

def test_about_us_text_visible(page: Page):
    expect(page.locator(ABOUT_US_TEXT)).to_be_visible()


# ── The Moment Group Section (after clicking tab) ─────────────────────────────

def test_moment_group_tab_switches_content(page: Page):
    page.locator(TAB_THE_MOMENT_GROUP).click()
    page.wait_for_timeout(300)
    expect(page.locator(HEADING_MOMENT_GROUP)).to_be_visible()

def test_img_about_artwork_visible(page: Page):
    page.locator(TAB_THE_MOMENT_GROUP).click()
    page.wait_for_timeout(300)
    expect(page.locator(IMG_ABOUT_ARTWORK)).to_be_visible()

def test_heading_moment_group_visible(page: Page):
    page.locator(TAB_THE_MOMENT_GROUP).click()
    page.wait_for_timeout(300)
    expect(page.locator(HEADING_MOMENT_GROUP)).to_be_visible()

def test_moment_group_text_visible(page: Page):
    page.locator(TAB_THE_MOMENT_GROUP).click()
    page.wait_for_timeout(300)
    expect(page.locator(MOMENT_GROUP_TEXT)).to_be_visible()


# ── About Singapore / Partners Section (after clicking tab) ───────────────────

def test_about_singapore_tab_switches_content(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(HEADING_SINGAPORE_PARTNERS)).to_be_visible()

def test_img_paper_visible(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(IMG_PAPER)).to_be_visible()

def test_img_05_visible(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(IMG_05)).to_be_visible()

def test_img_02_visible(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(IMG_02)).to_be_visible()

def test_img_leaf_visible(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(IMG_LEAF)).to_be_visible()

def test_heading_singapore_partners_visible(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(HEADING_SINGAPORE_PARTNERS)).to_be_visible()

def test_partner_russel_text_visible(page: Page):
    page.locator(TAB_ABOUT_SINGAPORE).click()
    page.wait_for_timeout(300)
    expect(page.locator(PARTNER_RUSSEL_TEXT)).to_be_visible()