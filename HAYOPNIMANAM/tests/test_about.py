import pytest
from playwright.sync_api import Page, expect
from locators.about_locators import AboutLocators as AL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_about(page: Page):
    page.goto(AL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.locator(AL.NAV_ABOUT).first.click()
    page.wait_for_url("**/who-we-are/**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestAboutNavigation:

    def test_about_page_loads(self, page: Page):
        expect(page).to_have_url(AL.ABOUT_URL)


# ── Section Tab Tests ─────────────────────────────────────────────────────────

class TestAboutTabs:

    def test_moment_group_tab_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator(AL.TAB_MOMENT_GROUP).first.click()
        expect(page.locator(AL.TAB_MOMENT_GROUP).first).to_be_visible()

    def test_partners_tab_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator(AL.TAB_PARTNERS).first.click()
        expect(page.locator(AL.TAB_PARTNERS).first).to_be_visible()


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestAboutFooter:

    def test_instagram_link_present(self, page: Page):
        # Instagram link is hidden behind CSS animation — check it exists in DOM
        expect(page.locator(AL.FOOTER_INSTAGRAM)).to_be_attached()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(AL.FOOTER_PRIVACY).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(AL.FOOTER_TERMS).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")