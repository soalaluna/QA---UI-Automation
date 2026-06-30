import pytest
from playwright.sync_api import Page, expect
from locators.menu_alacarte_locators import MenuAlaCarteLocators as ML


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_menu_ala_carte(page: Page):
    page.goto(ML.MENU_ALA_CARTE_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Page Header ───────────────────────────────────────────────────────────────

class TestMenuHeader:

    def test_the_menu_text_visible(self, page: Page):
        expect(page.get_by_text("the menu", exact=True)).to_be_visible()

    def test_behind_the_taste_visible(self, page: Page):
        expect(page.locator(ML.TEXT_BEHIND_THE_TASTE)).to_be_visible()


# ── Menu Tab Navigation ───────────────────────────────────────────────────────

class TestMenuTabNavigation:

    def test_a_la_carte_tab_visible(self, page: Page):
        expect(ML.swiper_tab(page, "2 / 5", "a la carte")).to_be_visible()

    def test_main_menu_tab_visible(self, page: Page):
        expect(page.locator(ML.TEXT_MAIN_MENU)).to_be_visible()

    def test_lunch_sets_tab_visible(self, page: Page):
        expect(ML.swiper_tab(page, "3 / 5", "lunch sets")).to_be_visible()

    def test_tsibog_combo_tab_visible(self, page: Page):
        expect(page.locator(ML.TEXT_TSIBOG_COMBO)).to_be_visible()

    def test_dessert_minatamis_tab_visible(self, page: Page):
        expect(page.locator(ML.TEXT_DESSERT_MINATAMIS)).to_be_visible()

    def test_drinks_inumin_tab_visible(self, page: Page):
        expect(page.locator(ML.TEXT_DRINKS_INUMIN)).to_be_visible()


# ── A La Carte Section ───────────────────────────────────────────────────────

class TestALaCarteSection:

    def test_heading_visible(self, page: Page):
        expect(ML.heading_a_la_carte(page)).to_be_visible()

    def test_about_the_menu_visible(self, page: Page):
        expect(page.locator(ML.TEXT_ABOUT_THE_MENU)).to_be_visible()

    def test_filipino_food_intro_visible(self, page: Page):
        expect(page.locator(ML.TEXT_FILIPINO_FOOD_AS_IT_IS)).to_be_visible()
        # NOTE: positional/fragile locator, see locator file docstring.
        expect(ML.filtered_div_filipino_food(page)).to_be_visible()

    def test_hayop_pantry_list_text_visible(self, page: Page):
        expect(page.locator(ML.TEXT_HAYOP_PANTRY_LIST)).to_be_visible()