import pytest
from playwright.sync_api import Page, expect
from locators.contact_us_locators import ContactLocators as CL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_contact(page: Page):
    page.goto(CL.CONTACT_URL)
    yield


# ── Page Content Tests ────────────────────────────────────────────────────────

class TestContactContent:

    def test_contact_us_heading_visible(self, page: Page):
        expect(page.locator(CL.HEADING_CONTACT_US)).to_be_visible()

    def test_kamusta_ka_heading_visible(self, page: Page):
        expect(page.locator(CL.HEADING_KAMUSTA_KA)).to_be_visible()

    def test_address_visible(self, page: Page):
        expect(page.locator(CL.TEXT_ADDRESS)).to_be_visible()

    def test_phone_visible(self, page: Page):
        expect(page.locator(CL.TEXT_PHONE)).to_be_visible()

    def test_inquiries_reservations_label_visible(self, page: Page):
        expect(page.locator(CL.TEXT_INQUIRIES_RESERVATIONS)).to_be_visible()

    def test_brand_business_label_visible(self, page: Page):
        expect(page.locator(CL.TEXT_BRAND_BUSINESS)).to_be_visible()

    def test_kalachuchi_image_visible(self, page: Page):
        expect(page.locator(CL.IMG_KALACHUCHI)).to_be_visible()

    def test_leaf_image_visible(self, page: Page):
        expect(page.locator(CL.IMG_LEAF)).to_be_visible()


# ── Email Link Tests ──────────────────────────────────────────────────────────

class TestContactEmails:

    def test_amoy_email_link_visible(self, page: Page):
        expect(page.locator(CL.LINK_EMAIL_AMOY)).to_be_visible()

    def test_amoy_email_has_correct_mailto(self, page: Page):
        link = page.locator(CL.LINK_EMAIL_AMOY)
        expect(link).to_have_attribute("href", "mailto:amoy.street@hayopnimanam.com")

    def test_moment_email_link_visible(self, page: Page):
        expect(page.locator(CL.LINK_EMAIL_MOMENT)).to_be_visible()

    def test_moment_email_has_correct_mailto(self, page: Page):
        link = page.locator(CL.LINK_EMAIL_MOMENT)
        expect(link).to_have_attribute("href", "mailto:momentgroup@hayopnimanam.com")