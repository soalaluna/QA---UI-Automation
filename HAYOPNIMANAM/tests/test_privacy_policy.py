import pytest
from playwright.sync_api import Page, expect
from locators.privacy_policy_locators import PrivacyPolicyLocators as PL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_privacy_policy(page: Page):
    page.goto(PL.PRIVACY_POLICY_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Header Tests ──────────────────────────────────────────────────────────────

class TestPrivacyPolicyHeader:

    def test_heading_visible(self, page: Page):
        expect(page.locator(PL.HEADING_PRIVACY_POLICY)).to_be_visible()

    def test_effective_date_visible(self, page: Page):
        expect(page.locator(PL.TEXT_EFFECTIVE_DATE)).to_be_visible()

    def test_intro_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_INTRO_PROTECTING)).to_be_visible()
        expect(page.locator(PL.TEXT_INTRO_WE_ARE)).to_be_visible()


# ── Definitions Tests ──────────────────────────────────────────────────────────

class TestDefinitionOfMaterialTerms:

    def test_definitions_heading_visible(self, page: Page):
        expect(page.locator(PL.HEADING_DEFINITIONS)).to_be_visible()

    @pytest.mark.parametrize("locator_attr", [
        "DEF_ACCOUNT", "DEF_CLIENT", "DEF_COOKIES", "DEF_DATA_SUBJECT",
        "DEF_LOG_FILES", "DEF_MOBILE_APP", "DEF_PERSONAL_INFORMATION",
        "DEF_PI_CONTROLLER", "DEF_PI_PROCESSOR", "DEF_SENSITIVE_PI",
        "DEF_SENSITIVE_RACE", "DEF_SENSITIVE_HEALTH", "DEF_SENSITIVE_GOV_ISSUED",
        "DEF_SENSITIVE_EXEC_ORDER", "DEF_USER", "DEF_VISITOR", "DEF_WEBSITE",
    ])
    def test_definition_visible(self, page: Page, locator_attr: str):
        expect(page.locator(getattr(PL, locator_attr))).to_be_visible()


# ── About Hayop Ni Manam ───────────────────────────────────────────────────────

class TestAboutHayopNiManam:

    def test_about_heading_visible(self, page: Page):
        expect(page.locator(PL.HEADING_ABOUT)).to_be_visible()

    def test_about_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_ABOUT_SG).first).to_be_visible()


# ── How Hayop Ni Manam Collects Information ────────────────────────────────────

class TestHowInformationIsCollected:

    def test_section_heading_visible(self, page: Page):
        expect(page.locator(PL.HEADING_HOW_COLLECTS)).to_be_visible()

    def test_intro_paragraphs_visible(self, page: Page):
        expect(page.locator(PL.TEXT_WHENEVER_USERS)).to_be_visible()
        expect(page.get_by_role("paragraph").filter(has_text="As a User")).to_be_visible()
        expect(page.locator(PL.TEXT_IF_YOU_ARE_USER)).to_be_visible()

    def test_user_data_fields_first_set_visible(self, page: Page):
        expect(page.locator(PL.LIST_NAME).first).to_be_visible()
        expect(page.locator(PL.LIST_GENDER).first).to_be_visible()
        expect(page.locator(PL.LIST_EMAIL).first).to_be_visible()
        expect(page.locator(PL.LIST_MOBILE_NUMBER).first).to_be_visible()
        expect(page.locator(PL.LIST_CIVIL_STATUS)).to_be_visible()
        expect(page.locator(PL.LIST_DOB).first).to_be_visible()
        expect(page.locator(PL.LIST_ADDRESS_CURRENT)).to_be_visible()
        expect(page.locator(PL.LIST_PAYMENT_INFO).first).to_be_visible()
        expect(page.locator(PL.LIST_ID_IMAGE).first).to_be_visible()
        expect(page.get_by_text("Personal photo for verification.", exact=True)).to_be_visible()
        expect(page.get_by_text("Required Fields", exact=True)).to_be_visible()

    def test_registration_and_app_download_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_WHEN_YOU_REGISTER)).to_be_visible()
        expect(page.locator(PL.TEXT_FROM_USERS_CLIENT)).to_be_visible()
        expect(page.locator(PL.TEXT_BY_DOWNLOADING_APP)).to_be_visible()

    def test_user_data_fields_second_set_visible(self, page: Page):
        expect(page.locator(PL.LIST_NAME).nth(1)).to_be_visible()
        expect(page.locator(PL.LIST_GENDER).nth(1)).to_be_visible()
        expect(page.locator(PL.LIST_EMAIL).nth(1)).to_be_visible()
        expect(page.locator(PL.LIST_MOBILE_NUMBER).nth(1)).to_be_visible()
        expect(page.locator(PL.LIST_DOB).nth(1)).to_be_visible()
        expect(page.locator(PL.LIST_ADDRESS_CURRENT_LOC2)).to_be_visible()
        expect(page.locator(PL.LIST_PAYMENT_INFO).nth(1)).to_be_visible()
        expect(page.locator(PL.LIST_ID_IMAGE).nth(1)).to_be_visible()
        expect(page.get_by_text("Personal photo for Verification.", exact=True)).to_be_visible()

    def test_services_text_visible(self, page: Page):
        expect(page.get_by_text("Hayop Ni Manam’s Services", exact=True)).to_be_visible()
        expect(page.locator(PL.TEXT_ABOUT_SG).nth(1)).to_be_visible()


