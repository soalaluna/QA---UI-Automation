import pytest
from playwright.sync_api import Page, expect
from locators.consumer_svn_locators import PldtSvnLocators as PL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_svn(page: Page):
    page.goto(PL.SVN_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Page Load ──────────────────────────────────────────────────────────────────

class TestSvnPageLoad:

    def test_consumer_nav_link_visible(self, page: Page):
        expect(page.get_by_role("link", name="Consumer", exact=True)).to_be_visible()

    def test_breadcrumb_span_visible(self, page: Page):
        expect(PL.span_smart_virtual_number(page)).to_be_visible()

    def test_heading_visible(self, page: Page):
        expect(PL.heading_svn(page)).to_be_visible()

    def test_description_text_visible(self, page: Page):
        expect(page.locator(PL.TEXT_SVN_DESCRIPTION)).to_be_visible()

    def test_learn_more_link_visible(self, page: Page):
        expect(page.locator(PL.LINK_LEARN_MORE)).to_be_visible()

    def test_section_image_visible(self, page: Page):
        expect(PL.section_breadcrumb_img(page)).to_be_visible()


# ── Learn More Popup ───────────────────────────────────────────────────────────

class TestLearnMorePopup:

    def test_learn_more_opens_popup(self, page: Page):
        """Clicking Learn More should open a new tab."""
        with page.expect_popup() as popup_info:
            page.locator(PL.LINK_LEARN_MORE).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert popup.url != ""
        popup.close()