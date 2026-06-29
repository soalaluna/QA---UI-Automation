import pytest
from playwright.sync_api import Page, expect
from locators.newsinsights_locators import NewsInsightsLocators as NL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_news(page: Page):
    page.goto(NL.BASE_URL, wait_until="domcontentloaded", timeout=60000)
    page.locator(NL.NAV_NEWS_INSIGHTS).click()
    page.wait_for_url("**/news-and-insights**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestNewsNavigation:

    def test_news_page_loads(self, page: Page):
        expect(page).to_have_url(NL.NEWS_URL)


# ── Article Card Tests ────────────────────────────────────────────────────────

class TestArticleCards:

    def test_read_more_button_visible(self, page: Page):
        """At least one 'Read more article' button should be present."""
        buttons = page.locator(NL.BTN_READ_MORE_FIRST)
        expect(buttons.first).to_be_visible()

    def test_read_more_button_clickable(self, page: Page):
        """Clicking 'Read more' on the first article should expand or navigate."""
        page.locator(NL.BTN_READ_MORE_FIRST).first.click()
        page.wait_for_timeout(500)
        # After expanding, a corresponding "Read article" link should appear
        expect(page.locator(NL.LINK_READ_ARTICLE_FIRST).first).to_be_visible()

    def test_articles_have_facebook_share_links(self, page: Page):
        """All visible Facebook share links should have valid hrefs."""
        links = page.locator(NL.LINK_SHARE_FACEBOOK)
        count = links.count()
        assert count > 0, "No Facebook share links found"
        for i in range(min(count, 10)):
            href = links.nth(i).get_attribute("href")
            assert href and href.strip() != "", f"Facebook share link {i} has empty href"

    def test_articles_have_linkedin_share_links(self, page: Page):
        """All visible LinkedIn share links should have valid hrefs."""
        links = page.locator(NL.LINK_SHARE_LINKEDIN)
        count = links.count()
        assert count > 0, "No LinkedIn share links found"
        for i in range(min(count, 10)):
            href = links.nth(i).get_attribute("href")
            assert href and href.strip() != "", f"LinkedIn share link {i} has empty href"

    def test_first_article_facebook_share_opens_popup(self, page: Page):
        """Sample test: first article's Facebook share should open a popup."""
        with page.expect_popup() as popup_info:
            page.locator(NL.LINK_SHARE_FACEBOOK).first.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_first_article_linkedin_share_opens_popup(self, page: Page):
        """Sample test: first article's LinkedIn share should open a popup."""
        with page.expect_popup() as popup_info:
            page.locator(NL.LINK_SHARE_LINKEDIN).first.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()


# ── Pagination Tests ──────────────────────────────────────────────────────────

class TestNewsPagination:

    def test_page_2_clickable(self, page: Page):
        page.locator(NL.BTN_PAGE_2).click()
        expect(page.locator(NL.BTN_PAGE_2)).to_be_visible()

    def test_page_3_clickable(self, page: Page):
        page.locator(NL.BTN_PAGE_2).click()
        page.locator(NL.BTN_PAGE_3).click()
        expect(page.locator(NL.BTN_PAGE_3)).to_be_visible()

    def test_page_4_clickable(self, page: Page):
        page.locator(NL.BTN_PAGE_2).click()
        page.locator(NL.BTN_PAGE_3).click()
        page.locator(NL.BTN_PAGE_4).click()
        expect(page.locator(NL.BTN_PAGE_4)).to_be_visible()

    def test_next_page_clickable(self, page: Page):
        page.locator(NL.BTN_NEXT_PAGE).click()
        expect(page.locator(NL.BTN_PAGE_2)).to_be_visible()

    def test_previous_page_clickable(self, page: Page):
        page.locator(NL.BTN_NEXT_PAGE).click()
        page.locator(NL.BTN_PREV_PAGE).click()
        expect(page.locator(NL.BTN_PAGE_2)).to_be_visible()


# ── Category Filter Tests ─────────────────────────────────────────────────────

class TestNewsCategoryFilters:

    def test_news_articles_tab_clickable(self, page: Page):
        page.locator(NL.TAB_NEWS_ARTICLES).click()
        expect(page.locator(NL.TAB_NEWS_ARTICLES)).to_be_visible()

    def test_events_tab_clickable(self, page: Page):
        page.locator(NL.TAB_EVENTS).click()
        expect(page.locator(NL.TAB_EVENTS)).to_be_visible()


# ── Explore Link Tests ────────────────────────────────────────────────────────

class TestExploreLinks:

    def test_explore_links_present(self, page: Page):
        """Multiple 'Explore' links should be present on the page."""
        links = page.locator(NL.LINK_EXPLORE)
        assert links.count() > 0, "No Explore links found"

    def test_first_explore_link_navigates(self, page: Page):
        page.locator(NL.LINK_EXPLORE).first.click()
        expect(page).not_to_have_url(NL.NEWS_URL)