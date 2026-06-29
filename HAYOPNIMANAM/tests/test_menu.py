import re
import pytest
from playwright.sync_api import Page, expect
from locators.menu_locators import MenuLocators as ML

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_menu(page: Page):
    page.goto(ML.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.locator(ML.NAV_MENU).first.click()
    page.wait_for_url("**/menu/**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestMenuNavigation:

    def test_menu_page_loads(self, page: Page):
        expect(page).to_have_url(re.compile(r".*/menu/.*"))


# ── Tab Tests ─────────────────────────────────────────────────────────────────

class TestMenuTabs:

    def test_a_la_carte_tab_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator(ML.TAB_A_LA_CARTE).first.click()
        expect(page.locator(ML.TAB_A_LA_CARTE).first).to_be_visible()

    def test_lunch_sets_tab_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator(ML.TAB_LUNCH_SETS).first.click()
        expect(page.locator(ML.TAB_LUNCH_SETS).first).to_be_visible()

    def test_dessert_tab_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator(ML.TAB_DESSERT).first.click()
        expect(page.locator(ML.TAB_DESSERT).first).to_be_visible()

    def test_drinks_tab_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator(ML.TAB_DRINKS).first.click()
        expect(page.locator(ML.TAB_DRINKS).first).to_be_visible()


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestMenuFooter:

    def test_instagram_link_present(self, page: Page):
        expect(page.locator(ML.FOOTER_INSTAGRAM)).to_be_attached()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(ML.FOOTER_PRIVACY).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(ML.FOOTER_TERMS).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")