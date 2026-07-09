import pytest
from playwright.sync_api import Page, expect
from locators.cookie_policy_locators import CookiePolicyLocators as PL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_cookie_policy(page: Page):
    page.goto(PL.COOKIE_POLICY_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Breadcrumb & Header ────────────────────────────────────────────────────────

class TestCookiePolicyHeader:

    def test_breadcrumb_home_link_visible(self, page: Page):
        expect(PL.breadcrumb_home_link(page)).to_be_visible()

    def test_breadcrumb_cookie_policy_text_visible(self, page: Page):
        expect(PL.breadcrumb_cookie_policy_text(page)).to_be_visible()

    def test_heading_visible(self, page: Page):
        expect(PL.heading_cookie_policy(page)).to_be_visible()

    def test_cookie_policy_title_visible(self, page: Page):
        expect(page.get_by_text("COOKIE POLICY", exact=True)).to_be_visible()

    def test_corporate_section_visible(self, page: Page):
        expect(page.locator(PL.TEXT_CORPORATE_SECTION)).to_be_visible()

    def test_pgi_intro_visible(self, page: Page):
        expect(page.locator(PL.TEXT_PGI_IS)).to_be_visible()


# ── Cookie Type Descriptions ───────────────────────────────────────────────────

class TestCookieTypeDescriptions:

    def test_what_are_cookies_visible(self, page: Page):
        expect(page.locator(PL.TEXT_WHAT_ARE_COOKIES)).to_be_visible()
        expect(page.locator(PL.TEXT_COOKIE_DEFINITION)).to_be_visible()

    def test_how_pldt_uses_cookies_visible(self, page: Page):
        expect(page.locator(PL.TEXT_HOW_PLDT_USES)).to_be_visible()
        expect(page.locator(PL.TEXT_FOLLOWING_SUMMARY)).to_be_visible()

    def test_strictly_necessary_description_visible(self, page: Page):
        expect(PL.underline_strictly_necessary(page)).to_be_visible()
        expect(page.locator(PL.TEXT_STRICTLY_NECESSARY_DESC)).to_be_visible()

    def test_functional_description_visible(self, page: Page):
        expect(PL.underline_functional(page)).to_be_visible()
        expect(page.locator(PL.TEXT_FUNCTIONAL_DESC)).to_be_visible()

    def test_performance_description_visible(self, page: Page):
        expect(PL.underline_performance(page)).to_be_visible()
        expect(page.locator(PL.TEXT_PERFORMANCE_DESC)).to_be_visible()

    def test_targeting_description_visible(self, page: Page):
        expect(PL.underline_targeting(page)).to_be_visible()
        expect(page.locator(PL.TEXT_TARGETING_DESC)).to_be_visible()


# ── Browser Options Section ────────────────────────────────────────────────────

class TestBrowserOptionsSection:

    def test_options_intro_visible(self, page: Page):
        expect(page.locator(PL.TEXT_WHAT_ARE_OPTIONS)).to_be_visible()
        expect(page.locator(PL.TEXT_YOU_HAVE_OPTIONS)).to_be_visible()
        expect(page.locator(PL.TEXT_TO_CHANGE_BROWSER)).to_be_visible()

    def test_browser_links_visible(self, page: Page):
        expect(page.locator(PL.TEXT_GOOGLE_CHROME_INTRO)).to_be_visible()
        expect(page.locator(PL.LINK_CHROME_SETTINGS)).to_be_visible()
        expect(page.locator(PL.TEXT_IE)).to_be_visible()
        expect(page.locator(PL.LINK_IE_SETTINGS)).to_be_visible()
        expect(page.locator(PL.TEXT_SAFARI)).to_be_visible()
        expect(page.locator(PL.LINK_SAFARI_SETTINGS)).to_be_visible()
        expect(page.locator(PL.TEXT_FIREFOX)).to_be_visible()
        expect(page.locator(PL.LINK_FIREFOX_SETTINGS)).to_be_visible()

    def test_chrome_link_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_CHROME_SETTINGS).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "google.com" in popup.url or "support" in popup.url
        popup.close()

    def test_ie_link_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_IE_SETTINGS).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "microsoft.com" in popup.url
        popup.close()

    def test_safari_link_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_SAFARI_SETTINGS).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "apple.com" in popup.url
        popup.close()

    def test_firefox_link_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_FIREFOX_SETTINGS).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "mozilla.org" in popup.url
        popup.close()


# ── Cookie List: Strictly Necessary ───────────────────────────────────────────

class TestStrictlyNecessaryTable:

    def test_section_heading_and_desc_visible(self, page: Page):
        expect(PL.heading_cookie_list(page)).to_be_visible()
        expect(page.locator(PL.TEXT_COOKIE_LIST_INTRO)).to_be_visible()
        expect(PL.heading_strictly_necessary_table(page)).to_be_visible()
        expect(PL.strictly_necessary_desc(page)).to_be_visible()

    def test_table_headers_visible(self, page: Page):
        expect(page.locator(PL.COL_COOKIE_SUBGROUP_0).first).to_be_visible()
        expect(page.locator(PL.COL_COOKIES_0).first).to_be_visible()
        expect(page.locator(PL.COL_COOKIES_USED_0).first).to_be_visible()

    def test_table_content_visible(self, page: Page):
        expect(page.locator(PL.CELL_PLDTGLOBAL_COM)).to_be_visible()
        expect(page.locator(PL.LINK_OPTANON_CONSENT)).to_be_visible()
        expect(page.locator(PL.LINK_OPTANON_ALERT_CLOSED)).to_be_visible()
        expect(page.locator(PL.CELL_FIRST_PARTY_0).first).to_be_visible()

    def test_optanon_consent_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_OPTANON_CONSENT).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_optanon_alert_closed_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_OPTANON_ALERT_CLOSED).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()


