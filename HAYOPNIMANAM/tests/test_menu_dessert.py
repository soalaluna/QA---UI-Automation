import pytest
from playwright.sync_api import Page, expect
from locators.menu_dessert_locators import MenuDessertLocators as ML


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_menu_dessert(page: Page):
    page.goto(ML.MENU_DESSERT_URL, wait_until="domcontentloaded", timeout=60000)
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
        expect(ML.swiper_tab(page, "2 /", "a la carte")).to_be_visible()

    def test_main_menu_tab_visible(self, page: Page):
        expect(page.locator(ML.TEXT_MAIN_MENU)).to_be_visible()

    def test_lunch_sets_tab_visible(self, page: Page):
        expect(ML.swiper_tab(page, "3 /", "lunch sets")).to_be_visible()

    def test_tsibog_combo_tab_visible(self, page: Page):
        expect(page.locator(ML.TEXT_TSIBOG_COMBO)).to_be_visible()

    def test_dessert_tab_visible(self, page: Page):
        expect(ML.swiper_tab(page, "4 /", "dessert")).to_be_visible()

    def test_minatamis_visible(self, page: Page):
        expect(page.locator(ML.TEXT_MINATAMIS)).to_be_visible()

    def test_drinks_visible(self, page: Page):
        expect(page.locator(ML.TEXT_DRINKS)).to_be_visible()

    def test_inumin_tab_visible(self, page: Page):
        expect(ML.swiper_tab(page, "5 /", "inumin")).to_be_visible()


# ── Dessert Section ───────────────────────────────────────────────────────────

class TestDessertSection:

    def test_heading_and_intro_visible(self, page: Page):
        expect(ML.heading_dessert(page)).to_be_visible()
        expect(ML.paragraph_a_la_carte(page)).to_be_visible()

    def test_halo_halo_visible(self, page: Page):
        expect(page.locator(ML.TEXT_HALO_HALO)).to_be_visible()
        expect(page.locator(ML.TEXT_SHAVED_ICE_UBE)).to_be_visible()

    def test_mais_con_hielo_visible(self, page: Page):
        expect(page.locator(ML.TEXT_MAIS_CON_HIELO)).to_be_visible()
        expect(page.locator(ML.TEXT_SHAVED_ICE_CORN)).to_be_visible()

    def test_ube_shake_visible(self, page: Page):
        expect(page.locator(ML.TEXT_UBE_SHAKE)).to_be_visible()
        expect(page.get_by_text(
            "Housemade purple yam sorbetes, coconut cream, white sago", exact=True
        )).to_be_visible()

    def test_turon_visible(self, page: Page):
        expect(page.locator(ML.TEXT_TURON_14)).to_be_visible()
        expect(ML.paragraph_crisp_caramelized_banana(page)).to_be_visible()

    def test_buko_pie_visible(self, page: Page):
        expect(page.locator(ML.TEXT_BUKO_PIE)).to_be_visible()
        expect(page.locator(ML.TEXT_COCONUT_PARMESAN_CRUMBLE)).to_be_visible()

    def test_patis_caramel_tart_visible(self, page: Page):
        expect(page.locator(ML.TEXT_PATIS_CARAMEL_TART)).to_be_visible()
        expect(page.locator(ML.TEXT_DARK_CHOCOLATE_GANACHE)).to_be_visible()

    def test_buko_pandan_shake_visible(self, page: Page):
        expect(page.locator(ML.TEXT_BUKO_PANDAN_SHAKE_15)).to_be_visible()
        expect(page.get_by_text(
            "House coconut blend, white sago, and green pandan gulaman", exact=True
        )).to_be_visible()

    def test_sorbetes_visible(self, page: Page):
        expect(page.locator(ML.TEXT_SORBETES_6)).to_be_visible()
        expect(page.locator(ML.TEXT_HOUSE_MADE_ICE_CREAM_UBE)).to_be_visible()