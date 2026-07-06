import pytest
from playwright.sync_api import Page, expect
from locators.brands_the_mess_hall_locators import TMHLocators as TMH


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_the_mess_hall(page: Page):
    page.goto(TMH.THE_MESS_HALL_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Brand Info ─────────────────────────────────────────────────────────────────

class TestBrandInfo:

    def test_brand_image_visible(self, page: Page):
        expect(page.locator(TMH.BRAND_IMAGE)).to_be_visible()

    def test_back_brands_link_visible(self, page: Page):
        expect(page.locator(TMH.LINK_BACK_BRANDS)).to_be_visible()

    def test_heading_visible(self, page: Page):
        expect(page.locator(TMH.HEADING_BRAND)).to_be_visible()

    def test_intro_text_visible(self, page: Page):
        expect(page.locator(TMH.TEXT_INTRO)).to_be_visible()

    def test_must_tries_heading_visible(self, page: Page):
        expect(page.locator(TMH.HEADING_MUST_TRIES)).to_be_visible()

    def test_must_tries_text_visible(self, page: Page):
        expect(page.locator(TMH.TEXT_MUST_TRIES)).to_be_visible()

    def test_chevron_down_visible(self, page: Page):
        expect(page.locator(TMH.CHEVRON_DOWN)).to_be_visible()

    def test_social_handle_visible(self, page: Page):
        expect(page.locator(TMH.TEXT_SOCIAL_HANDLE)).to_be_visible()


# ── Nav Links ──────────────────────────────────────────────────────────────────

class TestNavLinks:

    def test_hours_locations_link_visible(self, page: Page):
        expect(page.locator(TMH.LINK_HOURS_LOCATIONS)).to_be_visible()

    def test_gallery_link_visible(self, page: Page):
        expect(page.locator(TMH.LINK_GALLERY)).to_be_visible()

    def test_order_now_link_visible(self, page: Page):
        expect(page.locator(TMH.LINK_ORDER_NOW)).to_be_visible()

    def test_order_now_link_navigates(self, page: Page):
        page.locator(TMH.LINK_ORDER_NOW).click()
        page.wait_for_load_state("networkidle")
        assert TMH.ORDER_NOW_URL in page.url
        page.go_back()


# ── Social Icons ───────────────────────────────────────────────────────────────

class TestSocialIcons:

    def test_brand_icon_first_visible(self, page: Page):
        expect(page.locator(TMH.BRAND_ICON_FIRST)).to_be_visible()

    def test_social_media_second_visible(self, page: Page):
        expect(page.locator(TMH.SOCIAL_MEDIA_SECOND)).to_be_visible()

    def test_facebook_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(TMH.ICON_FACEBOOK).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "facebook" in popup.url
        popup.close()

    def test_instagram_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(TMH.ICON_INSTAGRAM).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "instagram" in popup.url
        popup.close()


# ── Locations & Hours ──────────────────────────────────────────────────────────

class TestLocationsHours:

    @pytest.fixture(autouse=True)
    def navigate_to_hours(self, page: Page):
        page.locator(TMH.LINK_HOURS_LOCATIONS).click()
        page.locator(TMH.HEADING_LOCATIONS_HOURS).wait_for(state="visible", timeout=10000)

    def test_locations_hours_layout_visible(self, page: Page):
        expect(page.locator(TMH.HEADING_LOCATIONS_HOURS)).to_be_visible()
        expect(page.locator(TMH.TEXT_SELECT_BRANCH)).to_be_visible()
        expect(page.locator(TMH.BRANCH_COMBOBOX)).to_be_visible()

    @pytest.mark.parametrize("branch_name", TMH.BRANCHES.keys())
    def test_branches_clickable_and_visible(self, page: Page, branch_name: str):
        """Iterates through every branch in the dictionary and verifies details load."""
        MC = TMH # Alias for shorter code
        
        # Click the branch name in the sidebar list
        MC.heading_branch_tab(page, branch_name).click()
        
        # Wait for the main detail heading to be visible
        expect(MC.heading_branch_detail(page, branch_name)).to_be_visible()
        
        # Grab locators from dictionary
        branch_data = MC.BRANCHES[branch_name]
        
        # Assert address and phone number text
        expect(page.locator(branch_data["address"])).to_be_visible()
        expect(page.locator(branch_data["phone"])).to_be_visible()
        
        # Verify map container renders after branch click
        expect(page.locator(MC.MAP_CONTAINER)).to_be_visible()


# ── Gallery ────────────────────────────────────────────────────────────────────

class TestGallery:

    @pytest.fixture(autouse=True)
    def navigate_to_gallery(self, page: Page):
        page.locator(TMH.LINK_GALLERY).click()
        page.locator(TMH.HEADING_GALLERY).wait_for(state="visible", timeout=10000)

    def test_gallery_layout_visible(self, page: Page):
        expect(page.locator(TMH.HEADING_GALLERY)).to_be_visible()
        expect(page.locator(TMH.GALLERY_IMG_FIRST)).to_be_visible()
        expect(page.locator(TMH.GALLERY_PAGINATION)).to_be_visible()

    # The Mess Hall has 13 slides (0 to 12)
    @pytest.mark.parametrize("slide_idx", range(0, 13))
    def test_slide_navigation(self, page: Page, slide_idx: int):
        """Click slide dot N and verify the corresponding image is visible."""
        # Clicks on pagination text to ensure slider is in view on later slides
        if slide_idx >= 10:
            page.locator(TMH.GALLERY_PAGINATION).click()
            
        page.locator(TMH.SLIDES[slide_idx]).click()
        expect(page.locator(TMH.GALLERY_IMGS[slide_idx])).to_be_visible()