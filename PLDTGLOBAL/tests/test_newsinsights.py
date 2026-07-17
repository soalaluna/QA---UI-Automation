import re
import pytest
from playwright.sync_api import Page, expect
from locators.newsinsights_locators import NewsInsightsLocators as NI


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_news_page(page: Page):
    page.goto(NI.URL, wait_until="domcontentloaded", timeout=60000)
    
    # Smoothly dismiss the cookie banner if it renders so it doesn't intercept clicks
    try:
        page.locator("role=button[name='Accept All Cookies']").click(timeout=3000)
    except Exception:
        pass 
        
    yield


# ── Hero & Filters ────────────────────────────────────────────────────────────

class TestNewsHeroAndFilters:

    def test_hero_section_visible(self, page: Page):
        expect(page.locator(NI.HEADING_SUB)).to_be_visible()
        expect(page.locator(NI.HEADING_MAIN)).to_be_visible()
        expect(page.locator(NI.TEXT_HERO_DESC)).to_be_visible()
        expect(page.locator(NI.IMG_HERO)).to_be_visible()

    def test_grid_filters_clickable(self, page: Page):
        expect(page.locator(NI.HEADING_GRID)).to_be_visible()
        
        # Verify and click through the category tabs
        expect(page.locator(NI.TAB_NEWS)).to_be_visible()
        page.locator(NI.TAB_NEWS).click()
        
        expect(page.locator(NI.TAB_EVENTS)).to_be_visible()
        page.locator(NI.TAB_EVENTS).click()
        
        expect(page.locator(NI.TAB_ALL)).to_be_visible()
        page.locator(NI.TAB_ALL).click()


# ── Article Cards & Sharing ───────────────────────────────────────────────────

class TestArticleInteractions:

    def test_article_card_elements_visible(self, page: Page):
        expect(page.locator(NI.LINK_ARTICLE)).to_be_visible()
        expect(page.locator(NI.BTN_READ_MORE)).to_be_visible()
        expect(page.locator(NI.TEXT_SHARE_TO)).to_be_visible()
        expect(page.locator(NI.BTN_SHARE_FB)).to_be_visible()
        expect(page.locator(NI.BTN_SHARE_LI)).to_be_visible()

    def test_read_more_navigates(self, page: Page):
        page.locator(NI.BTN_READ_MORE).click()
        
        # Playwright will automatically wait and retry until the URL changes
        expect(page).not_to_have_url(NI.URL)

    def test_share_on_facebook_popup(self, page: Page):
        """
        Uses no_wait_after=True + URL-pattern check instead of
        popup.wait_for_load_state(). The click itself was hanging on
        "waiting for scheduled navigations to finish" — something about
        this site's click handling keeps Playwright waiting on a same-tab
        navigation that never resolves, even though the link opens a new
        tab (target="_blank"). We only need the popup's URL, not for the
        main tab's navigation-wait or the popup's full load to complete.
        """
        with page.expect_popup() as popup_info:
            page.locator(NI.BTN_SHARE_FB).click(no_wait_after=True)

        popup = popup_info.value
        expect(popup).to_have_url(re.compile(r"facebook\.com"), timeout=10000)
        popup.close()

    def test_share_on_linkedin_popup(self, page: Page):
        """See test_share_on_facebook_popup docstring — same fix applied."""
        with page.expect_popup() as popup_info:
            page.locator(NI.BTN_SHARE_LI).click(no_wait_after=True)

        popup = popup_info.value
        expect(popup).to_have_url(re.compile(r"linkedin\.com"), timeout=10000)
        popup.close()


# ── Pagination ────────────────────────────────────────────────────────────────

class TestNewsPagination:

    def test_pagination_controls_visible(self, page: Page):
        expect(page.locator(NI.TEXT_PAGINATION)).to_be_visible()
        expect(page.locator(NI.BTN_PAGE_2)).to_be_visible()
        expect(page.locator(NI.BTN_PAGE_3)).to_be_visible()
        expect(page.locator(NI.BTN_PAGE_4)).to_be_visible()
        expect(page.locator(NI.BTN_NEXT_PAGE)).to_be_visible()


# ── Explore Solutions (Footer) ────────────────────────────────────────────────

class TestExploreSolutions:

    def test_explore_solutions_heading(self, page: Page):
        expect(page.locator(NI.HEADING_EXPLORE)).to_be_visible()
        expect(page.locator(NI.TEXT_EXPLORE_DESC)).to_be_visible()

    @pytest.mark.parametrize("solution_name, details", NI.SOLUTIONS.items())
    def test_explore_solution_cards(self, page: Page, solution_name: str, details: dict):
        # Assert the specific description paragraph for the card
        expect(page.locator(details["desc"])).to_be_visible()
        
        # Assert the 'Explore' button is visible and clickable
        explore_btn = page.locator(details["btn"])
        expect(explore_btn).to_be_visible()
        explore_btn.click()