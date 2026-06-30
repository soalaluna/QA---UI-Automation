import pytest
from playwright.sync_api import Page, expect
from locators.menu_drinks_locators import MenuDrinksLocators as ML


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_menu_drinks(page: Page):
    page.goto(ML.MENU_DRINKS_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Alcoholic Section (inuman) ─────────────────────────────────────────────────

class TestAlcoholicSection:

    def test_heading_visible(self, page: Page):
        expect(ML.heading_alcoholic_inuman(page)).to_be_visible()

    def test_cocktails_visible(self, page: Page):
        expect(page.locator(ML.TEXT_COCKTAILS_22)).to_be_visible()
        expect(page.locator(ML.TEXT_ALAT_SALTY)).to_be_visible()
        expect(page.locator(ML.TEXT_ASIM_SOUR)).to_be_visible()
        expect(page.locator(ML.TEXT_TAMIS_SWEET)).to_be_visible()
        expect(page.locator(ML.TEXT_ANGHANG_SPICY)).to_be_visible()
        expect(page.locator(ML.TEXT_MALINAMNAM_UMAMI)).to_be_visible()
        expect(page.locator(ML.TEXT_PAIT_BITTER)).to_be_visible()

    def test_philippine_beers_visible(self, page: Page):
        expect(page.locator(ML.TEXT_PHILIPPINE_BEERS)).to_be_visible()
        expect(ML.listitem_san_miguel_light(page)).to_be_visible()
        expect(ML.listitem_engkanto(page)).to_be_visible()

    def test_wines_and_sakes_visible(self, page: Page):
        expect(ML.listitem_wines_sakes(page)).to_be_visible()
        expect(ML.listitem_please_ask(page)).to_be_visible()


# ── Non-Alcoholic Section (inumin) ────────────────────────────────────────────

class TestNonAlcoholicSection:

    def test_heading_visible(self, page: Page):
        expect(ML.heading_non_alcoholic_inumin(page)).to_be_visible()

    def test_shakes_visible(self, page: Page):
        expect(page.locator(ML.TEXT_SHAKES_15)).to_be_visible()
        expect(page.locator(ML.TEXT_UBE_SHAKE_HOUSEMADE)).to_be_visible()
        expect(page.locator(ML.TEXT_BUKO_PANDAN_SHAKE)).to_be_visible()

    def test_canned_sodas_visible(self, page: Page):
        expect(page.locator(ML.TEXT_CANNED_SODAS_6)).to_be_visible()
        expect(page.locator(ML.TEXT_COCA_COLA)).to_be_visible()
        expect(page.locator(ML.TEXT_SPRITE)).to_be_visible()

    def test_coffee_visible(self, page: Page):
        expect(page.get_by_text("Coffee", exact=True)).to_be_visible()
        expect(page.locator(ML.TEXT_ESPRESSO_4_5)).to_be_visible()
        expect(page.locator(ML.TEXT_BLACK_COFFEE_5)).to_be_visible()
        expect(page.locator(ML.TEXT_FLAT_WHITE_6)).to_be_visible()
        expect(page.locator(ML.TEXT_LATTE_6)).to_be_visible()
        expect(page.locator(ML.TEXT_CAPPUCCINO_6)).to_be_visible()

    def test_tea_visible(self, page: Page):
        expect(ML.listitem_tea_6(page)).to_be_visible()
        expect(page.locator(ML.TEXT_OOLONG_TEA)).to_be_visible()
        expect(page.locator(ML.TEXT_GREEN_TEA)).to_be_visible()
        expect(page.locator(ML.TEXT_CHAMOMILE_TEA)).to_be_visible()