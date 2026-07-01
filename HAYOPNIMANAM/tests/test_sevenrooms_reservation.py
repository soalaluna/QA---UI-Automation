import re
import pytest
from playwright.sync_api import Page, expect
from locators.sevenrooms_reservation_locators import (
    BASE_URL,
    IMG_ANY, LABEL_MAKE_RESERVATION, BTN_SPECIAL_ATTENTION, TEXT_POWERED_BY,
    BTN_DATE, BTN_GUEST_COUNT, BTN_TIME, BTN_SEARCH,
    BANNER_INFO, BTN_BACK_ARROW, MAIN_RESULT_BLOCK,
    OTHER_DATES_COLLAPSED, SEVENROOMS_LINK,
    TEXT_HOLDING_TABLE, TEXT_SELECT_OPTION,
    BTN_FACEBOOK_LOGIN, BTN_GUEST_LOGIN,
    TEXT_YOUR_INFORMATION,
    FIELD_FIRST_NAME, FIELD_LAST_NAME, FIELD_EMAIL, FIELD_PHONE,
    FIELD_BIRTHDAY, TEXT_CREDIT_CARD_REQUIRED, PAYMENT_SECTION,
    TEXT_SUMMARY, ROW_VENUE_NAME, ROW_DATE_TIME, ROW_GUEST_COUNT,
    TEXT_DIETARY_RESTRICTIONS, TEXT_SPECIAL_OCCASIONS,
    GUEST_NOTES, TEXT_CANCELLATION_POLICY,
    BTN_DIETARY_ADD, BTN_SPECIAL_OCCASION_ADD,
    BTN_TAG_CANCEL, BTN_TAG_SAVE, TAB_YOURS, TAB_YOUR_GUESTS,
    FIELD_GUEST_NOTE, BTN_GUEST_NOTES_SAVE,
    TEXT_SUBMIT_DISCLAIMER, BTN_SUBMIT,
)


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(BASE_URL)
    page.wait_for_timeout(3000)


# ── Page Load ──────────────────────────────────────────────────────────────────

def test_page_image_visible(page: Page):
    expect(page.locator(IMG_ANY).first).to_be_visible()

def test_make_reservation_label_visible(page: Page):
    expect(page.locator(LABEL_MAKE_RESERVATION)).to_be_visible()

def test_special_attention_button_visible(page: Page):
    expect(page.locator(BTN_SPECIAL_ATTENTION)).to_be_visible()

def test_powered_by_sevenrooms_visible(page: Page):
    expect(page.locator(TEXT_POWERED_BY)).to_be_visible()


# ── Booking Form ───────────────────────────────────────────────────────────────

def test_date_button_visible(page: Page):
    expect(page.locator(BTN_DATE)).to_be_visible()

def test_guest_count_button_visible(page: Page):
    expect(page.locator(BTN_GUEST_COUNT)).to_be_visible()

def test_time_button_visible(page: Page):
    expect(page.locator(BTN_TIME)).to_be_visible()

def test_search_button_visible(page: Page):
    expect(page.locator(BTN_SEARCH)).to_be_visible()

def test_date_button_opens_calendar(page: Page):
    page.locator(BTN_DATE).click()
    page.wait_for_timeout(500)
    # Calendar should show increment/decrement arrows
    expect(page.locator("[data-test='sr-increment-arrow']").first).to_be_visible()

def test_guest_count_button_opens_selector(page: Page):
    page.locator(BTN_GUEST_COUNT).click()
    page.wait_for_timeout(500)
    expect(page.locator("[data-test='sr-increment-arrow']").first).to_be_visible()

def test_time_button_opens_selector(page: Page):
    page.locator(BTN_TIME).click()
    page.wait_for_timeout(500)
    expect(page.locator("[data-test='sr-increment-arrow']").first).to_be_visible()


# ── Search Results ─────────────────────────────────────────────────────────────

@pytest.fixture
def search_results(page: Page):
    """Run a search using the default date/guests/time steppers."""
    page.goto(BASE_URL)
    page.wait_for_timeout(3000)
    # Increment date by 1 to get tomorrow (avoids same-day cutoff issues)
    page.locator(BTN_DATE).click()
    page.wait_for_timeout(300)
    page.locator("[data-test='sr-calendar-date'] [data-test='sr-increment-arrow']").click()
    # Increment guests to 2
    page.locator(BTN_GUEST_COUNT).click()
    page.wait_for_timeout(300)
    page.locator("[data-test='sr-guest-count'] [data-test='sr-increment-arrow']").click()
    # Search
    page.locator(BTN_SEARCH).click()
    page.wait_for_timeout(3000)


def test_search_results_back_arrow_visible(page: Page, search_results):
    expect(page.locator(BTN_BACK_ARROW)).to_be_visible()

def test_search_results_main_block_visible(page: Page, search_results):
    expect(page.locator(MAIN_RESULT_BLOCK)).to_be_visible()

def test_search_results_has_time_slots(page: Page, search_results):
    """At least one time slot button should appear after searching."""
    slots = page.locator("[data-test='sr-main-result-block'] button")
    assert slots.count() > 0, "No time slots found in search results"

