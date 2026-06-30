import pytest
from playwright.sync_api import Page, expect
from locators.menu_lunch_locators import MenuLunchLocators as ML


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_menu_lunch_sets(page: Page):
    page.goto(ML.MENU_LUNCH_SETS_URL, wait_until="domcontentloaded", timeout=60000)
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


# ── Lunch Sets Section ───────────────────────────────────────────────────────

class TestLunchSetsSection:

    def test_heading_and_intro_visible(self, page: Page):
        expect(ML.heading_lunch_sets(page)).to_be_visible()
        expect(page.locator(ML.TEXT_COMES_WITH_CHOICE)).to_be_visible()

    def test_lechon_kawali_visible(self, page: Page):
        expect(ML.span_lechon_kawali(page)).to_be_visible()
        expect(ML.paragraph_golden_fried_duroc(page)).to_be_visible()

    def test_inihaw_na_baboy_visible(self, page: Page):
        expect(page.locator(ML.TEXT_INIHAW_NA_BABOY)).to_be_visible()
        expect(page.locator(ML.TEXT_OVEN_BRAISED)).to_be_visible()

    def test_adobong_pula_visible(self, page: Page):
        expect(page.locator(ML.TEXT_ADOBONG_PULA)).to_be_visible()
        expect(page.locator(ML.TEXT_CORN_FED_CHICKEN)).to_be_visible()

    def test_adobong_dilaw_visible(self, page: Page):
        expect(ML.span_adobong_dilaw(page)).to_be_visible()
        expect(page.get_by_text(
            "Grain-fed Duroc pork belly Turmeric, sukang tuba, ginger, calamansi", exact=True
        )).to_be_visible()

    def test_chicken_inasal_visible(self, page: Page):
        expect(page.locator(ML.TEXT_CHICKEN_INASAL_29)).to_be_visible()
        expect(page.locator(ML.TEXT_CHARCOAL_GRILLED_HALF_CHICKEN)).to_be_visible()

    def test_inasal_na_panga_visible(self, page: Page):
        expect(page.locator(ML.TEXT_INASAL_NA_PANGA)).to_be_visible()
        expect(ML.paragraph_charcoal_grilled_maguro_jaw(page)).to_be_visible()

    def test_crispy_palabok_visible(self, page: Page):
        expect(ML.span_crispy_palabok(page)).to_be_visible()
        expect(page.locator(ML.TEXT_CHARRED_BABY_CUTTLEFISH)).to_be_visible()

    def test_tapsilog_visible(self, page: Page):
        expect(page.locator(ML.TEXT_TAPSILOG)).to_be_visible()
        expect(page.locator(ML.TEXT_HOUSE_CURED_ANGUS)).to_be_visible()

    def test_wild_mushroom_kare_kare_visible(self, page: Page):
        expect(ML.span_wild_mushroom_kare_kare(page)).to_be_visible()
        expect(page.locator(ML.TEXT_MAITAKE_PORTOBELLO)).to_be_visible()


# ── Top Up Section ───────────────────────────────────────────────────────────

class TestTopUpSection:

    def test_heading_and_intro_visible(self, page: Page):
        expect(ML.heading_top_up(page)).to_be_visible()
        expect(page.locator(ML.TEXT_PLUS_7_VEG_OR_DESSERT)).to_be_visible()
        expect(page.locator(ML.TEXT_CHOICE_OF_VEGETABLES)).to_be_visible()

    def test_gising_gising_visible(self, page: Page):
        expect(page.locator(ML.TEXT_GISING_GISING)).to_be_visible()
        expect(ML.paragraph_winged_bean_tofu(page)).to_be_visible()

    def test_laing_visible(self, page: Page):
        expect(page.locator(ML.TEXT_LAING)).to_be_visible()
        expect(page.locator(ML.TEXT_TARO_LEAVES_COCONUT)).to_be_visible()
        expect(ML.paragraph_sauteed_kale(page)).to_be_visible()

    def test_adobong_gulay_visible(self, page: Page):
        expect(page.locator(ML.TEXT_ADOBONG_GULAY)).to_be_visible()

    def test_choice_of_dessert_visible(self, page: Page):
        expect(page.locator(ML.TEXT_CHOICE_OF_DESSERT)).to_be_visible()

    def test_turon_visible(self, page: Page):
        expect(page.get_by_text("Turon", exact=True)).to_be_visible()
        expect(ML.paragraph_crisp_caramelized_banana(page)).to_be_visible()

    def test_ensaymada_visible(self, page: Page):
        expect(page.locator(ML.TEXT_ENSAYMADA)).to_be_visible()
        expect(page.locator(ML.TEXT_WARM_HOUSE_MADE_BRIOCHE)).to_be_visible()