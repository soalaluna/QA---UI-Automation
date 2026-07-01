import re
import pytest
from playwright.sync_api import Page, expect
from locators.signup_locators import SignupLocators as SL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_signup(page: Page):
    page.goto(SL.SIGNUP_URL, wait_until="domcontentloaded", timeout=60000)
    yield


def _submit_phone(page: Page):
    """Fill phone and click Sign Up to reveal the detailed signup form."""
    SL.phone_input(page).click()
    SL.phone_country_select(page).select_option("PH")
    SL.phone_input(page).fill("+63 912 345 6789")
    page.locator(SL.BTN_SIGN_UP).click()
    page.get_by_role("textbox", name="Enter your email").wait_for(
        state="visible", timeout=15000
    )


def _fill_full_form_and_reach_otp(page: Page):
    """
    Submit phone, fill all form fields, click Sign Up for an account, and
    wait for the OTP modal. Handles both paths:
      - Normal: email form appears → fill everything → submit → OTP modal
      - Rate-limited: server skips straight to OTP modal after phone submit

    The phone number may have been submitted several times in earlier tests,
    so the server can skip the email form entirely.
    """
    SL.phone_input(page).click()
    SL.phone_country_select(page).select_option("PH")
    SL.phone_input(page).fill("+63 912 345 6789")
    page.locator(SL.BTN_SIGN_UP).click()

    # Check which state the server lands on (email form vs OTP modal directly)
    otp_already_visible = False
    try:
        page.get_by_text("Sign up with 6-digit code").wait_for(
            state="visible", timeout=5000
        )
        otp_already_visible = True
    except Exception:
        pass

    if not otp_already_visible:
        # Email form appeared — fill all fields and submit
        page.get_by_role("textbox", name="Enter your email").wait_for(
            state="visible", timeout=30000
        )
        page.get_by_role("textbox", name="Enter your email").fill("testing@mail.com")
        page.get_by_role("textbox", name="Name").fill("testing")
        page.locator(SL.TITLE_SELECT).click()
        page.get_by_text("Miss").click()
        page.get_by_role("textbox", name="When is your birthday?").click()
        SL.btn_year_panel(page).click()
        page.get_by_text("2024").click()
        SL.btn_year_panel(page).click()
        SL.btn_super_prev_year(page).click()
        SL.btn_super_prev_year(page).click()
        page.get_by_role("cell", name="2003").click()
        page.get_by_role("textbox", name="When is your birthday?").click()
        page.locator(SL.ANT_PICKER).click()
        page.get_by_text("Jul").click()
        page.get_by_text("1").nth(2).click()
        page.locator(SL.BTN_SIGN_UP_FOR_ACCOUNT).click()
        page.get_by_text("Sign up with 6-digit code").wait_for(
            state="visible", timeout=30000
        )


# ── Initial Signup Page ───────────────────────────────────────────────────────

class TestSignupPageLoad:

    def test_nav_elements_visible(self, page: Page):
        expect(page.locator(SL.LINK_HAYOP)).to_be_visible()
        expect(page.locator(SL.BTN_ORDER_NOW)).to_be_visible()
        expect(SL.path_nth_2(page)).to_be_visible()

    def test_heading_and_intro_visible(self, page: Page):
        expect(SL.heading_sign_up(page)).to_be_visible()
        expect(page.locator(SL.TEXT_FASTER_CHECKOUTS)).to_be_visible()
        expect(page.locator(SL.TEXT_ALREADY_HAVE_ACCOUNT)).to_be_visible()

    def test_phone_form_visible(self, page: Page):
        expect(page.get_by_test_id("input-label")).to_be_visible()
        expect(SL.phone_input(page)).to_be_visible()
        expect(SL.phone_country_select(page)).to_be_visible()
        expect(page.locator(SL.BTN_SIGN_UP)).to_be_visible()
        expect(page.get_by_text("or", exact=True)).to_be_visible()
        expect(page.locator(SL.BTN_CONTINUE_EMAIL)).to_be_visible()
        expect(page.locator(SL.POWERED_BY_ATLAS)).to_be_visible()


# ── Navigation Interactions ───────────────────────────────────────────────────

class TestSignupNavInteractions:

    def test_order_now_button_clickable(self, page: Page):
        page.locator(SL.BTN_ORDER_NOW).click()

    def test_path_icon_clickable(self, page: Page):
        SL.path_nth_2(page).click()

    def test_log_in_here_link_navigates(self, page: Page):
        page.locator(SL.LINK_LOG_IN_HERE).click()
        expect(page).to_have_url(re.compile(r".*/login.*"))


# ── Phone Submission Flow ─────────────────────────────────────────────────────

