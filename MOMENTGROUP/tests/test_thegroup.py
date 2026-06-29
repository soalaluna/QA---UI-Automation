import pytest
from playwright.sync_api import Page, expect
from locators.thegroup_locators import TheGroupLocators as GL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_group(page: Page):
    """Navigate to The Group page before each test"""
    page.goto(GL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    page.get_by_role("link", name="The Group").first.click()
    page.wait_for_url("**/the-group/**")
    yield


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestGroupNavigation:

    def test_group_page_loads(self, page: Page):
        """The Group page should load at correct URL"""
        # Page lands on /the-group/ — hash fragment is not part of the actual URL
        expect(page).to_have_url(GL.GROUP_URL)


# ── Section Heading Tests ─────────────────────────────────────────────────────

class TestGroupSections:

    def test_the_group_heading_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.locator("#thegroup_frame1").get_by_role("heading", name="The Group")).to_be_visible()

    def test_about_heading_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.get_by_role("heading", name="About")).to_be_visible()

    def test_partnerships_heading_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.locator("#breadcrumbs-3").get_by_role("heading", name="Partnerships")).to_be_visible()

    def test_milestones_heading_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.locator("#breadcrumbs-4").get_by_role("heading", name="Milestones")).to_be_visible()


# ── Breadcrumb Tab Tests ──────────────────────────────────────────────────────

class TestGroupBreadcrumbs:

    def test_breadcrumb_1_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator("#breadcrumbs-1").get_by_role("heading", name="The Group").click()
        expect(page.locator("#breadcrumbs-1")).to_be_visible()

    def test_breadcrumb_partnerships_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator("#breadcrumbs-3").get_by_role("heading", name="Partnerships").click()
        expect(page.locator("#breadcrumbs-3")).to_be_visible()

    def test_breadcrumb_milestones_clickable(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        page.locator("#breadcrumbs-4").get_by_role("heading", name="Milestones").click()
        expect(page.locator("#breadcrumbs-4")).to_be_visible()


# ── Founders Section Tests ────────────────────────────────────────────────────

class TestGroupFounders:

    def test_founders_heading_visible(self, page: Page):
        """Two 'The Founders' headings exist (white + black) — target the black/visible one"""
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(
            page.get_by_role("heading", name="The Founders", exact=True).first
        ).to_be_visible()

    def test_founder_abba_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.get_by_role("heading", name="Abba Napa")).to_be_visible()

    def test_founder_eliza_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.get_by_role("heading", name="Eliza Antonino")).to_be_visible()

    def test_founder_jon_visible(self, page: Page):
        page.add_style_tag(content=DISABLE_ANIMATIONS)
        expect(page.get_by_role("heading", name="Jon Syjuco")).to_be_visible()