import pytest
from playwright.sync_api import Page, expect
from locators.contact_locators import (
    BASE_URL, CONTACT_URL,
    BTN_ACCEPT_COOKIES, NAV_CONTACT_BTN,
    BTN_ENTERPRISE, BTN_CARRIER,
    FORM_TYPE_GROUP, RADIO_HYPERSCALER, RADIO_CARRIER_DATA, RADIO_CARRIER_BUYING,
    BTN_SUBMIT,
    FIELD_SALUTATION, FIELD_FIRST_NAME, FIELD_LAST_NAME,
    FIELD_COMPANY, FIELD_EMAIL, FIELD_MESSAGE,
    FIELD_INDUSTRY, FIELD_POSITION,
    FIELD_PHONE, FIELD_MOBILE, FIELD_COUNTRY, FIELD_INQUIRY,
    FIELD_CITY, FIELD_STATE, FIELD_REGION,
    CONTACT_EMAIL, CONTACT_PHONE, CONTACT_ADDRESS, CONTACT_LINKEDIN,
)


@pytest.fixture(autouse=True)
def setup(page: Page):
    page.goto(CONTACT_URL)
    page.wait_for_load_state("networkidle")
    cookie_btn = page.locator(BTN_ACCEPT_COOKIES)
    if cookie_btn.is_visible():
        cookie_btn.click()


# ── Nav to Contact ────────────────────────────────────────────────────────────

def test_contact_nav_btn_visible(page: Page):
    """Contact us button should be visible on the homepage"""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(NAV_CONTACT_BTN)).to_be_visible()

def test_contact_nav_btn_navigates(page: Page):
    """Clicking contact us button should navigate to contact page"""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator(NAV_CONTACT_BTN).click()
    page.wait_for_load_state("networkidle")
    assert "contact" in page.url.lower(), f"Expected contact page, got: {page.url}"


# ── Page Load ─────────────────────────────────────────────────────────────────

def test_contact_page_loads(page: Page):
    """Contact page should load successfully"""
    assert "contact" in page.url.lower(), f"Expected contact page, got: {page.url}"

def test_submit_button_visible(page: Page):
    """Submit form button should be visible"""
    expect(page.locator(BTN_SUBMIT)).to_be_visible()

def test_enterprise_tab_visible(page: Page):
    """Enterprise tab button should be visible"""
    expect(page.locator(BTN_ENTERPRISE)).to_be_visible()

def test_carrier_tab_visible(page: Page):
    """Carrier tab button should be visible"""
    expect(page.locator(BTN_CARRIER)).to_be_visible()


# ── Default (Consumer) Form Fields ───────────────────────────────────────────

def test_salutation_field_visible(page: Page):
    """Salutation dropdown should be visible"""
    expect(page.locator(FIELD_SALUTATION)).to_be_visible()

def test_salutation_options(page: Page):
    """Salutation dropdown should have all options"""
    page.locator(FIELD_SALUTATION).select_option("mr")
    page.locator(FIELD_SALUTATION).select_option("mrs")
    page.locator(FIELD_SALUTATION).select_option("ms")
    page.locator(FIELD_SALUTATION).select_option("dr")

def test_first_name_field_visible(page: Page):
    """First Name field should be visible"""
    expect(page.locator(FIELD_FIRST_NAME)).to_be_visible()

def test_first_name_accepts_input(page: Page):
    """First Name field should accept text input"""
    page.locator(FIELD_FIRST_NAME).fill("Testing")
    expect(page.locator(FIELD_FIRST_NAME)).to_have_value("Testing")

def test_last_name_field_visible(page: Page):
    """Last Name field should be visible"""
    expect(page.locator(FIELD_LAST_NAME)).to_be_visible()

def test_last_name_accepts_input(page: Page):
    """Last Name field should accept text input"""
    page.locator(FIELD_LAST_NAME).fill("Testing")
    expect(page.locator(FIELD_LAST_NAME)).to_have_value("Testing")

def test_company_field_visible(page: Page):
    """Company field should be visible"""
    expect(page.locator(FIELD_COMPANY)).to_be_visible()

def test_company_accepts_input(page: Page):
    """Company field should accept text input"""
    page.locator(FIELD_COMPANY).fill("Make Tech")
    expect(page.locator(FIELD_COMPANY)).to_have_value("Make Tech")

def test_email_field_visible(page: Page):
    """Email Address field should be visible"""
    expect(page.locator(FIELD_EMAIL)).to_be_visible()

def test_email_accepts_input(page: Page):
    """Email Address field should accept text input"""
    page.locator(FIELD_EMAIL).fill("testing@mail.com")
    expect(page.locator(FIELD_EMAIL)).to_have_value("testing@mail.com")

def test_industry_field_visible(page: Page):
    """Industry dropdown should be visible"""
    expect(page.locator(FIELD_INDUSTRY)).to_be_visible()

def test_industry_options(page: Page):
    """Industry dropdown should have expected options"""
    for option in ["technology", "healthcare", "finance", "retail", "manufacturing", "other"]:
        page.locator(FIELD_INDUSTRY).select_option(option)

def test_position_field_visible(page: Page):
    """Position/Job Title dropdown should be visible"""
    expect(page.locator(FIELD_POSITION)).to_be_visible()

def test_position_options(page: Page):
    """Position/Job Title dropdown should have expected options"""
    for option in ["partnership", "distribution", "reseller", "collaboration"]:
        page.locator(FIELD_POSITION).select_option(option)

