import pytest
from playwright.sync_api import Page, expect, Browser
from HAYOPNIMANAM.locators.order_online_locators import OrderOnlineLocators

MAIN_URL        = "https://hayopnimanam.com/"
ORDER_URL       = "https://hayop.atlas.kitchen/"
SIGNUP_URL      = "https://hayop.atlas.kitchen/signup"
LOGIN_URL       = "https://hayop.atlas.kitchen/login"
ITEM_URL        = "https://hayop.atlas.kitchen/items/443-buko-pie"


def test_order_online_opens_new_tab(page: Page, browser: Browser):
    """Clicking ORDER ONLINE from nav should open hayop.atlas.kitchen in a new tab"""
    page.goto(MAIN_URL)
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Go to Page ORDER ONLINE").click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    expect(popup).to_have_url("https://hayop.atlas.kitchen/")


def test_location_search_input_is_present(page: Page):
    """Location/address search text should be present on the ordering homepage"""
    page.goto(ORDER_URL)
    page.wait_for_load_state("domcontentloaded")
    # Use the desktop-visible version (nth 1 skips the hidden mobile one)
    location_dropdown = page.get_by_text("Select a delivery/pickup").nth(1)
    expect(location_dropdown).to_be_visible()


def test_location_search_navigates_to_menu(page: Page):
    """Clicking the location dropdown should navigate to the menu/ordering page"""
    page.goto(ORDER_URL)
    page.wait_for_load_state("domcontentloaded")
    # Clicking the dropdown navigates directly to menu — verify menu loads
    page.get_by_text("Select a delivery/pickup").nth(1).click()
    page.wait_for_load_state("domcontentloaded")
    # Menu page should show at least one food item
    expect(page.get_by_role("heading", name="Starters")).to_be_visible()


def test_signup_page_loads(page: Page):
    """Sign up page should load with phone field and Continue with email button"""
    page.goto(SIGNUP_URL)
    page.wait_for_load_state("domcontentloaded")
    expect(page.get_by_role("textbox", name="Contact number")).to_be_visible()
    expect(page.get_by_role("button", name="Continue with email")).to_be_visible()


def test_signup_form_accepts_phone_input(page: Page):
    """Sign up phone field should accept a phone number"""
    page.goto(SIGNUP_URL)
    page.wait_for_load_state("domcontentloaded")
    phone_input = page.get_by_role("textbox", name="Contact number")
    phone_input.fill("+65 9823 9223")
    expect(phone_input).not_to_be_empty()


def test_signup_email_flow(page: Page):
    """Clicking Continue with email should reveal the email field"""
    page.goto(SIGNUP_URL)
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("button", name="Continue with email").click()
    page.wait_for_timeout(500)
    # After clicking, only email field appears on this step
    expect(page.get_by_role("textbox", name="Enter your email")).to_be_visible()
    # Continue with phone button should also appear as alternative
    expect(page.get_by_role("button", name="Continue with phone")).to_be_visible()


def test_login_page_loads(page: Page):
    """Login page should load with phone number input and country selector"""
    page.goto(LOGIN_URL)
    page.wait_for_load_state("domcontentloaded")
    expect(page.get_by_role("textbox", name="Contact number")).to_be_visible()
    expect(page.get_by_label("Phone number country")).to_be_visible()


def test_login_country_selector_works(page: Page):
    """Country selector on login page should allow changing to PH"""
    page.goto(LOGIN_URL)
    page.wait_for_load_state("domcontentloaded")
    country_select = page.get_by_label("Phone number country")
    country_select.select_option("PH")
    expect(country_select).to_have_value("PH")


def test_login_phone_accepts_input(page: Page):
    """Login phone field should accept a phone number"""
    page.goto(LOGIN_URL)
    page.wait_for_load_state("domcontentloaded")
    phone_input = page.get_by_role("textbox", name="Contact number")
    phone_input.fill("+63 968 422 4829")
    expect(phone_input).not_to_be_empty()


def test_item_page_loads(page: Page):
    """Buko Pie item page should load with special instructions field"""
    page.goto(ITEM_URL)
    page.wait_for_load_state("domcontentloaded")
    notes_input = page.get_by_role("textbox", name="Let us know of any special")
    expect(notes_input).to_be_visible()


def test_item_special_notes_accepts_input(page: Page):
    """Special instructions field on item page should accept text input"""
    page.goto(ITEM_URL)
    page.wait_for_load_state("domcontentloaded")
    notes_input = page.get_by_role("textbox", name="Let us know of any special")
    notes_input.fill("no pie")
    expect(notes_input).to_have_value("no pie")