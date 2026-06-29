import pytest
from playwright.sync_api import Page, expect
from locators.careers_locators import CareersLocators as CL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_careers(page: Page):
    page.goto(CL.BASE_URL, wait_until="domcontentloaded", timeout=60000)
    page.locator(CL.NAV_CAREERS).click()
    page.wait_for_url("**/careers**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestCareersNavigation:

    def test_careers_page_loads(self, page: Page):
        expect(page).to_have_url(CL.CAREERS_URL)


# ── Job Listing Tests ─────────────────────────────────────────────────────────

class TestJobListings:

    def test_apply_links_present(self, page: Page):
        """Multiple 'Apply' links should be present for job listings."""
        links = page.locator(CL.LINK_APPLY)
        assert links.count() > 0, "No Apply links found on careers page"

    def test_first_apply_link_navigates(self, page: Page):
        """Clicking the first Apply link should navigate to a job application page."""
        page.locator(CL.LINK_APPLY).first.click()
        expect(page).not_to_have_url(CL.CAREERS_URL)

    def test_linkedin_link_opens_popup(self, page: Page):
        """'Go to LinkedIn' link should open LinkedIn in a new tab."""
        with page.expect_popup() as popup_info:
            page.locator(CL.LINK_GO_TO_LINKEDIN).click()
        popup = popup_info.value
        assert "linkedin.com" in popup.url
        popup.close()


# ── Application Form Tests ────────────────────────────────────────────────────

class TestApplicationForm:

    @pytest.fixture(autouse=True)
    def open_application_form(self, page: Page):
        """Navigate to the first job's application form."""
        page.locator(CL.LINK_APPLY).first.click()
        page.locator(CL.BTN_SUBMIT_APPLICATION_FORM).wait_for(state="visible", timeout=10000)
        page.locator(CL.BTN_SUBMIT_APPLICATION_FORM).click()
        page.locator(CL.FIELD_FIRST_NAME).wait_for(state="visible", timeout=10000)

    def test_salutation_dropdown_selectable(self, page: Page):
        """Salutation dropdown should support all options."""
        for option in ["mr", "mrs", "ms", "dr"]:
            page.locator(CL.FIELD_SALUTATION).select_option(option)
            expect(page.locator(CL.FIELD_SALUTATION)).to_have_value(option)

    def test_first_name_field_fillable(self, page: Page):
        page.locator(CL.FIELD_FIRST_NAME).fill("Testing")
        expect(page.locator(CL.FIELD_FIRST_NAME)).to_have_value("Testing")

    def test_last_name_field_fillable(self, page: Page):
        page.locator(CL.FIELD_LAST_NAME).fill("Testing")
        expect(page.locator(CL.FIELD_LAST_NAME)).to_have_value("Testing")

    def test_email_field_fillable(self, page: Page):
        page.locator(CL.FIELD_EMAIL).fill("testing@mail.com")
        expect(page.locator(CL.FIELD_EMAIL)).to_have_value("testing@mail.com")

    def test_contact_number_field_fillable(self, page: Page):
        page.locator(CL.FIELD_CONTACT_NUMBER).fill("+639 123 456 7890")
        expect(page.locator(CL.FIELD_CONTACT_NUMBER)).to_have_value("+639 123 456 7890")

    def test_linkedin_url_field_fillable(self, page: Page):
        page.locator(CL.FIELD_LINKEDIN_URL).fill("https://linkedin.com/testing")
        expect(page.locator(CL.FIELD_LINKEDIN_URL)).to_have_value("https://linkedin.com/testing")

    def test_upload_icon_visible(self, page: Page):
        """Resume upload control should be present and clickable."""
        expect(page.locator(CL.BTN_UPLOAD_ICON)).to_be_visible()

    def test_apply_now_link_visible_on_application_page(self, page: Page):
        """'Apply Now' CTA should be present on the job application page itself."""
        expect(page.locator(CL.LINK_APPLY_NOW)).to_be_visible()