# ── Use and Utilization of Information ─────────────────────────────────────────

class TestUseAndUtilization:

    def test_section_heading_visible(self, page: Page):
        expect(page.locator(PL.HEADING_USE_UTILIZATION)).to_be_visible()

    def test_purposes_list_visible(self, page: Page):
        expect(page.locator(PL.TEXT_ONLY_USES)).to_be_visible()
        expect(page.locator(PL.LIST_PROVIDE_USERS)).to_be_visible()
        expect(page.locator(PL.LIST_PROVIDE_INFO)).to_be_visible()
        expect(page.locator(PL.LIST_FACILITATE_IMPROVE)).to_be_visible()
        expect(page.locator(PL.LIST_MARKETING)).to_be_visible()
        expect(page.locator(PL.LIST_COMMUNICATIONS)).to_be_visible()

    def test_information_categories_visible(self, page: Page):
        expect(page.locator(PL.TEXT_WE_USE_INFO_FOR)).to_be_visible()
        expect(page.locator(PL.TEXT_WHEN_YOU_SHARE)).to_be_visible()
        expect(page.locator(PL.LIST_LOCATION_INFO)).to_be_visible()
        expect(page.locator(PL.LIST_TRANSACTION_INFO)).to_be_visible()
        expect(page.locator(PL.LIST_USAGE_PREFERENCE)).to_be_visible()
        expect(page.locator(PL.LIST_DEVICE_INFO)).to_be_visible()
        expect(page.locator(PL.LIST_LOG_INFO)).to_be_visible()
        expect(page.locator(PL.LIST_COOKIES_TRACKING)).to_be_visible()
        expect(page.locator(PL.TEXT_THIRD_PARTY)).to_be_visible()
        expect(page.locator(PL.TEXT_TRANSFER_STORE)).to_be_visible()


# ── Information Sharing ─────────────────────────────────────────────────────────

