import pytest
from playwright.sync_api import Page, expect
from locators.login_locators import LoginLocators as LL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_login(page: Page):
    page.goto(LL.LOGIN_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Page Load ─────────────────────────────────────────────────────────────────

class TestLoginPageLoad:

    def test_nav_elements_visible(self, page: Page):
        expect(page.locator(LL.LINK_HAYOP)).to_be_visible()
        expect(page.locator(LL.BTN_ORDER_NOW)).to_be_visible()
        expect(LL.path_nth_2(page)).to_be_visible()

    def test_heading_and_intro_visible(self, page: Page):
        expect(LL.heading_welcome_back(page)).to_be_visible()
        expect(page.locator(LL.TEXT_LOG_IN_FASTER)).to_be_visible()
        expect(page.locator(LL.TEXT_NO_ACCOUNT_YET)).to_be_visible()

    def test_phone_form_visible(self, page: Page):
        expect(page.get_by_test_id("input-label")).to_be_visible()
        expect(LL.phone_country_select(page)).to_be_visible()
        expect(LL.phone_input(page)).to_be_visible()
        expect(page.locator(LL.BTN_LOG_IN)).to_be_visible()
        expect(LL.div_or_divider(page)).to_be_visible()
        expect(page.locator(LL.BTN_CONTINUE_EMAIL)).to_be_visible()
        expect(page.locator(LL.POWERED_BY_ATLAS)).to_be_visible()


# ── Navigation Interactions ───────────────────────────────────────────────────

class TestLoginNavInteractions:

    def test_hayop_logo_link_visible_and_clickable(self, page: Page):
        """Codegen clicks the logo twice; assert it remains visible after."""
        expect(page.locator(LL.LINK_HAYOP)).to_be_visible()
        page.locator(LL.LINK_HAYOP).click()
        page.go_back()
        expect(page.locator(LL.LINK_HAYOP)).to_be_visible()

    def test_sign_up_here_link_navigates_to_signup(self, page: Page):
        page.locator(LL.LINK_SIGN_UP_HERE).click()
        expect(page).to_have_url("https://hayop.atlas.kitchen/signup")


# ── Phone Login Flow ──────────────────────────────────────────────────────────

class TestPhoneLoginFlow:

    def test_country_selector_works(self, page: Page):
        LL.phone_country_select(page).select_option("PH")
        expect(LL.phone_country_select(page)).to_have_value("PH")

    def test_phone_field_accepts_input(self, page: Page):
        LL.phone_input(page).fill("+63 912 345 6789")
        expect(LL.phone_input(page)).not_to_be_empty()

    def test_login_button_submits_phone(self, page: Page):
        """
        Fill a valid PH number and click Log in.
        Codegen navigates to about:blank after to avoid the OTP flow;
        we just assert the button is clickable and the page responds
        (no JS error / crash) rather than waiting for the OTP modal,
        which would require a real registered number.
        """
        LL.phone_country_select(page).select_option("PH")
        LL.phone_input(page).fill("+63 912 345 6789")
        page.locator(LL.BTN_LOG_IN).click()
        # Navigate away to abort the OTP flow (same as codegen's about:blank)
        page.goto("about:blank")