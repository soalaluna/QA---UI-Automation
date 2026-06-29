import pytest
from playwright.sync_api import Page, expect
from locators.press_locators import PressLocators as PL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_press(page: Page):
    page.goto(PL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.locator(PL.NAV_PRESS).first.click()
    page.wait_for_url("**/press/**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestPressNavigation:

    def test_press_page_loads(self, page: Page):
        expect(page).to_have_url(PL.PRESS_URL)


# ── Pagination Tests ──────────────────────────────────────────────────────────

class TestPressPagination:

    def test_page_2_button_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()
        expect(page.get_by_role("button", name="2")).to_be_visible()

    def test_page_3_button_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()
        page.get_by_role("button", name="3").click()
        expect(page.get_by_role("button", name="3")).to_be_visible()

    def test_page_4_button_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()
        page.get_by_role("button", name="3").click()
        page.get_by_role("button", name="4").click()
        expect(page.get_by_role("button", name="4")).to_be_visible()

    def test_prev_button_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()
        page.get_by_role("button").first.click()
        expect(page.get_by_role("button", name="1")).to_be_visible()

    def test_next_button_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button").nth(5).click()
        expect(page.get_by_role("button", name="2")).to_be_visible()


# ── Article Link Tests (Page 1) ───────────────────────────────────────────────

class TestPressArticlesPage1:

    def test_cna_article_opens_popup(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="read more", exact=True).click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_moment_group_article_opens_popup(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        link = page.get_by_role("link", name="Moment Group").first
        expect(link).to_be_attached()
        with page.expect_popup() as popup_info:
            link.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_overseas_outpost_article_opens_popup(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Hayop – Overseas Outpost of").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_filipino_restaurant_article_opens_popup(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Filipino restaurant Hayop").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_sister_article_opens_popup(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="hayop, Manam's sister").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_best_eats_article_opens_popup(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Best eats of 2024: Best").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()


# ── Article Link Tests (Page 2) ───────────────────────────────────────────────

class TestPressArticlesPage2:

    @pytest.fixture(autouse=True)
    def go_to_page_2(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()

    def test_joys_of_article_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="At Hayop, the joys of").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_first_fine_article_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Hayop: Singapore's First Fine").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_joyous_article_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Hayop is a joyous").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_food_picks_article_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Food Picks: Filipino fare at").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_adobo_article_opens_popup(self, page: Page):
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="From adobo to zipyu thee").click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()


# ── Article Link Tests (Page 3) ───────────────────────────────────────────────
# NOTE: Article titles on page 3+ shift as new articles are published.
# Using a.card selectors is more stable than hardcoding titles.

class TestPressArticlesPage3:

    @pytest.fixture(autouse=True)
    def go_to_page_3(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()
        page.wait_for_selector("button:has-text('3')")
        page.get_by_role("button", name="3").click()
        page.wait_for_timeout(500)

    def test_page_3_first_article_opens_popup(self, page: Page):
        article_link = page.locator("a.card").first
        expect(article_link).to_be_visible()
        with page.expect_popup() as popup_info:
            article_link.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_page_3_second_article_opens_popup(self, page: Page):
        article_link = page.locator("a.card").nth(1)
        expect(article_link).to_be_visible()
        with page.expect_popup() as popup_info:
            article_link.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_page_3_third_article_opens_popup(self, page: Page):
        article_link = page.locator("a.card").nth(2)
        expect(article_link).to_be_visible()
        with page.expect_popup() as popup_info:
            article_link.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()


# ── Article Link Tests (Page 4) ───────────────────────────────────────────────

class TestPressArticlesPage4:

    @pytest.fixture(autouse=True)
    def go_to_page_4(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.get_by_role("button", name="2").click()
        page.wait_for_selector("button:has-text('3')")
        page.get_by_role("button", name="3").click()
        page.wait_for_selector("button:has-text('4')")
        page.get_by_role("button", name="4").click()
        page.wait_for_timeout(500)

    def test_page_4_has_working_article_link(self, page: Page):
        article_link = page.locator("a.card").first
        expect(article_link).to_be_visible()
        with page.expect_popup() as popup_info:
            article_link.click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestPressFooter:

    def test_instagram_link_present(self, page: Page):
        expect(page.locator(PL.FOOTER_INSTAGRAM)).to_be_attached()

    def test_privacy_policy_navigates(self, page: Page):
        page.locator(PL.FOOTER_PRIVACY).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/privacy-policy/")

    def test_terms_conditions_navigates(self, page: Page):
        page.locator(PL.FOOTER_TERMS).first.click()
        expect(page).to_have_url("https://hayopnimanam.com/terms-conditions/")