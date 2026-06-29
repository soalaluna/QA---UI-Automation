import pytest
from playwright.sync_api import Page, expect
from locators.careers_locators import (
    BASE_URL, CAREERS_URL, CAREERS_URL_AFTER_SUBMIT,
    NAV_CAREERS,
    OPENINGS_HEADING, OPENINGS_HEADING_ICON,
    SLIDE_FIRST, SLIDE_SECOND,
    BTN_APPLY,
    FORM_NAME, FORM_EMAIL, FORM_CONTACT, FORM_SUBJECT, FORM_MESSAGE,
    BTN_SUBMIT, BTN_OK,
)


# ── Nav to Careers ────────────────────────────────────────────────────────────

def test_careers_nav_link_visible(page: Page):
    """Careers link should be visible in the navigation"""
    page.goto(BASE_URL)
    expect(page.locator(NAV_CAREERS)).to_be_visible()

def test_careers_nav_link_navigates(page: Page):
    """Clicking Careers nav link should navigate to the careers page"""
    page.goto(BASE_URL)
    page.locator(NAV_CAREERS).click()
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(CAREERS_URL)


# ── Careers Page Content ──────────────────────────────────────────────────────

def test_openings_heading_visible(page: Page):
    """Openings heading should be present on the careers page"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(OPENINGS_HEADING)).to_be_attached()

def test_openings_heading_icon_visible(page: Page):
    """Icon inside the Openings heading should be present"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(OPENINGS_HEADING_ICON)).to_be_attached()

def test_job_slide_first_visible(page: Page):
    """First job listing slide should be present"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(SLIDE_FIRST)).to_be_attached()

def test_job_slide_second_visible(page: Page):
    """Second job listing slide should be present"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(SLIDE_SECOND)).to_be_attached()

def test_apply_button_visible(page: Page):
    """Apply button should be visible on the careers page"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(BTN_APPLY)).to_be_visible()


# ── Application Form ──────────────────────────────────────────────────────────

def test_form_opens_on_apply_click(page: Page):
    """Clicking Apply should reveal the application form"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(FORM_NAME)).to_be_visible()

def test_form_name_field_visible(page: Page):
    """Name field should be visible after clicking Apply"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(FORM_NAME)).to_be_visible()

def test_form_email_field_visible(page: Page):
    """Email field should be visible after clicking Apply"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(FORM_EMAIL)).to_be_visible()

def test_form_contact_field_visible(page: Page):
    """Contact number field should be visible after clicking Apply"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(FORM_CONTACT)).to_be_visible()

def test_form_subject_field_visible(page: Page):
    """Subject field should be visible after clicking Apply"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(FORM_SUBJECT)).to_be_visible()

def test_form_message_field_visible(page: Page):
    """Message field should be visible after clicking Apply"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(FORM_MESSAGE)).to_be_visible()

def test_form_submit_button_visible(page: Page):
    """Submit button should be visible after clicking Apply"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    expect(page.locator(BTN_SUBMIT)).to_be_visible()


# ── Form Input Interaction ────────────────────────────────────────────────────

def test_form_name_field_accepts_input(page: Page):
    """Name field should accept text input"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    page.locator(FORM_NAME).fill("testing")
    expect(page.locator(FORM_NAME)).to_have_value("testing")

def test_form_email_field_accepts_input(page: Page):
    """Email field should accept text input"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    page.locator(FORM_EMAIL).fill("testing@gmail.com")
    expect(page.locator(FORM_EMAIL)).to_have_value("testing@gmail.com")

def test_form_contact_field_accepts_input(page: Page):
    """Contact number field should accept text input"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    page.locator(FORM_CONTACT).fill("09123456789")
    expect(page.locator(FORM_CONTACT)).to_have_value("09123456789")

def test_form_subject_field_accepts_input(page: Page):
    """Subject field should accept text input"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    page.locator(FORM_SUBJECT).fill("careers")
    expect(page.locator(FORM_SUBJECT)).to_have_value("careers")

def test_form_message_field_accepts_input(page: Page):
    """Message field should accept text input"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()
    page.locator(FORM_MESSAGE).fill("career")
    expect(page.locator(FORM_MESSAGE)).to_have_value("career")


# ── Full Form Submission Flow ─────────────────────────────────────────────────

def test_form_full_submission_flow(page: Page):
    """Filling and submitting the form should show a confirmation dialog"""
    page.goto(CAREERS_URL)
    page.wait_for_load_state("networkidle")
    page.locator(BTN_APPLY).click()

    page.locator(FORM_NAME).fill("testing")
    page.locator(FORM_EMAIL).fill("testing@gmail.com")
    page.locator(FORM_CONTACT).fill("09123456789")
    page.locator(FORM_SUBJECT).fill("careers")
    page.locator(FORM_MESSAGE).fill("career")

    page.locator(BTN_SUBMIT).click()

    # Confirm the OK dialog appears after submission
    expect(page.locator(BTN_OK)).to_be_visible()
    page.locator(BTN_OK).click()

    # After dismissing, page lands on #openings anchor
    expect(page).to_have_url(CAREERS_URL_AFTER_SUBMIT)