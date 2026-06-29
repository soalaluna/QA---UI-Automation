import pytest
from playwright.sync_api import Page, expect
from locators.header_locators import HeaderLocators as HL

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_homepage(page: Page):
    page.goto(HL.BASE_URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    yield


# ── Visibility Tests ──────────────────────────────────────────────────────────

class TestHeaderVisibility:

    def test_homepage_link_visible(self, page: Page):
        """Homepage logo link should be visible"""
        expect(page.get_by_role("link", name="Homepage")).to_be_visible()

    def test_menu_link_visible(self, page: Page):
        """MENU nav link should be visible"""
        expect(page.get_by_role("link", name="Go to Page MENU")).to_be_visible()

    def test_about_link_visible(self, page: Page):
        """ABOUT nav link should be visible"""
        expect(page.get_by_role("link", name="Go to Page ABOUT")).to_be_visible()

    def test_press_link_visible(self, page: Page):
        """PRESS nav link should be visible"""
        expect(page.get_by_role("banner").get_by_role("listitem").filter(has_text="PRESS")).to_be_visible()

    def test_contact_link_visible(self, page: Page):
        """CONTACT nav link should be visible"""
        expect(page.get_by_role("link", name="Go to Page CONTACT")).to_be_visible()

    def test_reservations_link_visible(self, page: Page):
        """RESERVATIONS nav link should be visible"""
        expect(page.get_by_role("link", name="Go to Page RESERVATIONS")).to_be_visible()

    def test_order_online_link_visible(self, page: Page):
        """ORDER ONLINE nav link should be visible"""
        expect(page.get_by_role("link", name="Go to Page ORDER ONLINE")).to_be_visible()


# ── Navigation Tests ──────────────────────────────────────────────────────────

class TestHeaderNavigation:

    def test_homepage_link_stays_on_homepage(self, page: Page):
        """Clicking Homepage logo should stay on homepage"""
        page.get_by_role("link", name="Homepage").click()
        expect(page).to_have_url(HL.BASE_URL)

    def test_menu_link_navigates(self, page: Page):
        """Clicking MENU should navigate to menu page"""
        page.get_by_role("link", name="Go to Page MENU").click()
        page.wait_for_load_state("networkidle")
        assert "menu" in page.url.lower(), f"Expected menu page, got: {page.url}"

    def test_about_link_navigates(self, page: Page):
        """Clicking ABOUT should navigate to about page"""
        page.get_by_role("link", name="Go to Page ABOUT").click()
        page.wait_for_load_state("networkidle")
        assert "who-we-are" in page.url.lower(), f"Expected about page, got: {page.url}"

    def test_press_link_navigates(self, page: Page):
        """Clicking PRESS should navigate to press page"""
        page.get_by_role("banner").get_by_role("listitem").filter(has_text="PRESS").click()
        page.wait_for_load_state("networkidle")
        assert "press" in page.url.lower(), f"Expected press page, got: {page.url}"

    def test_contact_link_navigates(self, page: Page):
        """Clicking CONTACT should navigate to contact page"""
        page.get_by_role("link", name="Go to Page CONTACT").click()
        page.wait_for_load_state("networkidle")
        assert "contact" in page.url.lower(), f"Expected contact page, got: {page.url}"

    def test_reservations_link_navigates(self, page: Page):
        """Clicking RESERVATIONS should navigate to reservation page"""
        page.get_by_role("link", name="Go to Page RESERVATIONS").click()
        page.wait_for_load_state("networkidle")
        assert "reservation" in page.url.lower(), f"Expected reservation page, got: {page.url}"

    def test_order_online_opens_popup(self, page: Page):
        """Clicking ORDER ONLINE should open external site in new tab"""
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Go to Page ORDER ONLINE").click()
        popup = popup_info.value
        assert "atlas.kitchen" in popup.url, f"Expected atlas.kitchen, got: {popup.url}"
        popup.close()