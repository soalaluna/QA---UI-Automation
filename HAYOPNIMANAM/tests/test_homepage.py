"""
Test suite for the Homepage - hayopnimanam.com
Only tests clickable/interactive elements.
"""

import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import HomepageLocators as HL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_homepage(page: Page):
    page.goto(HL.BASE_URL)
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestNavigation:

    def test_nav_menu_navigates(self, page: Page):
        page.locator(HL.NAV_MENU).click()
        expect(page).not_to_have_url(HL.BASE_URL)

    def test_nav_about_navigates(self, page: Page):
        page.locator(HL.NAV_ABOUT).click()
        expect(page).not_to_have_url(HL.BASE_URL)

    def test_nav_press_navigates(self, page: Page):
        page.locator(HL.NAV_PRESS).click()
        expect(page).not_to_have_url(HL.BASE_URL)

    def test_nav_contact_navigates(self, page: Page):
        page.locator(HL.NAV_CONTACT).click()
        expect(page).not_to_have_url(HL.BASE_URL)

    def test_nav_reservations_navigates(self, page: Page):
        page.locator(HL.NAV_RESERVATIONS).click()
        expect(page).not_to_have_url(HL.BASE_URL)

    def test_nav_order_online_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(HL.NAV_ORDER_ONLINE).click()
        popup = popup_info.value
        assert "atlas.kitchen" in popup.url
        popup.close()

    def test_nav_homepage_stays_on_homepage(self, page: Page):
        page.locator(HL.NAV_HOMEPAGE).first.click()
        expect(page).to_have_url(HL.BASE_URL)


# ── Hero / CTA Tests ──────────────────────────────────────────────────────────

class TestHeroCTAs:

    def test_make_reservation_navigates(self, page: Page):
        page.locator(HL.BTN_MAKE_RESERVATION).click()
        expect(page).not_to_have_url(HL.BASE_URL)

    def test_order_online_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(HL.BTN_ORDER_ONLINE).click()
        popup = popup_info.value
        assert "atlas.kitchen" in popup.url
        popup.close()

    def test_see_the_menu_navigates(self, page: Page):
        page.locator(HL.BTN_SEE_THE_MENU).click()
        expect(page).to_have_url("https://hayopnimanam.com/menu/")


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestFooter:

    def test_instagram_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(HL.FOOTER_INSTAGRAM).click()
        popup = popup_info.value
        assert "instagram.com" in popup.url
        popup.close()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(HL.FOOTER_PRIVACY).click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(HL.FOOTER_TERMS).click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")