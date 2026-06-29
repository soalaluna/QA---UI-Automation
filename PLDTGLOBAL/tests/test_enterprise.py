import pytest
from playwright.sync_api import Page, expect
from locators.enterprise_locators import *

BASE_URL = "https://www.pldtglobal.com/en"


@pytest.fixture(autouse=True)
def navigate_to_enterprise(page: Page):
    page.goto(ENTERPRISE_URL)
    page.wait_for_load_state("networkidle")
    cookie_btn = page.locator(BTN_ACCEPT_COOKIES)
    if cookie_btn.is_visible():
        cookie_btn.click()
    yield


# ── Navigation ────────────────────────────────────────────────────────────────

def test_enterprise_page_loads(page: Page):
    """Enterprise page should load at correct URL"""
    expect(page).to_have_url(ENTERPRISE_URL)


# ── Learn More Links ──────────────────────────────────────────────────────────

def test_learn_more_first_navigates(page: Page):
    """First Learn More link should navigate to contact page"""
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_role("link", name="Learn More").first.click()
    assert "contact-us" in page.url, f"Expected contact-us page, got: {page.url}"

def test_learn_more_2nd_navigates(page: Page):
    """Second Learn More link should navigate"""
    page.goto(ENTERPRISE_URL)
    page.get_by_role("link", name="Learn More").nth(1).click()
    page.wait_for_load_state("networkidle")
    assert page.url != ENTERPRISE_URL, f"Expected navigation away from enterprise page"

def test_learn_more_3rd_navigates(page: Page):
    """Third Learn More link should navigate"""
    page.goto(ENTERPRISE_URL)
    page.get_by_role("link", name="Learn More").nth(2).click()
    page.wait_for_load_state("networkidle")
    assert page.url != ENTERPRISE_URL, f"Expected navigation away from enterprise page"

def test_learn_more_4th_navigates(page: Page):
    """Fourth Learn More link should navigate to Global Connectivity page"""
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_role("link", name="Learn More").nth(3).click()
    assert "global-connectivity" in page.url, f"Expected global-connectivity page, got: {page.url}"

def test_learn_more_5th_navigates(page: Page):
    """Fifth Learn More link should navigate to Managed Network and Cloud page"""
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_role("link", name="Learn More").nth(4).click()
    assert "managed-network" in page.url, f"Expected managed-network page, got: {page.url}"

def test_learn_more_6th_navigates(page: Page):
    """Sixth Learn More link should navigate"""
    page.goto(ENTERPRISE_URL)
    page.get_by_role("link", name="Learn More").nth(5).click()
    page.wait_for_load_state("networkidle")
    assert page.url != ENTERPRISE_URL, f"Expected navigation away from enterprise page"


# ── Contact Form ──────────────────────────────────────────────────────────────

@pytest.fixture()
def goto_contact_form(page: Page):
    """Navigate to contact form via first Learn More link"""
    page.get_by_role("link", name="Learn More").first.click()
    page.wait_for_load_state("networkidle")

def test_salutation_options(page: Page, goto_contact_form):
    """Salutation dropdown should accept all options"""
    for option in ["mr", "mrs", "ms", "dr"]:
        page.get_by_label("Salutation *").select_option(option)
        expect(page.get_by_label("Salutation *")).to_have_value(option)

def test_first_name_fillable(page: Page, goto_contact_form):
    """First Name field should accept input"""
    page.get_by_role("textbox", name="First Name required").fill("Testing")
    expect(page.get_by_role("textbox", name="First Name required")).to_have_value("Testing")

def test_last_name_fillable(page: Page, goto_contact_form):
    """Last Name field should accept input"""
    page.get_by_role("textbox", name="Last Name required").fill("Testing")
    expect(page.get_by_role("textbox", name="Last Name required")).to_have_value("Testing")

def test_company_fillable(page: Page, goto_contact_form):
    """Company field should accept input"""
    page.get_by_role("textbox", name="Company required").fill("Make Technology")
    expect(page.get_by_role("textbox", name="Company required")).to_have_value("Make Technology")

def test_email_fillable(page: Page, goto_contact_form):
    """Email field should accept input"""
    page.get_by_role("textbox", name="Email Address required").fill("testing@mail.com")
    expect(page.get_by_role("textbox", name="Email Address required")).to_have_value("testing@mail.com")

def test_industry_options(page: Page, goto_contact_form):
    """Industry dropdown should accept multiple options"""
    for option in ["technology", "healthcare", "finance", "retail", "manufacturing", "other"]:
        page.get_by_label("Industry *").select_option(option)
        expect(page.get_by_label("Industry *")).to_have_value(option)

def test_position_options(page: Page, goto_contact_form):
    """Position/Job Title dropdown should accept multiple options"""
    for option in ["partnership", "distribution", "reseller", "collaboration"]:
        page.get_by_label("Position/Job Title *").select_option(option)
        expect(page.get_by_label("Position/Job Title *")).to_have_value(option)

def test_message_fillable(page: Page, goto_contact_form):
    """Message field should accept input"""
    page.get_by_role("textbox", name="Message required").fill("testing")
    expect(page.get_by_role("textbox", name="Message required")).to_have_value("testing")


# ── Contact Info Links ────────────────────────────────────────────────────────

def test_email_link_visible(page: Page, goto_contact_form):
    """Email link should be visible in contact section"""
    expect(page.locator("#main").get_by_role("link", name="askus@pldtglobal.com")).to_be_visible()

def test_phone_link_visible(page: Page, goto_contact_form):
    """Phone link should be visible in contact section"""
    expect(page.locator("#main").get_by_role("link", name="(+632) 8886-")).to_be_visible()

def test_address_opens_popup(page: Page, goto_contact_form):
    """Address link should open a new tab"""
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="12F Rufino Pacific Tower").click()
    popup = popup_info.value
    assert popup.url != ""
    popup.close()

def test_linkedin_opens_popup(page: Page, goto_contact_form):
    """LinkedIn link should open a new tab"""
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="linkedin.com/company/").click()
    popup = popup_info.value
    assert "linkedin.com" in popup.url
    popup.close()


# ── Load More & Inquiry ───────────────────────────────────────────────────────

def test_load_more_solutions_clickable(page: Page):
    """Load More Solutions button should be clickable"""
    page.locator(BTN_LOAD_MORE).click()
    expect(page.locator(BTN_LOAD_MORE)).to_be_visible()

def test_send_inquiry_navigates(page: Page):
    """Send an Inquiry link should navigate to contact page"""
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_role("link", name="Send an Inquiry").click()
    assert "contact-us" in page.url, f"Expected contact-us page, got: {page.url}"