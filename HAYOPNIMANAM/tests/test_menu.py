import pytest
from playwright.sync_api import Page, expect
from locators.menu_locators import (
    BASE_URL,
    IMG_KINILAW_HAMACHI, IMG_WAGYU_WATERMELON, IMG_MIDNIGHT_ADOBO,
    IMG_DRINKS_CAROUSEL, IMG_PRODUCE,
    LABEL_THE_MENU,
    TAB_A_LA_CARTE_MAIN, TAB_LUNCH_SETS_COMBO, TAB_DESSERT_MINATAMIS, TAB_DRINKS_INUMIN,
    HEADING_A_LA_CARTE,
    ABOUT_THE_MENU, ABOUT_TEXT_FILIPINO, ABOUT_TEXT_PANTRY,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


# ── Carousel Images ────────────────────────────────────────────────────────────

def test_img_kinilaw_hamachi_visible(page: Page):
    expect(page.locator(IMG_KINILAW_HAMACHI)).to_be_attached()

def test_img_wagyu_watermelon_visible(page: Page):
    expect(page.locator(IMG_WAGYU_WATERMELON)).to_be_attached()

def test_img_midnight_adobo_visible(page: Page):
    expect(page.locator(IMG_MIDNIGHT_ADOBO)).to_be_attached()

def test_img_drinks_carousel_visible(page: Page):
    expect(page.locator(IMG_DRINKS_CAROUSEL)).to_be_attached()

def test_img_produce_visible(page: Page):
    expect(page.locator(IMG_PRODUCE)).to_be_attached()


# ── Header Labels ──────────────────────────────────────────────────────────────

def test_label_the_menu_visible(page: Page):
    expect(page.locator(LABEL_THE_MENU)).to_be_visible()


# ── Menu Category Tabs ─────────────────────────────────────────────────────────

def test_tab_a_la_carte_main_visible(page: Page):
    expect(page.locator(TAB_A_LA_CARTE_MAIN)).to_be_visible()

def test_tab_lunch_sets_combo_visible(page: Page):
    expect(page.locator(TAB_LUNCH_SETS_COMBO)).to_be_visible()

def test_tab_dessert_minatamis_visible(page: Page):
    expect(page.locator(TAB_DESSERT_MINATAMIS)).to_be_visible()

def test_tab_drinks_inumin_visible(page: Page):
    expect(page.locator(TAB_DRINKS_INUMIN)).to_be_visible()


# ── Section Heading ─────────────────────────────────────────────────────────────

def test_heading_a_la_carte_visible(page: Page):
    expect(page.locator(HEADING_A_LA_CARTE)).to_be_visible()


# ── About the Menu ───────────────────────────────────────────────────────────────

def test_about_the_menu_visible(page: Page):
    expect(page.locator(ABOUT_THE_MENU)).to_be_visible()

def test_about_text_filipino_visible(page: Page):
    expect(page.locator(ABOUT_TEXT_FILIPINO)).to_be_visible()

def test_about_text_pantry_visible(page: Page):
    expect(page.locator(ABOUT_TEXT_PANTRY)).to_be_visible()