class TestInformationSharing:

    def test_section_heading_visible(self, page: Page):
        expect(page.locator(PL.HEADING_INFO_SHARING)).to_be_visible()

    def test_disclosure_intro_visible(self, page: Page):
        expect(page.locator(PL.TEXT_MAY_DISCLOSE_MARKET)).to_be_visible()
        expect(page.locator(PL.TEXT_IN_ADDITION_DISCLOSE)).to_be_visible()
        expect(page.locator(PL.TEXT_THROUGH_OUR_SERVICES)).to_be_visible()
        expect(page.get_by_text("We may share your information:", exact=True)).to_be_visible()

    def test_sharing_parties_list_visible(self, page: Page):
        expect(page.locator(PL.LIST_CLIENTS_DESIGNERS)).to_be_visible()
        expect(page.locator(PL.LIST_AFFILIATES)).to_be_visible()
        expect(page.locator(PL.LIST_ADVERTISERS)).to_be_visible()
        expect(page.locator(PL.LIST_THIRD_PARTY_PROVIDERS)).to_be_visible()
        expect(page.locator(PL.LIST_HNM_STAFF)).to_be_visible()
        expect(page.locator(PL.LIST_ORGS_GROUPS)).to_be_visible()
        expect(page.locator(PL.LIST_STUDYING_PURPOSE)).to_be_visible()
        expect(page.locator(PL.LIST_CONTRACTORS)).to_be_visible()
        expect(page.locator(PL.LIST_BUYER_SUCCESSOR)).to_be_visible()

    def test_other_important_sharing_visible(self, page: Page):
        expect(page.get_by_role("paragraph").filter(has_text="Other Important Sharing we")).to_be_visible()
        expect(page.locator(PL.TEXT_SUBSIDIARIES_AFFILIATED)).to_be_visible()
        expect(page.locator(PL.TEXT_VENDORS_CONSULTANTS)).to_be_visible()
        expect(page.locator(PL.TEXT_IN_RESPONSE_REQUEST)).to_be_visible()
        expect(page.locator(PL.TEXT_LAW_ENFORCEMENT)).to_be_visible()
        expect(page.locator(PL.TEXT_IN_CONNECTION_WITH)).to_be_visible()
        expect(page.locator(PL.TEXT_IF_WE_OTHERWISE)).to_be_visible()
        expect(page.locator(PL.TEXT_AGGREGATED)).to_be_visible()

    def test_social_sharing_features_visible(self, page: Page):
        expect(page.get_by_text("Social Sharing Features", exact=True)).to_be_visible()
        expect(page.locator(PL.TEXT_WE_MAY_INTEGRATE)).to_be_visible()


# ── Cookies and other Tracking Technologies ────────────────────────────────────

class TestCookiesAndTracking:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.HEADING_COOKIES_TRACKING)).to_be_visible()
        expect(page.locator(PL.TEXT_SOME_WEB_PAGES)).to_be_visible()
        expect(page.locator(PL.TEXT_TRACKING_TECH_MAY)).to_be_visible()


# ── Storage and Security ────────────────────────────────────────────────────────

class TestStorageAndSecurity:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.HEADING_STORAGE_SECURITY)).to_be_visible()
        expect(page.locator(PL.TEXT_ALL_INFO_GATHERED)).to_be_visible()


# ── Retention Period ─────────────────────────────────────────────────────────────

class TestRetentionPeriod:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.HEADING_RETENTION)).to_be_visible()
        expect(page.locator(PL.TEXT_SHALL_NOT_STORE)).to_be_visible()
        expect(page.locator(PL.TEXT_SHALL_ONLY)).to_be_visible()


# ── Updating Personal Information ────────────────────────────────────────────────

class TestUpdatingPersonalInformation:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.HEADING_UPDATING_INFO)).to_be_visible()
        expect(page.locator(PL.TEXT_USERS_MAY_UPDATE)).to_be_visible()
        expect(page.locator(PL.TEXT_USERS_MAY_ALSO_ASK)).to_be_visible()


# ── Your Rights Under the Data Privacy Act ───────────────────────────────────────

