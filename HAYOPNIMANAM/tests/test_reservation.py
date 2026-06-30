import pytest
from playwright.sync_api import Page, expect
from locators.reservation_locators import ReservationLocators as RL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_reservation_page(page: Page):
    page.goto(RL.RESERVATION_URL)
    yield


# ── Page Content Tests ────────────────────────────────────────────────────────

class TestReservationPageContent:

    def test_make_reservation_link_visible(self, page: Page):
        expect(page.locator(RL.LINK_MAKE_RESERVATION)).to_be_visible()

    def test_lunch_label_visible(self, page: Page):
        expect(page.locator(RL.TEXT_LUNCH_LABEL)).to_be_visible()

    def test_lunch_hours_visible(self, page: Page):
        expect(page.locator(RL.TEXT_LUNCH_HOURS)).to_be_visible()

    def test_dinner_label_visible(self, page: Page):
        expect(page.locator(RL.TEXT_DINNER_LABEL)).to_be_visible()

    def test_dinner_hours_visible(self, page: Page):
        expect(page.locator(RL.TEXT_DINNER_HOURS)).to_be_visible()

    def test_address_visible(self, page: Page):
        expect(page.locator(RL.TEXT_ADDRESS)).to_be_visible()

    def test_reservation_info_card_visible(self, page: Page):
        expect(page.locator(RL.CARD_RESERVATION_INFO).first).to_be_visible()


# ── CTA Tests ──────────────────────────────────────────────────────────────────

class TestMakeReservationCTA:

    def test_make_reservation_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(RL.LINK_MAKE_RESERVATION).click()
        popup = popup_info.value
        assert "sevenrooms.com" in popup.url
        popup.close()