def test_message_field_visible(page: Page):
    """Message field should be visible"""
    expect(page.locator(FIELD_MESSAGE)).to_be_visible()

def test_message_accepts_input(page: Page):
    """Message field should accept text input"""
    page.locator(FIELD_MESSAGE).fill("testing")
    expect(page.locator(FIELD_MESSAGE)).to_have_value("testing")


# ── Enterprise Form ───────────────────────────────────────────────────────────

def test_enterprise_tab_switches_form(page: Page):
    """Clicking Enterprise tab should reveal enterprise-specific fields"""
    page.locator(BTN_ENTERPRISE).click()
    page.wait_for_timeout(500)
    expect(page.locator(FIELD_PHONE)).to_be_visible()

def test_enterprise_phone_accepts_input(page: Page):
    """Enterprise Phone field should accept input"""
    page.locator(BTN_ENTERPRISE).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_PHONE).fill("+63 912 345 6790")
    expect(page.locator(FIELD_PHONE)).to_have_value("+63 912 345 6790")

def test_enterprise_mobile_accepts_input(page: Page):
    """Enterprise Mobile field should accept input"""
    page.locator(BTN_ENTERPRISE).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_MOBILE).fill("+63 912 345 6789")
    expect(page.locator(FIELD_MOBILE)).to_have_value("+63 912 345 6789")

def test_enterprise_country_accepts_input(page: Page):
    """Enterprise Country field should accept input"""
    page.locator(BTN_ENTERPRISE).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_COUNTRY).fill("Philippines")
    expect(page.locator(FIELD_COUNTRY)).to_have_value("Philippines")

def test_enterprise_inquiry_accepts_input(page: Page):
    """Enterprise Inquiry field should accept input"""
    page.locator(BTN_ENTERPRISE).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_INQUIRY).fill("testing")
    expect(page.locator(FIELD_INQUIRY)).to_have_value("testing")


# ── Carrier Form ──────────────────────────────────────────────────────────────

def test_carrier_tab_switches_form(page: Page):
    """Clicking Carrier tab should reveal carrier-specific fields"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    expect(page.locator(FORM_TYPE_GROUP)).to_be_visible()

def test_carrier_radio_hyperscaler(page: Page):
    """Hyperscaler radio button should be selectable"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(RADIO_HYPERSCALER).check()
    expect(page.locator(RADIO_HYPERSCALER)).to_be_checked()

def test_carrier_radio_carrier_data(page: Page):
    """Carrier Data radio button should be selectable"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(RADIO_CARRIER_DATA).check()
    expect(page.locator(RADIO_CARRIER_DATA)).to_be_checked()

def test_carrier_radio_carrier_buying(page: Page):
    """Carrier Buying radio button should be selectable"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(RADIO_CARRIER_BUYING).check()
    expect(page.locator(RADIO_CARRIER_BUYING)).to_be_checked()

def test_carrier_city_accepts_input(page: Page):
    """Carrier City field should accept input"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_CITY).fill("Manila")
    expect(page.locator(FIELD_CITY)).to_have_value("Manila")

def test_carrier_state_accepts_input(page: Page):
    """Carrier State/Province field should accept input"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_STATE).fill("Manila")
    expect(page.locator(FIELD_STATE)).to_have_value("Manila")

def test_carrier_country_accepts_input(page: Page):
    """Carrier Country field should accept input"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_COUNTRY).fill("Philippines")
    expect(page.locator(FIELD_COUNTRY)).to_have_value("Philippines")

def test_carrier_region_accepts_input(page: Page):
    """Carrier Region field should accept input"""
    page.locator(BTN_CARRIER).click()
    page.wait_for_timeout(500)
    page.locator(FIELD_REGION).fill("NCR")
    expect(page.locator(FIELD_REGION)).to_have_value("NCR")


# ── Contact Info ──────────────────────────────────────────────────────────────

def test_contact_email_visible(page: Page):
    """Contact email should be visible on the page"""
    expect(page.locator(CONTACT_EMAIL)).to_be_visible()

def test_contact_email_href(page: Page):
    """Contact email should have correct mailto href"""
    href = page.locator(CONTACT_EMAIL).get_attribute("href")
    assert "askus@pldtglobal.com" in href, f"Unexpected href: {href}"

def test_contact_phone_visible(page: Page):
    """Contact phone should be visible on the page"""
    expect(page.locator(CONTACT_PHONE)).to_be_visible()

def test_contact_phone_href(page: Page):
    """Contact phone should have correct tel href"""
    href = page.locator(CONTACT_PHONE).get_attribute("href")
    assert "tel:" in href, f"Unexpected href: {href}"

def test_contact_address_visible(page: Page):
    """Office address link should be visible"""
    expect(page.locator(CONTACT_ADDRESS)).to_be_visible()

def test_contact_address_opens_maps(page: Page):
    """Office address link should open Google Maps"""
    with page.expect_popup() as popup_info:
        page.locator(CONTACT_ADDRESS).click()
    popup = popup_info.value
    assert "google.com/maps" in popup.url or "maps.google" in popup.url, \
        f"Expected Google Maps, got: {popup.url}"

def test_contact_linkedin_visible(page: Page):
    """LinkedIn link should be visible on the contact page"""
    expect(page.locator(CONTACT_LINKEDIN)).to_be_visible()

def test_contact_linkedin_href(page: Page):
    """LinkedIn link should point to LinkedIn"""
    href = page.locator(CONTACT_LINKEDIN).get_attribute("href")
    assert "linkedin.com" in href, f"Unexpected href: {href}"