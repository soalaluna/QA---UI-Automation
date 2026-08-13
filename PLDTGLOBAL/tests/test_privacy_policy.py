import pytest
from playwright.sync_api import Page, expect
from locators.privacy_policy_locators import PrivacyPolicyLocators as PL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_privacy_page(page: Page):
    # Try to navigate with a longer wait
    page.goto(PL.URL, wait_until="networkidle", timeout=60000)
    
    # Increase the timeout for the cookie banner
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=10000)
        # Wait for the banner to animate away
        page.wait_for_timeout(1000) 
    except Exception:
        pass 
        
    yield


# ── Header & Intro ────────────────────────────────────────────────────────────

class TestPrivacyPolicyHeader:

    def test_breadcrumbs_visible(self, page: Page):
        expect(page.locator(PL.LINK_HOME)).to_be_visible()
        expect(page.locator(PL.TEXT_BREADCRUMB)).to_be_visible()

    def test_main_headings_and_logos_visible(self, page: Page):
        expect(page.locator(PL.HEADING_MAIN)).to_be_visible()
        expect(page.locator(PL.IMG_OT_LOGO)).to_be_visible()
        expect(page.locator(PL.TEXT_OT_TITLE)).to_be_visible()

    def test_intro_paragraphs_visible(self, page: Page):
        expect(page.locator(PL.TEXT_CORP_WEBSITE)).to_be_visible()
        expect(page.locator(PL.TEXT_PGI_INTRO).first).to_be_visible()


# ── Collection Section ────────────────────────────────────────────────────────

class TestWhyWeCollectSection:

    def test_collection_intro_visible(self, page: Page):
        expect(page.locator(PL.HEADING_WHY_COLLECT)).to_be_visible()
        expect(page.locator(PL.TEXT_VISIT_CONTACT).first).to_be_visible()

    def test_collection_purpose_bullets_visible(self, page: Page):
        """Iterates through the specific collection purposes rather than checking repeating text."""
        for bullet in PL.BULLETS_COLLECT:
            expect(page.locator(bullet).first).to_be_visible()

    def test_public_authorities_clause_visible(self, page: Page):
        expect(page.locator(PL.TEXT_PROCESS_B).first).to_be_visible()
        expect(page.locator(PL.TEXT_PUBLIC_AUTH).first).to_be_visible()


# ── Disclosure Section ────────────────────────────────────────────────────────

class TestDisclosureSection:

    def test_disclosure_clauses_visible(self, page: Page):
        expect(page.locator(PL.HEADING_DISCLOSE)).to_be_visible()
        expect(page.locator(PL.TEXT_DISCLOSE_INTRO).first).to_be_visible()
        expect(page.locator(PL.TEXT_SHARE_MIGHT).first).to_be_visible()
        expect(page.locator(PL.TEXT_SERVICE_PROVS).first).to_be_visible()
        expect(page.locator(PL.TEXT_LAW_ENFORCE).first).to_be_visible()


# ── Protection Section ────────────────────────────────────────────────────────

class TestProtectionSection:

    def test_protection_and_retention_clauses_visible(self, page: Page):
        expect(page.locator(PL.HEADING_PROTECT)).to_be_visible()
        expect(page.locator(PL.TEXT_INTEGRITY).first).to_be_visible()
        expect(page.locator(PL.TEXT_SAFEGUARDS).first).to_be_visible()
        expect(page.locator(PL.TEXT_KEEP_PROTECT).first).to_be_visible()
        expect(page.locator(PL.TEXT_ONLY_NECESSARY).first).to_be_visible()
        expect(page.locator(PL.TEXT_RESTRICT).first).to_be_visible()
        expect(page.locator(PL.TEXT_NOTIFY).first).to_be_visible()
        expect(page.locator(PL.TEXT_UPDATE).first).to_be_visible()


# ── User Choices Section ──────────────────────────────────────────────────────

class TestUserChoicesSection:

    def test_choices_intro_visible(self, page: Page):
        expect(page.locator(PL.HEADING_CHOICES)).to_be_visible()
        expect(page.locator(PL.TEXT_AFFORDED).first).to_be_visible()

    def test_user_rights_bullets_visible(self, page: Page):
        """Verifies visibility of the specific data subject rights."""
        for bullet in PL.BULLETS_RIGHTS:
            expect(page.locator(bullet).first).to_be_visible()

    def test_exercise_rights_clauses_visible(self, page: Page):
        expect(page.locator(PL.TEXT_MOREOVER_RIGHT).first).to_be_visible()
        expect(page.locator(PL.TEXT_TO_THE_EXTENT).first).to_be_visible()
        expect(page.locator(PL.TEXT_EXERCISE).first).to_be_visible()
        expect(page.locator(PL.TEXT_COMPLAINT).first).to_be_visible()


# ── Footer / Contact ──────────────────────────────────────────────────────────

class TestPrivacyContactAndFooter:

    def test_contact_details_and_end_notice_visible(self, page: Page):
        expect(page.locator(PL.TEXT_COMPANY_NAME).first).to_be_visible()
        expect(page.locator(PL.TEXT_ADDRESS_1).first).to_be_visible()
        expect(page.locator(PL.TEXT_ADDRESS_2).first).to_be_visible()
        expect(page.locator(PL.LINK_PRIVACY_EMAIL)).to_be_visible()
        expect(page.locator(PL.TEXT_END_NOTICE)).to_be_visible()