# ── Cookie List: Functional ────────────────────────────────────────────────────

class TestFunctionalCookiesTable:

    def test_section_heading_and_desc_visible(self, page: Page):
        expect(PL.heading_functional_table(page)).to_be_visible()
        expect(PL.functional_desc(page)).to_be_visible()

    def test_table_content_visible(self, page: Page):
        expect(page.locator(PL.LINK_CLARITY_MS_EXACT)).to_be_visible()
        expect(page.locator(PL.LINK_C_CLARITY_MS)).to_be_visible()
        expect(page.locator(PL.LINK_WWW_CLARITY_MS)).to_be_visible()
        expect(PL.functional_c_bing_label(page)).to_be_visible()
        expect(page.get_by_role("columnheader", name="Cookies").nth(2)).to_be_visible()
        expect(page.locator(PL.CELL_MUID_0).first).to_be_visible()
        expect(page.locator(PL.CELL_MR_SM_ANONCHK)).to_be_visible()
        expect(page.locator(PL.CELL_CLID)).to_be_visible()
        expect(page.locator(PL.CELL_SRM_B)).to_be_visible()
        expect(page.get_by_role("columnheader", name="Cookies used").nth(1)).to_be_visible()
        expect(page.locator(PL.CELL_THIRD_PARTY_0).first).to_be_visible()
        expect(page.locator(PL.CELL_THIRD_PARTY_0).nth(1)).to_be_visible()
        expect(page.locator(PL.CELL_THIRD_PARTY_0).nth(2)).to_be_visible()
        expect(page.locator(PL.CELL_THIRD_PARTY_0).nth(3)).to_be_visible()

    def test_clarity_ms_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_CLARITY_MS_EXACT).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "clarity" in popup.url
        popup.close()

    def test_c_clarity_ms_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_C_CLARITY_MS).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_www_clarity_ms_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_WWW_CLARITY_MS).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_functional_c_bing_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            PL.functional_c_bing_label(page).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "bing" in popup.url or popup.url != ""
        popup.close()


# ── Cookie List: Performance ───────────────────────────────────────────────────

class TestPerformanceCookiesTable:

    def test_section_heading_and_desc_visible(self, page: Page):
        expect(PL.heading_performance_table(page)).to_be_visible()
        expect(PL.performance_desc(page)).to_be_visible()

    def test_table_content_visible(self, page: Page):
        expect(page.get_by_role("columnheader", name="Cookie Subgroup").nth(2)).to_be_visible()
        expect(page.locator(PL.CELL_PLDTGLOBAL_COM_EXACT)).to_be_visible()
        expect(PL.performance_c_bing_label(page)).to_be_visible()
        expect(page.get_by_role("columnheader", name="Cookies").nth(4)).to_be_visible()
        expect(page.locator(PL.LINK_GA_XXXXXXXXXX)).to_be_visible()
        expect(page.get_by_text("MR", exact=True)).to_be_visible()
        expect(page.get_by_role("columnheader", name="Cookies used").nth(2)).to_be_visible()
        expect(page.locator(PL.CELL_FIRST_PARTY_1).nth(1)).to_be_visible()
        expect(page.locator(PL.CELL_THIRD_PARTY_0).nth(4)).to_be_visible()

    def test_ga_xxxxxxxxxx_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_GA_XXXXXXXXXX).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_ga_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_GA).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_clsk_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_CLSK).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_clck_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_CLCK).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()

    def test_performance_c_bing_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            PL.performance_c_bing_label(page).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()


# ── Cookie List: Targeting ─────────────────────────────────────────────────────

class TestTargetingCookiesTable:

    def test_section_heading_and_desc_visible(self, page: Page):
        expect(PL.heading_targeting_table(page)).to_be_visible()
        expect(PL.targeting_desc(page)).to_be_visible()

    def test_table_content_visible(self, page: Page):
        expect(page.get_by_role("columnheader", name="Cookie Subgroup").nth(3)).to_be_visible()
        expect(page.locator(PL.LINK_BING_COM_EXACT)).to_be_visible()
        expect(page.get_by_role("columnheader", name="Cookies", exact=True).nth(3)).to_be_visible()
        expect(page.locator(PL.CELL_MUID_1).nth(1)).to_be_visible()
        expect(page.get_by_role("columnheader", name="Cookies used").nth(3)).to_be_visible()
        expect(page.locator(PL.CELL_THIRD_PARTY_0).nth(5)).to_be_visible()

    def test_bing_com_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_BING_COM_EXACT).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "bing.com" in popup.url or popup.url != ""
        popup.close()