class TestYourRights:

    def test_section_heading_and_intro_visible(self, page: Page):
        expect(page.locator(PL.HEADING_YOUR_RIGHTS)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_RESPECTS)).to_be_visible()
        expect(page.locator(PL.TEXT_AS_DATA_SUBJECT)).to_be_visible()

    def test_rights_list_visible(self, page: Page):
        expect(page.get_by_text("The right to be informed", exact=True)).to_be_visible()
        expect(page.get_by_text("The right to object", exact=True)).to_be_visible()
        expect(page.get_by_text("The right to access", exact=True)).to_be_visible()
        expect(page.locator(PL.RIGHT_TO_RECTIFICATION)).to_be_visible()
        expect(page.locator(PL.RIGHT_TO_ERASURE)).to_be_visible()
        expect(page.locator(PL.RIGHT_TO_DAMAGES)).to_be_visible()
        expect(page.locator(PL.RIGHT_TO_PORTABILITY)).to_be_visible()

    def test_right_to_be_informed_section_visible(self, page: Page):
        expect(page.get_by_role("paragraph").filter(has_text="A. Right to be Informed")).to_be_visible()
        expect(page.locator(PL.TEXT_HAVE_RIGHT_INFORMED)).to_be_visible()
        expect(page.locator(PL.TEXT_AS_DATA_SUBJECT_SHALL)).to_be_visible()
        expect(page.locator(PL.LIST_DESC_PERSONAL)).to_be_visible()
        expect(page.locator(PL.LIST_PURPOSES)).to_be_visible()
        expect(page.locator(PL.LIST_BASIS_PROCESSING)).to_be_visible()
        expect(page.locator(PL.LIST_SCOPE_METHOD)).to_be_visible()
        expect(page.locator(PL.LIST_RECIPIENTS)).to_be_visible()
        expect(page.locator(PL.LIST_METHODS_UTILIZED)).to_be_visible()
        expect(page.locator(PL.LIST_IDENTITY_CONTACT)).to_be_visible()
        expect(page.locator(PL.LIST_PERIOD_FOR_WHICH)).to_be_visible()
        expect(page.locator(PL.LIST_EXISTENCE_OF_RIGHTS)).to_be_visible()

    def test_right_to_object_section_visible(self, page: Page):
        expect(page.get_by_role("paragraph").filter(has_text="B. Right to Object")).to_be_visible()
        expect(page.locator(PL.TEXT_HAVE_RIGHT_OBJECT)).to_be_visible()
        expect(page.locator(PL.TEXT_ALSO_HAVE_RIGHT)).to_be_visible()
        expect(page.locator(PL.GENERIC_SECTION)).to_be_visible()
        expect(page.locator(PL.TEXT_SHOULD_YOU_WITHHOLD)).to_be_visible()
        expect(page.locator(PL.TEXT_PERSONAL_DATA_NEEDED_1)).to_be_visible()
        expect(page.locator(PL.TEXT_PROCESSING_OBVIOUS)).to_be_visible()
        expect(page.locator(PL.TEXT_PERSONAL_DATA_LEGAL)).to_be_visible()

    def test_right_to_access_section_visible(self, page: Page):
        expect(page.get_by_role("paragraph").filter(has_text="C. Right to Access")).to_be_visible()
        expect(page.locator(PL.TEXT_REASONABLE_ACCESS)).to_be_visible()
        expect(page.locator(PL.LIST_CONTENTS_PERSONAL)).to_be_visible()
        expect(page.locator(PL.LIST_SOURCES_PERSONAL)).to_be_visible()
        expect(page.locator(PL.LIST_NAMES_ADDRESSES)).to_be_visible()
        expect(page.locator(PL.LIST_MANNER_BY_WHICH)).to_be_visible()
        expect(page.locator(PL.LIST_REASONS_DISCLOSURE)).to_be_visible()
        expect(page.locator(PL.LIST_AUTOMATED_INFO)).to_be_visible()
        expect(page.locator(PL.LIST_DATE_PERSONAL_DATA)).to_be_visible()
        expect(page.locator(PL.LIST_DESIGNATION_NAME)).to_be_visible()

    def test_right_to_rectification_visible(self, page: Page):
        expect(page.get_by_text("Right to Rectification", exact=True)).to_be_visible()
        expect(page.locator(PL.TEXT_HAVE_RIGHT_DISPUTE)).to_be_visible()

    def test_right_to_erasure_visible(self, page: Page):
        expect(page.get_by_text("Right to Erasure or Blocking", exact=True)).to_be_visible()
        expect(page.locator(PL.TEXT_HAVE_RIGHT_SUSPEND)).to_be_visible()
        expect(page.locator(PL.TEXT_RIGHT_MAY_BE_EXERCISED)).to_be_visible()
        expect(page.locator(PL.TEXT_DPO_MAY_NOTIFY)).to_be_visible()

    def test_right_to_damages_visible(self, page: Page):
        expect(page.locator(PL.HEADING_F_RIGHT_DAMAGES)).to_be_visible()
        expect(page.locator(PL.TEXT_INDEMNIFIED)).to_be_visible()

    def test_right_to_data_portability_visible(self, page: Page):
        expect(page.locator(PL.HEADING_G_RIGHT_PORTABILITY)).to_be_visible()
        expect(page.locator(PL.TEXT_WHERE_PI_PROCESSED)).to_be_visible()