def test_other_dates_collapsed_visible(page: Page, search_results):
    expect(page.locator(OTHER_DATES_COLLAPSED)).to_be_visible()

def test_sevenrooms_link_visible(page: Page, search_results):
    expect(page.locator(SEVENROOMS_LINK)).to_be_visible()


# ── Login / Auth Step ──────────────────────────────────────────────────────────

@pytest.fixture
def at_login(page: Page, search_results):
    """Click the first available time slot to reach the login screen."""
    first_slot = page.locator("[data-test='sr-main-result-block'] button").first
    first_slot.wait_for(state="visible", timeout=10000)
    first_slot.click()
    page.wait_for_timeout(2000)


def test_holding_table_text_visible(page: Page, at_login):
    expect(page.locator(TEXT_HOLDING_TABLE)).to_be_visible()

def test_select_option_text_visible(page: Page, at_login):
    expect(page.locator(TEXT_SELECT_OPTION)).to_be_visible()

def test_facebook_login_button_visible(page: Page, at_login):
    expect(page.locator(BTN_FACEBOOK_LOGIN)).to_be_visible()

def test_guest_login_button_visible(page: Page, at_login):
    expect(page.locator(BTN_GUEST_LOGIN)).to_be_visible()


# ── Reservation Form ───────────────────────────────────────────────────────────

@pytest.fixture
def at_form(page: Page, at_login):
    """Continue as guest to reach the reservation form."""
    page.locator(BTN_GUEST_LOGIN).click()
    page.wait_for_timeout(3000)


def test_form_your_information_visible(page: Page, at_form):
    expect(page.locator(TEXT_YOUR_INFORMATION)).to_be_visible()

def test_form_first_name_visible(page: Page, at_form):
    expect(page.locator(FIELD_FIRST_NAME)).to_be_visible()

def test_form_last_name_visible(page: Page, at_form):
    expect(page.locator(FIELD_LAST_NAME)).to_be_visible()

def test_form_email_visible(page: Page, at_form):
    expect(page.locator(FIELD_EMAIL)).to_be_visible()

def test_form_phone_visible(page: Page, at_form):
    expect(page.locator(FIELD_PHONE)).to_be_visible()

def test_form_birthday_visible(page: Page, at_form):
    expect(page.locator(FIELD_BIRTHDAY)).to_be_visible()

def test_form_summary_visible(page: Page, at_form):
    expect(page.locator(TEXT_SUMMARY)).to_be_visible()

def test_form_venue_name_row_visible(page: Page, at_form):
    expect(page.locator(ROW_VENUE_NAME)).to_be_visible()

def test_form_date_time_row_visible(page: Page, at_form):
    expect(page.locator(ROW_DATE_TIME)).to_be_visible()

def test_form_guest_count_row_visible(page: Page, at_form):
    expect(page.locator(ROW_GUEST_COUNT)).to_be_visible()

def test_form_dietary_restrictions_visible(page: Page, at_form):
    expect(page.locator(TEXT_DIETARY_RESTRICTIONS)).to_be_visible()

def test_form_special_occasions_visible(page: Page, at_form):
    expect(page.locator(TEXT_SPECIAL_OCCASIONS)).to_be_visible()

def test_form_cancellation_policy_visible(page: Page, at_form):
    expect(page.locator(TEXT_CANCELLATION_POLICY)).to_be_visible()

def test_form_submit_button_visible(page: Page, at_form):
    expect(page.locator(BTN_SUBMIT)).to_be_visible()


# ── Dietary Tags ───────────────────────────────────────────────────────────────

def test_dietary_add_opens_selector(page: Page, at_form):
    page.locator(BTN_DIETARY_ADD).click()
    page.wait_for_timeout(300)
    expect(page.locator(BTN_TAG_CANCEL)).to_be_visible()
    expect(page.locator(BTN_TAG_SAVE)).to_be_visible()
    expect(page.locator(TAB_YOURS)).to_be_visible()
    expect(page.locator(TAB_YOUR_GUESTS)).to_be_visible()


# ── Special Occasions ──────────────────────────────────────────────────────────

def test_special_occasion_add_opens_selector(page: Page, at_form):
    page.locator(BTN_SPECIAL_OCCASION_ADD).click()
    page.wait_for_timeout(300)
    expect(page.locator(BTN_TAG_CANCEL)).to_be_visible()
    expect(page.locator(BTN_TAG_SAVE)).to_be_visible()


# ── Guest Notes ────────────────────────────────────────────────────────────────

def test_guest_notes_field_accepts_input(page: Page, at_form):
    page.locator(GUEST_NOTES).click()
    page.wait_for_timeout(300)
    expect(page.locator(FIELD_GUEST_NOTE)).to_be_visible()
    page.locator(FIELD_GUEST_NOTE).fill("testing")
    expect(page.locator(FIELD_GUEST_NOTE)).to_have_value("testing")
    page.locator(BTN_GUEST_NOTES_SAVE).click()