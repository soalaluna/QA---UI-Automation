import pytest
from playwright.sync_api import Page, expect
from locators.footer_locators import FooterLocators as FL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_homepage(page: Page):
    page.goto(FL.BASE_URL)
    yield


# ── Footer Content Visibility Tests ───────────────────────────────────────────

class TestFooterContent:

    def test_socials_icon_visible(self, page: Page):
        expect(page.locator(FL.LINK_SOCIALS_ICON)).to_be_visible()

    def test_tagline_visible(self, page: Page):
        expect(page.locator(FL.TEXT_TAGLINE)).to_be_visible()

    def test_address_visible(self, page: Page):
        expect(page.locator(FL.TEXT_ADDRESS)).to_be_visible()

    def test_menu_item_visible(self, page: Page):
        expect(page.locator(FL.MENU_ITEM_11)).to_be_visible()

    def test_terms_link_visible(self, page: Page):
        expect(page.locator(FL.LINK_TERMS)).to_be_visible()


# ── Footer Link Tests ──────────────────────────────────────────────────────────

class TestFooterLinks:

    def test_socials_icon_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(FL.LINK_SOCIALS_ICON).click()
        popup = popup_info.value
        assert "instagram.com" in popup.url
        popup.close()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(FL.LINK_PRIVACY).click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(FL.LINK_TERMS).click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")