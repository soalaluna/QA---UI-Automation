import pytest
from playwright.sync_api import Page, expect
from locators.brands_mama_nams_locators import MNLocators as MN


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_mama_nams(page: Page):
    page.goto(MN.MAMA_NAMS_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Brand Info ─────────────────────────────────────────────────────────────────

class TestBrandInfo:

    def test_brand_image_visible(self, page: Page):
        expect(page.locator(MN.BRAND_IMAGE)).to_be_visible()

    def test_back_brands_link_visible(self, page: Page):
        expect(page.locator(MN.LINK_BACK_BRANDS)).to_be_visible()

    def test_heading_visible(self, page: Page):
        expect(page.locator(MN.HEADING_BRAND)).to_be_visible()

    def test_order_online_text_visible(self, page: Page):
        expect(page.locator(MN.TEXT_ORDER_ONLINE)).to_be_visible()

    def test_must_tries_heading_visible(self, page: Page):
        expect(page.locator(MN.HEADING_MUST_TRIES)).to_be_visible()

    def test_must_tries_text_visible(self, page: Page):
        expect(page.locator(MN.TEXT_MUST_TRIES)).to_be_visible()

    def test_chevron_down_visible(self, page: Page):
        expect(page.locator(MN.CHEVRON_DOWN)).to_be_visible()


# ── Nav Links ──────────────────────────────────────────────────────────────────

class TestNavLinks:

    def test_hours_locations_link_visible(self, page: Page):
        expect(page.locator(MN.LINK_HOURS_LOCATIONS)).to_be_visible()

    def test_gallery_link_visible(self, page: Page):
        expect(page.locator(MN.LINK_GALLERY)).to_be_visible()


# ── Social Icons ───────────────────────────────────────────────────────────────

class TestSocialIcons:

    def test_facebook_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(MN.ICON_FACEBOOK).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "facebook" in popup.url
        popup.close()

    def test_instagram_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(MN.ICON_INSTAGRAM).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "instagram" in popup.url
        popup.close()


# ── Locations & Hours ──────────────────────────────────────────────────────────

class TestLocationsHours:

    @pytest.fixture(autouse=True)
    def navigate_to_hours(self, page: Page):
        page.locator(MN.LINK_HOURS_LOCATIONS).click()
        page.locator(MN.HEADING_LOCATIONS_HOURS).wait_for(state="visible", timeout=10000)

    def test_locations_hours_layout_visible(self, page: Page):
        expect(page.locator(MN.HEADING_LOCATIONS_HOURS)).to_be_visible()
        expect(page.locator(MN.TEXT_SELECT_BRANCH)).to_be_visible()
        expect(page.locator(MN.BRANCH_COMBOBOX)).to_be_visible()

    @pytest.mark.parametrize("branch_name", MN.BRANCHES.keys())
    def test_branches_clickable_and_visible(self, page: Page, branch_name: str):
        """Iterates through every branch in the dictionary and verifies details load."""
        
        # Click the branch name in the sidebar list
        MN.heading_branch_tab(page, branch_name).click()
        
        # Wait for the main detail heading to be visible
        expect(MN.heading_branch_detail(page, branch_name)).to_be_visible()
        
        # Grab locators from dictionary
        branch_data = MN.BRANCHES[branch_name]
        
        # Assert address and phone number text
        expect(page.locator(branch_data["address"])).to_be_visible()
        expect(page.locator(branch_data["phone"])).to_be_visible()
        
        # Verify map container renders after branch click
        expect(page.locator(MN.MAP_CONTAINER)).to_be_visible()


# ── Gallery ────────────────────────────────────────────────────────────────────

class TestGallery:

    @pytest.fixture(autouse=True)
    def navigate_to_gallery(self, page: Page):
        page.locator(MN.LINK_GALLERY).click()
        page.locator(MN.HEADING_GALLERY).wait_for(state="visible", timeout=10000)

    def test_gallery_layout_visible(self, page: Page):
        """Mama Nams currently has an empty gallery on the live site."""
        expect(page.locator(MN.HEADING_GALLERY)).to_be_visible()