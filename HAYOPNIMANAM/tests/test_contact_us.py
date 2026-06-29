import pytest
from playwright.sync_api import Page, expect
from HAYOPNIMANAM.locators.contact_us_locators import ContactLocators as CL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_contact(page: Page):
    page.goto(CL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.locator(CL.NAV_CONTACT).first.click()
    page.wait_for_url("**/contact-us/**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestContactNavigation:

    def test_contact_page_loads(self, page: Page):
        expect(page).to_have_url(CL.CONTACT_URL)

    def test_nav_contact_reloads_contact_page(self, page: Page):
        page.locator(CL.NAV_CONTACT).first.click()
        expect(page).to_have_url(CL.CONTACT_URL)


# ── Email Link Tests ──────────────────────────────────────────────────────────

class TestContactEmails:

    def test_amoy_email_has_correct_mailto(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        link = page.locator(CL.LINK_EMAIL_AMOY)
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", "mailto:amoy.street@hayopnimanam.com")

    def test_moment_email_has_correct_mailto(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        link = page.locator(CL.LINK_EMAIL_MOMENT)
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", "mailto:momentgroup@hayopnimanam.com")


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestContactFooter:

    def test_instagram_link_present(self, page: Page):
        expect(page.locator(CL.FOOTER_INSTAGRAM)).to_be_attached()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(CL.FOOTER_PRIVACY).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(CL.FOOTER_TERMS).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")