import pytest
from playwright.sync_api import Page, expect
from locators.terms_conditions_locators import TermsConditionsLocators as TL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_terms_conditions(page: Page):
    page.goto(TL.TERMS_CONDITIONS_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Header ──────────────────────────────────────────────────────────────────────

class TestTermsConditionsHeader:

    def test_heading_visible(self, page: Page):
        expect(TL.heading_terms_conditions(page)).to_be_visible()

    def test_effective_date_visible(self, page: Page):
        expect(page.locator(TL.TEXT_EFFECTIVE_DATE)).to_be_visible()


# ── Covenant ──────────────────────────────────────────────────────────────────

class TestCovenant:

    def test_section_visible(self, page: Page):
        expect(TL.heading_covenant(page)).to_be_visible()
        expect(page.locator(TL.TEXT_WHEN_YOU_VISIT)).to_be_visible()
        expect(page.locator(TL.TEXT_FURTHER_BY_ACCESSING)).to_be_visible()
        expect(page.locator(TL.TEXT_IF_YOU_DO_NOT_AGREE)).to_be_visible()


# ── Amendments to the Terms and Conditions ───────────────────────────────────────

class TestAmendments:

    def test_section_visible(self, page: Page):
        expect(TL.heading_amendments(page)).to_be_visible()
        expect(page.locator(TL.TEXT_HNM_MAY_FROM_TIME)).to_be_visible()
        expect(page.locator(TL.TEXT_HNM_SHALL_INFORM)).to_be_visible()
        expect(page.locator(TL.TEXT_CHANGES_IN_TERMS)).to_be_visible()
        expect(page.locator(TL.TEXT_IF_YOU_CONTINUE)).to_be_visible()


# ── Definition of Terms ───────────────────────────────────────────────────────────

class TestDefinitionOfTerms:

    def test_section_visible(self, page: Page):
        expect(TL.heading_definition_of_terms(page)).to_be_visible()
        expect(page.locator(TL.TEXT_UNLESS_CONTEXT)).to_be_visible()
        expect(page.locator(TL.TEXT_INTERPRETATION)).to_be_visible()


# ── General Use of Services ───────────────────────────────────────────────────────

class TestGeneralUseOfServices:

    def test_section_heading_and_intro_visible(self, page: Page):
        expect(TL.heading_general_use_of_services(page)).to_be_visible()
        expect(page.locator(TL.TEXT_AGREE_TO_COMPLY)).to_be_visible()
        expect(page.locator(TL.TEXT_HNM_IS_SINGAPORE)).to_be_visible()
        expect(page.locator(TL.TEXT_MUST_BE_EIGHTEEN)).to_be_visible()
        expect(page.locator(TL.TEXT_AVAILABILITY)).to_be_visible()
        expect(page.locator(TL.TEXT_RIGHT_NOT_OBLIGATION)).to_be_visible()
        expect(page.locator(TL.TEXT_ADDITIONAL_TERMS)).to_be_visible()

    def test_account_creation_text_visible(self, page: Page):
        expect(page.get_by_text("Creating your account", exact=True)).to_be_visible()
        expect(page.locator(TL.TEXT_PASSWORD)).to_be_visible()
        expect(page.locator(TL.TEXT_INFORMATION_CREATING)).to_be_visible()
        expect(page.locator(TL.TEXT_SHARING_HNM)).to_be_visible()


# ── Use of Services ───────────────────────────────────────────────────────────────

class TestUseOfServices:

    def test_section_visible(self, page: Page):
        expect(TL.heading_use_of_services(page)).to_be_visible()
        expect(page.locator(TL.TEXT_RESTRICTIONS_USE)).to_be_visible()
        expect(page.locator(TL.TEXT_GENERAL_TC_HEADING)).to_be_visible()
        expect(page.locator(TL.TEXT_GENERAL_TC_BODY)).to_be_visible()
        expect(page.locator(TL.TEXT_PURPORTED_USE)).to_be_visible()
        expect(page.locator(TL.TEXT_AGREE_TO_BE_BOUND)).to_be_visible()


# ── Intellectual Property ───────────────────────────────────────────────────────

class TestIntellectualProperty:

    def test_section_visible(self, page: Page):
        expect(page.get_by_text("Intellectual Property", exact=True)).to_be_visible()
        expect(page.locator(TL.TEXT_OWNERSHIP)).to_be_visible()
        expect(page.locator(TL.TEXT_RESTRICTED_USE)).to_be_visible()
        expect(page.locator(TL.TEXT_TRADEMARKS_REGISTERED)).to_be_visible()


# ── Third-Party Links ─────────────────────────────────────────────────────────────

class TestThirdPartyLinks:

    def test_section_visible(self, page: Page):
        expect(page.get_by_text("Third-Party Links", exact=True)).to_be_visible()
        expect(page.locator(TL.TEXT_CERTAIN_CONTENT)).to_be_visible()
        expect(page.locator(TL.TEXT_WEBSITE_MAY_CONTAIN)).to_be_visible()
        expect(page.locator(TL.TEXT_MAY_LINK_TO_HOMEPAGE)).to_be_visible()
        expect(page.locator(TL.TEXT_MAY_USE_FEATURES)).to_be_visible()
        expect(page.locator(TL.TEXT_WEBSITE_FROM_WHICH)).to_be_visible()
        expect(page.locator(TL.TEXT_AGREE_TO_COOPERATE)).to_be_visible()
        expect(page.locator(TL.TEXT_WE_MAY_DISABLE)).to_be_visible()
        expect(page.locator(TL.TEXT_THIRD_PARTY_LINKS_BODY)).to_be_visible()
        expect(page.locator(TL.TEXT_HNM_NOT_LIABLE_INCONV)).to_be_visible()


# ── User Comments, Feedbacks, and Suggestions ───────────────────────────────────

class TestUserComments:

    def test_section_visible(self, page: Page):
        expect(TL.heading_user_comments(page)).to_be_visible()
        expect(page.locator(TL.TEXT_WE_APPRECIATE_HEARING)).to_be_visible()
        expect(page.locator(TL.TEXT_OWN_EXCLUSIVELY)).to_be_visible()
        expect(page.locator(TL.TEXT_NOT_BE_SUBJECT)).to_be_visible()
        expect(page.locator(TL.TEXT_ENTITLED_UNRESTRICTED)).to_be_visible()


# ── Cookies ────────────────────────────────────────────────────────────────────────

class TestCookies:

    def test_section_visible(self, page: Page):
        expect(TL.heading_cookies(page)).to_be_visible()
        expect(page.locator(TL.TEXT_PLATFORM_EMPLOYS_COOKIES)).to_be_visible()
        expect(page.locator(TL.TEXT_WE_MAY_USE_THIRD_PARTY)).to_be_visible()
        expect(page.locator(TL.TEXT_MAY_REFUSE_TO_ACCEPT)).to_be_visible()


# ── Representations and Warranties ───────────────────────────────────────────────

class TestRepresentationsAndWarranties:

    def test_section_visible(self, page: Page):
        expect(page.locator(TL.TEXT_REPS_AND_WARRANTIES_HEADING)).to_be_visible()
        expect(page.locator(TL.TEXT_WHILE_WE_AIM)).to_be_visible()
        expect(page.locator(TL.TEXT_ACCEPT_AND_UNDERSTAND)).to_be_visible()
        expect(page.locator(TL.TEXT_EXCEPT_AS_OTHERWISE)).to_be_visible()
        expect(page.locator(TL.TEXT_IN_NO_CASE_SHALL)).to_be_visible()


# ── Risk and Liability ───────────────────────────────────────────────────────────

class TestRiskAndLiability:

    def test_section_visible(self, page: Page):
        expect(TL.heading_risk_and_liability(page)).to_be_visible()
        expect(page.locator(TL.TEXT_RISK_OF_DAMAGE)).to_be_visible()
        expect(page.locator(TL.TEXT_LIABILITY_OF_HNM)).to_be_visible()
        expect(page.locator(TL.TEXT_NOT_LIABLE_LOSS_DELAY)).to_be_visible()
        expect(page.locator(TL.TEXT_CLAIMS_FOR_LOSS)).to_be_visible()


# ── Payment ────────────────────────────────────────────────────────────────────────

class TestPayment:

    def test_section_visible(self, page: Page):
        expect(TL.heading_payment(page)).to_be_visible()
        expect(page.locator(TL.TEXT_RESERVATION_POLICY)).to_be_visible()
        expect(page.locator(TL.TEXT_PAYMENT_METHODS)).to_be_visible()
        expect(page.locator(TL.TEXT_PAYMENT_PROCESSING)).to_be_visible()
        expect(page.locator(TL.TEXT_REFUND_POLICY)).to_be_visible()
        expect(page.locator(TL.TEXT_PAYMENT_METHODS_MAY_BE)).to_be_visible()
        expect(page.locator(TL.TEXT_YOU_AGREE_THAT)).to_be_visible()


# ── Notices ────────────────────────────────────────────────────────────────────────

class TestNotices:

    def test_section_visible(self, page: Page):
        expect(TL.heading_notices(page)).to_be_visible()
        expect(page.locator(TL.TEXT_NOTICES_FROM_US)).to_be_visible()
        expect(page.locator(TL.TEXT_GIVE_NOTICE_TO_US)).to_be_visible()


# ── Termination ───────────────────────────────────────────────────────────────────

class TestTermination:

    def test_section_visible(self, page: Page):
        expect(TL.heading_termination(page)).to_be_visible()
        expect(page.locator(TL.TEXT_YOU_MAY_TERMINATE)).to_be_visible()


# ── General Provisions ───────────────────────────────────────────────────────────

class TestGeneralProvisions:

    def test_section_visible(self, page: Page):
        expect(TL.heading_general_provisions(page)).to_be_visible()
        expect(page.locator(TL.TEXT_CUMULATIVE_RIGHTS)).to_be_visible()
        expect(page.locator(TL.TEXT_NO_WAIVER)).to_be_visible()
        expect(page.locator(TL.TEXT_SEVERABILITY)).to_be_visible()
        expect(page.locator(TL.TEXT_RIGHTS_OF_THIRD_PARTIES)).to_be_visible()
        expect(page.locator(TL.TEXT_GOVERNING_LAW)).to_be_visible()
        expect(page.locator(TL.TEXT_AMENDMENTS_BY_NOTICE)).to_be_visible()
        expect(page.locator(TL.TEXT_CORRECTION_OF_ERRORS)).to_be_visible()
        expect(page.locator(TL.TEXT_CURRENCY)).to_be_visible()
        expect(page.locator(TL.TEXT_ENTIRE_AGREEMENT)).to_be_visible()
        expect(page.locator(TL.TEXT_BINDING_AND_CONCLUSIVE)).to_be_visible()
        expect(page.locator(TL.TEXT_ASSIGNMENT)).to_be_visible()
        expect(page.locator(TL.TEXT_FORCE_MAJEURE)).to_be_visible()


# ── How to reach Hayop Ni Manam ───────────────────────────────────────────────────

class TestHowToReach:

    def test_contact_section_visible(self, page: Page):
        expect(TL.heading_how_to_reach(page)).to_be_visible()
        expect(page.locator(TL.TEXT_SHOULD_YOU_HAVE_Q)).to_be_visible()
        expect(page.locator(TL.LINK_EMAIL_AMOY_STREET)).to_be_visible()
        expect(page.locator(TL.LINK_EMAIL_MOMENT_GROUP)).to_be_visible()
        expect(page.locator(TL.TEXT_CONTACT_NO)).to_be_visible()
        expect(TL.paragraph_email_amoy_street(page)).to_be_visible()
        expect(page.locator(TL.IMG_KALACHUHI)).to_be_visible()
    def test_email_links_clickable(self, page: Page):
        """Both contact email links (amoy.street and momentgroup) should be clickable."""
        page.locator(TL.LINK_EMAIL_AMOY_STREET).click()
        page.locator(TL.LINK_EMAIL_MOMENT_GROUP).click()