# ── Participation of Data Subjects ───────────────────────────────────────────────

class TestParticipationOfDataSubjects:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.TEXT_PARTICIPATION_HEADING)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_ENCOURAGES)).to_be_visible()
        expect(page.locator(PL.TEXT_USERS_SHIPPERS_FREELY)).to_be_visible()
        expect(page.locator(PL.TEXT_IF_YOU_DO_NOT_AGREE_1)).to_be_visible()


# ── External Links ───────────────────────────────────────────────────────────────

class TestExternalLinks:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.TEXT_EXTERNAL_LINKS_HEADING)).to_be_visible()
        expect(page.locator(PL.TEXT_INSTANCES_WHERE)).to_be_visible()
        expect(page.locator(PL.TEXT_HYPERLINKS_MAY_LEAD)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_ENDEAVORS)).to_be_visible()
        expect(page.locator(PL.TEXT_UNLESS_CLEARLY_STATED)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_DOES_NOT_ALSO)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_IS_NOT)).to_be_visible()
        expect(page.locator(PL.TEXT_SHOULD_YOU_CLICK)).to_be_visible()
        expect(page.locator(PL.TEXT_ANY_INFO_WHICH_YOU_MAY)).to_be_visible()


# ── Effectivity ────────────────────────────────────────────────────────────────

class TestEffectivity:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.TEXT_EFFECTIVITY_HEADING)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_PRIVACY)).to_be_visible()


# ── Acceptance of this Data Privacy Notice ───────────────────────────────────────

class TestAcceptance:

    def test_section_visible(self, page: Page):
        expect(page.locator(PL.HEADING_ACCEPTANCE)).to_be_visible()
        expect(page.locator(PL.TEXT_APPLIES_TO_ALL_PI)).to_be_visible()
        expect(page.locator(PL.TEXT_BY_ACCESSING_WEBSITE)).to_be_visible()
        expect(page.locator(PL.TEXT_ALSO_AGREE_BY_USING)).to_be_visible()
        expect(page.locator(PL.TEXT_IF_YOU_DO_NOT_AGREE_2)).to_be_visible()
        expect(page.locator(PL.TEXT_HNM_RESERVES_RIGHT)).to_be_visible()


# ── Contact Information ──────────────────────────────────────────────────────────

class TestContactInformation:

    def test_contact_section_visible(self, page: Page):
        expect(page.get_by_text("Contact Information", exact=True)).to_be_visible()
        expect(page.locator(PL.TEXT_SHOULD_YOU_HAVE_Q)).to_be_visible()
        expect(page.locator(PL.LINK_EMAIL_AMOY_STREET)).to_be_visible()
        expect(page.locator(PL.TEXT_EMAIL_AMOY_STREET)).to_be_visible()
        expect(page.locator(PL.TEXT_CONTACT_NO)).to_be_visible()
        expect(page.locator(PL.IMG_KALACHUHI)).to_be_visible()

    def test_email_links_clickable(self, page: Page):
        """Both contact email links (amoy.street and momentgroup) should be clickable."""
        page.locator(PL.LINK_EMAIL_AMOY_STREET).click()
        page.locator(PL.LINK_EMAIL_MOMENT_GROUP).click()