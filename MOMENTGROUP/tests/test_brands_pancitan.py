import pytest
from playwright.sync_api import Page, expect
from locators.brands_pancitan_locators import PPLocators as PP


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_pancit_pancitan(page: Page):
    page.goto(PP.PANCIT_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Brand Info ─────────────────────────────────────────────────────────────────

class TestBrandInfo:

    def test_brand_image_visible(self, page: Page):
        expect(page.locator(PP.BRAND_IMAGE)).to_be_visible()

    def test_back_brands_link_visible(self, page: Page):
        expect(page.locator(PP.LINK_BACK_BRANDS)).to_be_visible()

    def test_heading_visible(self, page: Page):
        expect(page.locator(PP.HEADING_BRAND)).to_be_visible()

    def test_order_online_text_visible(self, page: Page):
        expect(page.locator(PP.TEXT_ORDER_ONLINE)).to_be_visible()

    def test_must_tries_heading_visible(self, page: Page):
        expect(page.locator(PP.HEADING_MUST_TRIES)).to_be_visible()

    def test_must_tries_text_visible(self, page: Page):
        expect(page.locator(PP.TEXT_MUST_TRIES)).to_be_visible()

    def test_chevron_down_visible(self, page: Page):
        expect(page.locator(PP.CHEVRON_DOWN)).to_be_visible()

    def test_social_handle_visible(self, page: Page):
        expect(page.locator(PP.TEXT_SOCIAL_HANDLE)).to_be_visible()


# ── Nav Links ──────────────────────────────────────────────────────────────────

class TestNavLinks:

    def test_hours_locations_link_visible(self, page: Page):
        expect(page.locator(PP.LINK_HOURS_LOCATIONS)).to_be_visible()

    def test_gallery_link_visible(self, page: Page):
        expect(page.locator(PP.LINK_GALLERY)).to_be_visible()

    def test_order_now_link_visible(self, page: Page):
        expect(page.locator(PP.LINK_ORDER_NOW)).to_be_visible()

    def test_order_now_link_navigates(self, page: Page):
        page.locator(PP.LINK_ORDER_NOW).click()
        page.wait_for_load_state("networkidle")
        assert PP.ORDER_NOW_URL in page.url
        page.go_back()


# ── Social Icons ───────────────────────────────────────────────────────────────

class TestSocialIcons:

    def test_brand_icon_first_visible(self, page: Page):
        expect(page.locator(PP.BRAND_ICON_FIRST)).to_be_visible()

    def test_social_media_second_visible(self, page: Page):
        expect(page.locator(PP.SOCIAL_MEDIA_SECOND)).to_be_visible()

    def test_facebook_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PP.ICON_FACEBOOK).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "facebook" in popup.url
        popup.close()

    def test_instagram_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(PP.ICON_INSTAGRAM).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "instagram" in popup.url
        popup.close()


# ── Locations & Hours ──────────────────────────────────────────────────────────

class TestLocationsHours:

    @pytest.fixture(autouse=True)
    def navigate_to_hours(self, page: Page):
        page.locator(PP.LINK_HOURS_LOCATIONS).click()
        page.locator(PP.HEADING_LOCATIONS_HOURS).wait_for(state="visible", timeout=10000)

    def test_locations_hours_layout_visible(self, page: Page):
        expect(page.locator(PP.HEADING_LOCATIONS_HOURS)).to_be_visible()
        expect(page.locator(PP.TEXT_SELECT_BRANCH)).to_be_visible()
        expect(page.locator(PP.BRANCH_COMBOBOX)).to_be_visible()

    @pytest.mark.parametrize("branch_name", PP.BRANCHES.keys())
    def test_branches_clickable_and_visible(self, page: Page, branch_name: str):
        """Iterates through every branch in the dictionary and verifies details load."""
        
        # Click the branch name in the sidebar list
        PP.heading_branch_tab(page, branch_name).click()
        
        # Wait for the main detail heading to be visible
        expect(PP.heading_branch_detail(page, branch_name)).to_be_visible()
        
        # Grab locators from dictionary
        branch_data = PP.BRANCHES[branch_name]
        
        # Assert address and phone number text
        expect(page.locator(branch_data["address"])).to_be_visible()
        expect(page.locator(branch_data["phone"])).to_be_visible()
        
        # Verify map container renders after branch click
        expect(page.locator(PP.MAP_CONTAINER)).to_be_visible()


# ── Gallery ────────────────────────────────────────────────────────────────────

class TestGallery:

    @pytest.fixture(autouse=True)
    def navigate_to_gallery(self, page: Page):
        page.locator(PP.LINK_GALLERY).click()
        page.locator(PP.HEADING_GALLERY).wait_for(state="visible", timeout=10000)

    def test_gallery_layout_visible(self, page: Page):
        expect(page.locator(PP.HEADING_GALLERY)).to_be_visible()
        expect(page.locator(PP.GALLERY_IMG_FIRST)).to_be_visible()
        expect(page.locator(PP.GALLERY_PAGINATION)).to_be_visible()

    @pytest.mark.parametrize("slide_idx", range(0, 5))
    def test_slide_navigation(self, page: Page, slide_idx: int):
        """Click slide dot N and verify the corresponding image is visible."""
        if slide_idx >= 4:
            page.locator(PP.GALLERY_PAGINATION).click()
            
        page.locator(PP.SLIDES[slide_idx]).click()
        expect(page.locator(PP.GALLERY_IMGS[slide_idx])).to_be_visible()