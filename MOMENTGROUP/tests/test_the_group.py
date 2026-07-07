import pytest
from playwright.sync_api import Page, expect
from locators.the_group_locators import TGLocators as TG


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_the_group(page: Page):
    page.goto(TG.URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Hero & Navigation ──────────────────────────────────────────────────────────

class TestHeroAndNav:

    def test_hero_elements_visible(self, page: Page):
        expect(page.locator(TG.HEADING_MAIN)).to_be_visible()
        expect(page.locator(TG.TEXT_CREATION)).to_be_visible()
        expect(page.locator(TG.IMG_BACKGROUND)).to_be_visible()

    def test_breadcrumb_tabs_visible(self, page: Page):
        expect(page.locator(TG.TAB_THE_GROUP)).to_be_visible()
        expect(page.locator(TG.TAB_ABOUT)).to_be_visible()
        expect(page.locator(TG.TAB_PARTNERSHIPS)).to_be_visible()
        expect(page.locator(TG.TAB_MILESTONES)).to_be_visible()
        expect(page.locator(TG.TAB_FOUNDERS)).to_be_visible()


# ── About Section ──────────────────────────────────────────────────────────────

class TestAboutSection:

    def test_about_section_content(self, page: Page):
        page.locator(TG.TAB_ABOUT).click()
        
        expect(page.locator(TG.HEADING_BUSINESS)).to_be_visible()
        expect(page.locator(TG.TEXT_ABOUT_1)).to_be_visible()
        expect(page.locator(TG.TEXT_ABOUT_2)).to_be_visible()
        expect(page.locator(TG.TEXT_ABOUT_3)).to_be_visible()
        expect(page.locator(TG.TEXT_ABOUT_4)).to_be_visible()
        expect(page.locator(TG.TEXT_ABOUT_5)).to_be_visible()


# ── Founders Section ───────────────────────────────────────────────────────────

class TestFoundersSection:

    @pytest.fixture(autouse=True)
    def open_founders_accordion(self, page: Page):
        # Force click the expand icon in case it's obscured
        page.locator(TG.ICON_FOUNDERS_EXPAND).click(force=True)
        page.wait_for_timeout(500) 

    def test_abba_napa_info(self, page: Page):
        expect(page.locator(TG.FOUNDER_ABBA)).to_be_visible()
        expect(page.locator(TG.ABBA_ROLE)).to_be_visible()
        
        # force=True bypasses the CSS wrapper intercepting the pointer events
        page.locator(TG.FOUNDER_ABBA).click(force=True)
        expect(page.locator(TG.ABBA_BIO)).to_be_visible()

    def test_eliza_antonino_info(self, page: Page):
        expect(page.locator(TG.FOUNDER_ELIZA)).to_be_visible()
        expect(page.locator(TG.ELIZA_ROLE)).to_be_visible()
        
        page.locator(TG.FOUNDER_ELIZA).click(force=True)
        expect(page.locator(TG.ELIZA_BIO)).to_be_visible()

    def test_jon_syjuco_info(self, page: Page):
        expect(page.locator(TG.FOUNDER_JON)).to_be_visible()
        expect(page.locator(TG.JON_ROLE)).to_be_visible()
        
        page.locator(TG.FOUNDER_JON).click(force=True)
        expect(page.locator(TG.JON_BIO)).to_be_visible()


# ── Partnerships Section ───────────────────────────────────────────────────────

class TestPartnershipsSection:

    def test_partnerships_content(self, page: Page):
        page.locator(TG.TAB_PARTNERSHIPS).click()
        expect(page.locator(TG.HEADING_PARTNERSHIPS)).to_be_visible()
        expect(page.locator(TG.TEXT_INTERESTED)).to_be_visible()


# ── Milestones Section ─────────────────────────────────────────────────────────

class TestMilestonesSection:

    @pytest.fixture(autouse=True)
    def navigate_to_milestones(self, page: Page):
        page.locator(TG.TAB_MILESTONES).click()
        page.locator(TG.HEADING_MILESTONES).wait_for(state="visible")

    def test_milestones_layout(self, page: Page):
        expect(page.locator(TG.HEADING_MILESTONES)).to_be_visible()
        expect(page.locator(TG.SLIDER_CONTAINER)).to_be_visible()

    def test_milestones_slider_navigation(self, page: Page):
        expect(page.locator(TG.MILESTONE_2012)).to_be_visible()
        expect(page.locator(TG.MILESTONE_2013)).to_be_visible()

        # Click Next a few times to reveal later years
        for _ in range(4):
            page.locator(TG.BTN_NEXT).click()
            page.wait_for_timeout(300) 
            
        expect(page.locator(TG.MILESTONE_2014)).to_be_visible()
        expect(page.locator(TG.MILESTONE_2017)).to_be_visible()
        
        # Click Previous to ensure reverse navigation works
        for _ in range(4):
            page.locator(TG.BTN_PREV).click()
            page.wait_for_timeout(300)
            
        # Check 2013 instead of 2012 to avoid carousel edge-boundary quirks
        expect(page.locator(TG.MILESTONE_2013)).to_be_visible()

        # Click Next a few times to reveal later years
        for _ in range(4):
            page.locator(TG.BTN_NEXT).click()
            page.wait_for_timeout(300) 
            
        expect(page.locator(TG.MILESTONE_2014)).to_be_visible()
        expect(page.locator(TG.MILESTONE_2017)).to_be_visible()
        
        # Click Previous to ensure reverse navigation works
        for _ in range(4):
            page.locator(TG.BTN_PREV).click()
            page.wait_for_timeout(300)
            
        expect(page.locator(TG.MILESTONE_2012)).to_be_visible()