class TestPhoneSubmissionFlow:

    def test_phone_field_accepts_input(self, page: Page):
        SL.phone_input(page).click()
        SL.phone_country_select(page).select_option("PH")
        SL.phone_input(page).fill("+63 912 345 6789")
        expect(SL.phone_input(page)).not_to_be_empty()

    def test_signup_form_appears_after_phone_submit(self, page: Page):
        _submit_phone(page)

        expect(page.locator(SL.TEXT_EMAIL_REQUIRED)).to_be_visible()
        expect(page.get_by_role("textbox", name="Enter your email")).to_be_visible()
        expect(page.get_by_text("Name", exact=True)).to_be_visible()
        expect(page.locator(SL.TEXT_NAME_REQUIRED)).to_be_visible()
        expect(page.get_by_role("textbox", name="Name")).to_be_visible()
        expect(SL.div_title(page)).to_be_visible()
        expect(SL.div_address_title(page)).to_be_visible()
        expect(page.locator(SL.TEXT_DATE_OF_BIRTH)).to_be_visible()
        expect(page.get_by_role("textbox", name="When is your birthday?")).to_be_visible()
        expect(page.locator(SL.ANT_PICKER)).to_be_visible()
        expect(page.locator(SL.TEXT_CONSENT)).to_be_visible()
        expect(page.get_by_role("checkbox", name="I consent to receiving")).to_be_visible()
        expect(page.locator(SL.TEXT_BY_CONTINUING)).to_be_visible()
        expect(page.locator(SL.BTN_SIGN_UP_FOR_ACCOUNT)).to_be_visible()


# ── Signup Form Fill ──────────────────────────────────────────────────────────

class TestSignupFormFill:

    @pytest.fixture(autouse=True)
    def submit_phone_first(self, page: Page):
        _submit_phone(page)

    def test_fill_email_and_name(self, page: Page):
        page.get_by_role("textbox", name="Enter your email").fill("testing@mail.com")
        page.get_by_role("textbox", name="Name").fill("testing")
        expect(page.get_by_role("textbox", name="Enter your email")).to_have_value("testing@mail.com")
        expect(page.get_by_role("textbox", name="Name")).to_have_value("testing")

    def test_select_title(self, page: Page):
        page.locator(SL.TITLE_SELECT).click()
        page.get_by_text("Miss").click()

    def test_select_birthday(self, page: Page):
        page.get_by_role("textbox", name="When is your birthday?").click()
        SL.btn_year_panel(page).click()
        page.get_by_text("2024").click()
        SL.btn_year_panel(page).click()
        SL.btn_super_prev_year(page).click()
        SL.btn_super_prev_year(page).click()
        page.get_by_role("cell", name="2003").click()
        page.get_by_role("textbox", name="When is your birthday?").click()
        page.locator(SL.ANT_PICKER).click()
        page.get_by_text("Jul").click()
        page.get_by_text("1").nth(2).click()


# ── Terms and Privacy Links ───────────────────────────────────────────────────

class TestTermsAndPrivacyLinks:
    """
    Terms/privacy links only render inside the detailed signup form (after
    phone submission). The submit_phone_first fixture makes them visible.

    Privacy policy uses href assertion instead of expect_popup() because
    browsers commonly block a second consecutive programmatic popup from
    the same page after one has already been opened (security measure).
    """

    @pytest.fixture(autouse=True)
    def submit_phone_first(self, page: Page):
        _submit_phone(page)

    def test_terms_of_service_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="terms of service").click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_privacy_policy_link_has_correct_href(self, page: Page):
        """
        Verify the privacy policy link is visible and points to the Atlas
        privacy policy URL. Avoids expect_popup() which browsers can block
        for a second consecutive popup on the same page.
        """
        link = page.get_by_role("link", name="privacy policy")
        expect(link).to_be_visible()
        href = link.get_attribute("href")
        assert href and "privacy" in href.lower(), (
            f"Privacy policy link href unexpected: {href}"
        )


# ── OTP Modal ─────────────────────────────────────────────────────────────────
# Session-scoped so the form is submitted exactly once.
# _fill_full_form_and_reach_otp handles both server paths:
#   1. Email form appears → fill everything → submit → OTP modal
#   2. Server skips to OTP directly (phone used recently = rate limited)

@pytest.fixture(scope="session")
def otp_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hayop.atlas.kitchen/signup", wait_until="domcontentloaded", timeout=60000)
    _fill_full_form_and_reach_otp(page)
    yield page
    context.close()


class TestOTPModal:

    def test_otp_modal_visible(self, otp_page):
        expect(SL.otp_dialog(otp_page)).to_be_visible()
        expect(otp_page.locator(SL.TEXT_OTP_HEADING)).to_be_visible()
        expect(otp_page.locator(SL.TEXT_OTP_INSTRUCTION)).to_be_visible()

    def test_otp_input_fields_visible(self, otp_page):
        for n in range(1, 7):
            expect(SL.otp_input(otp_page, n)).to_be_visible()

    def test_code_sent_and_resend_visible(self, otp_page):
        expect(otp_page.locator(SL.TEXT_CODE_SENT)).to_be_visible()
        expect(otp_page.locator(SL.TEXT_RESEND)).to_be_visible()
        expect(SL.powered_by_atlas_in_dialog(otp_page)).to_be_visible()

    def test_resend_code(self, otp_page):
        # Server enforces a 30s cooldown between resends — wait it out.
        otp_page.wait_for_timeout(31000)
        otp_page.locator(SL.TEXT_RESEND).click()
        expect(otp_page.locator(SL.TEXT_CODE_RESENT)).to_be_visible()

    def test_close_modal(self, otp_page):
        otp_page.get_by_role("button", name="Close", exact=True).click()
        expect(otp_page.locator(SL.TEXT_OTP_HEADING)).not_to_be_visible()