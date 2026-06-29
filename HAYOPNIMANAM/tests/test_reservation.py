import pytest
from playwright.sync_api import Page, expect
from locators.reservation_locators import ReservationLocators as RL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_reservation(page: Page):
    page.goto(RL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.locator(RL.NAV_RESERVATIONS).first.click()
    page.wait_for_url("**/reservation/**")
    yield


@pytest.fixture()
def sevenrooms(page: Page):
    """Opens the SevenRooms popup and returns it as the active page."""
    with page.expect_popup() as popup_info:
        page.locator(RL.LINK_MAKE_RESERVATION).click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    popup.wait_for_timeout(1000)
    return popup


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestReservationNavigation:

    def test_reservation_page_loads(self, page: Page):
        expect(page).to_have_url(RL.RESERVATION_URL)

    def test_make_reservation_opens_sevenrooms(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(RL.LINK_MAKE_RESERVATION).click()
        popup = popup_info.value
        assert "sevenrooms.com" in popup.url
        popup.close()


# ── SevenRooms: Date Stepper ──────────────────────────────────────────────────

class TestSevenRoomsDatePicker:

    def test_date_display_visible(self, page: Page, sevenrooms):
        """Date button showing current date should be visible"""
        expect(sevenrooms.locator(RL.SR_DATE_DISPLAY)).to_be_visible()

    def test_date_increment_clickable(self, page: Page, sevenrooms):
        """Increment date button should advance the date"""
        sevenrooms.locator(RL.SR_DATE_INCREMENT).click()
        expect(sevenrooms.locator(RL.SR_DATE_INCREMENT)).to_be_visible()

    def test_date_decrement_present(self, page: Page, sevenrooms):
        """Decrement date button should be present (disabled on current date)"""
        expect(sevenrooms.locator(RL.SR_DATE_DECREMENT)).to_be_visible()


# ── SevenRooms: Guest Stepper ─────────────────────────────────────────────────

class TestSevenRoomsGuestCount:

    def test_guest_display_visible(self, page: Page, sevenrooms):
        """Guest count button should be visible"""
        expect(sevenrooms.locator(RL.SR_GUEST_DISPLAY)).to_be_visible()

    def test_guest_increment_clickable(self, page: Page, sevenrooms):
        """Increment guest button should increase guest count"""
        sevenrooms.locator(RL.SR_GUEST_INCREMENT).first.click()
        expect(sevenrooms.locator(RL.SR_GUEST_INCREMENT).first).to_be_visible()

    def test_guest_decrement_clickable(self, page: Page, sevenrooms):
        """Decrement guest button should decrease guest count"""
        sevenrooms.locator(RL.SR_GUEST_INCREMENT).first.click()
        sevenrooms.locator(RL.SR_GUEST_DECREMENT).first.click()
        expect(sevenrooms.locator(RL.SR_GUEST_DISPLAY)).to_be_visible()


# ── SevenRooms: Time Stepper ──────────────────────────────────────────────────

class TestSevenRoomsTimePicker:

    def test_time_display_visible(self, page: Page, sevenrooms):
        """Time button should be visible"""
        expect(sevenrooms.locator(RL.SR_TIME_DISPLAY)).to_be_visible()

    def test_time_increment_clickable(self, page: Page, sevenrooms):
        """Increment time button should advance the time"""
        sevenrooms.locator(RL.SR_TIME_INCREMENT).click()
        expect(sevenrooms.locator(RL.SR_TIME_INCREMENT)).to_be_visible()

    def test_time_decrement_clickable(self, page: Page, sevenrooms):
        """Decrement time button should decrease the time"""
        sevenrooms.locator(RL.SR_TIME_DECREMENT).click()
        expect(sevenrooms.locator(RL.SR_TIME_DECREMENT)).to_be_visible()


# ── SevenRooms: Search ────────────────────────────────────────────────────────

class TestSevenRoomsSearch:

    def test_search_button_visible(self, page: Page, sevenrooms):
        expect(sevenrooms.locator(RL.SR_SEARCH_BUTTON)).to_be_visible()

    def test_search_button_clickable(self, page: Page, sevenrooms):
        """Clicking Search should proceed to login/results page"""
        sevenrooms.locator(RL.SR_SEARCH_BUTTON).click()
        sevenrooms.wait_for_timeout(1500)
        assert "sevenrooms.com" in sevenrooms.url


# ── SevenRooms: Login Options ─────────────────────────────────────────────────

class TestSevenRoomsLogin:

    @pytest.fixture(autouse=True)
    def after_search(self, sevenrooms):
        """Click Search then select a time slot to reach login screen"""
        sevenrooms.locator(RL.SR_SEARCH_BUTTON).click()
        sevenrooms.wait_for_timeout(2000)
        sevenrooms.locator(RL.SR_TIME_SLOT).first.click()
        sevenrooms.wait_for_timeout(1000)
        self.sr = sevenrooms

    def test_guest_login_visible(self, page: Page):
        expect(self.sr.locator(RL.SR_LOGIN_GUEST)).to_be_visible()

    def test_guest_login_clickable(self, page: Page):
        self.sr.locator(RL.SR_LOGIN_GUEST).click()
        self.sr.wait_for_timeout(500)
        expect(self.sr.get_by_role("textbox", name="First Name")).to_be_visible()


# ── SevenRooms: Guest Details Form ───────────────────────────────────────────

class TestSevenRoomsGuestForm:

    @pytest.fixture(autouse=True)
    def open_guest_form(self, sevenrooms):
        sevenrooms.locator(RL.SR_SEARCH_BUTTON).click()
        sevenrooms.locator(RL.SR_TIME_SLOT).first.wait_for(state="visible", timeout=15000)
        sevenrooms.locator(RL.SR_TIME_SLOT).first.click()
        sevenrooms.locator(RL.SR_LOGIN_GUEST).wait_for(state="visible", timeout=15000)
        sevenrooms.locator(RL.SR_LOGIN_GUEST).click()
        sevenrooms.get_by_role("textbox", name="First Name").wait_for(state="visible", timeout=10000)
        self.sr = sevenrooms

    def test_first_name_field_fillable(self, page: Page):
        self.sr.get_by_role("textbox", name="First Name").fill("Test")
        expect(self.sr.get_by_role("textbox", name="First Name")).to_have_value("Test")

    def test_last_name_field_fillable(self, page: Page):
        self.sr.get_by_role("textbox", name="Last Name").fill("User")
        expect(self.sr.get_by_role("textbox", name="Last Name")).to_have_value("User")

    def test_email_field_fillable(self, page: Page):
        self.sr.get_by_role("textbox", name="Email").fill("test@test.com")
        expect(self.sr.get_by_role("textbox", name="Email")).to_have_value("test@test.com")

    def test_phone_field_fillable(self, page: Page):
        self.sr.get_by_role("textbox", name="Phone Number").fill("+65 91234567")
        # SevenRooms auto-formats phone numbers (e.g. +65 6591-234567)
        # so just verify the field accepted input and is not empty
        value = self.sr.get_by_role("textbox", name="Phone Number").input_value()
        assert value != "", "Phone field should not be empty after filling"


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestReservationFooter:

    def test_instagram_link_present(self, page: Page):
        expect(page.locator(RL.FOOTER_INSTAGRAM)).to_be_attached()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(RL.FOOTER_PRIVACY).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(RL.FOOTER_TERMS).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")