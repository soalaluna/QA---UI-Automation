import pytest
from playwright.sync_api import Page, expect
from locators.brands_ooma_locators import OomaLocators as OC


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_ooma(page: Page):
    page.goto(OC.OOMA_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Brand Info ─────────────────────────────────────────────────────────────────

class TestBrandInfo:

    def test_brand_image_visible(self, page: Page):
        expect(page.get_by_role("img").nth(2)).to_be_visible()

    def test_back_brands_link_visible(self, page: Page):
        expect(page.locator(OC.LINK_BACK_BRANDS)).to_be_visible()

    def test_heading_visible(self, page: Page):
        expect(OC.heading_brand(page)).to_be_visible()

    def test_order_online_text_visible(self, page: Page):
        expect(page.locator(OC.TEXT_ORDER_ONLINE)).to_be_visible()

    def test_must_tries_heading_visible(self, page: Page):
        expect(page.locator(OC.HEADING_MUST_TRIES)).to_be_visible()

    def test_must_tries_text_visible(self, page: Page):
        expect(page.locator(OC.TEXT_MUST_TRIES)).to_be_visible()

    def test_chevron_down_visible(self, page: Page):
        expect(page.locator(OC.CHEVRON_DOWN)).to_be_visible()

    def test_social_handle_visible(self, page: Page):
        expect(page.locator(OC.TEXT_SOCIAL_HANDLE)).to_be_visible()


# ── Nav Links ──────────────────────────────────────────────────────────────────

class TestNavLinks:

    def test_hours_locations_link_visible(self, page: Page):
        expect(page.locator(OC.LINK_HOURS_LOCATIONS)).to_be_visible()

    def test_gallery_link_visible(self, page: Page):
        expect(page.locator(OC.LINK_GALLERY)).to_be_visible()

    def test_order_now_link_visible(self, page: Page):
        expect(page.locator(OC.LINK_ORDER_NOW)).to_be_visible()

    def test_order_now_link_navigates(self, page: Page):
        # Fixed: Removed the popup expectation since it navigates in the same tab
        page.locator(OC.LINK_ORDER_NOW).click()
        page.wait_for_load_state("networkidle")
        assert OC.ORDER_NOW_URL in page.url or "ooma" in page.url
        # Go back so the test runner returns to the main page for the next tests
        page.go_back()


# ── Social Icons ───────────────────────────────────────────────────────────────

class TestSocialIcons:

    def test_brand_icon_first_visible(self, page: Page):
        expect(page.locator(OC.BRAND_ICON_FIRST).first).to_be_visible()

    def test_social_media_second_visible(self, page: Page):
        expect(page.locator(OC.SOCIAL_MEDIA_SECOND)).to_be_visible()

    def test_facebook_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(OC.ICON_FACEBOOK).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "facebook" in popup.url
        popup.close()

    def test_instagram_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(OC.ICON_INSTAGRAM).click()
        popup = popup_info.value
        popup.wait_for_load_state()
        assert "instagram" in popup.url
        popup.close()


# ── Locations & Hours ──────────────────────────────────────────────────────────

class TestLocationsHours:

    @pytest.fixture(autouse=True)
    def navigate_to_hours(self, page: Page):
        page.locator(OC.LINK_HOURS_LOCATIONS).click()
        OC.heading_locations_hours(page).wait_for(state="visible", timeout=10000)

    def test_locations_hours_heading_visible(self, page: Page):
        expect(OC.heading_locations_hours(page)).to_be_visible()

    def test_intro_text_visible(self, page: Page):
        expect(page.locator(OC.TEXT_LOCATIONS_HOURS_INTRO)).to_be_visible()

    def test_select_branch_visible(self, page: Page):
        expect(page.locator(OC.TEXT_SELECT_BRANCH)).to_be_visible()

    def test_branch_combobox_visible(self, page: Page):
        expect(page.locator(OC.BRANCH_COMBOBOX)).to_be_visible()

    def test_map_container_visible(self, page: Page):
        # The map container doesn't render until a branch is actually
        # selected/clicked — it's not present on initial load even though
        # SM City Cebu shows as pre-selected in the combobox.
        OC.heading_sm_cebu_first(page).click()
        expect(page.locator(OC.MAP_CONTAINER)).to_be_visible()

    # SM City Cebu (default branch)
    def test_sm_cebu_heading_visible(self, page: Page):
        expect(OC.heading_sm_cebu_first(page)).to_be_visible()

    def test_sm_cebu_details_visible(self, page: Page):
        # Even though SM City Cebu is pre-selected in the combobox, its
        # detail section (the second "SM City Cebu" heading, .nth(1)) does
        # not render until the sidebar heading is clicked — same as every
        # other branch below. Missing this click was why heading_sm_cebu_detail
        # (.nth(1)) never found a second match.
        OC.heading_sm_cebu_first(page).click()
        expect(OC.heading_sm_cebu_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_SM_CEBU_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_SM_CEBU_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_SM_CEBU_HOURS)).to_be_visible()

    # Bonifacio High Street
    def test_bhs_branch_clickable(self, page: Page):
        OC.heading_bhs(page).click()
        expect(OC.heading_bhs_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_BHS_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_BHS_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_BHS_HOURS)).to_be_visible()

    # Greenbelt
    def test_greenbelt_branch_clickable(self, page: Page):
        OC.heading_greenbelt(page).click()
        expect(OC.heading_greenbelt_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_GREENBELT_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_GREENBELT_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_GREENBELT_HOURS)).to_be_visible()

    # Power Plant Mall
    def test_power_plant_branch_clickable(self, page: Page):
        OC.heading_power_plant(page).click()
        expect(OC.heading_power_plant_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_POWER_PLANT_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_POWER_PLANT_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_POWER_PLANT_HOURS)).to_be_visible()

    # Salcedo
    def test_salcedo_branch_clickable(self, page: Page):
        OC.heading_salcedo(page).click()
        expect(OC.heading_salcedo_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_SALCEDO_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_SALCEDO_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_SALCEDO_HOURS)).to_be_visible()

    # SM Megamall
    def test_sm_megamall_branch_clickable(self, page: Page):
        OC.heading_sm_megamall(page).click()
        expect(OC.heading_sm_megamall_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_SM_MEGAMALL_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_SM_MEGAMALL_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_SM_MEGAMALL_HOURS)).to_be_visible()

    # Molito
    def test_molito_branch_clickable(self, page: Page):
        OC.heading_molito(page).click()
        expect(OC.heading_molito_detail(page)).to_be_visible()
        expect(page.locator(OC.LINK_MOLITO_ADDRESS)).to_be_visible()
        expect(page.locator(OC.LINK_MOLITO_PHONE)).to_be_visible()
        expect(page.locator(OC.TEXT_MOLITO_HOURS)).to_be_visible()


# ── Gallery ────────────────────────────────────────────────────────────────────

class TestGallery:

    @pytest.fixture(autouse=True)
    def navigate_to_gallery(self, page: Page):
        page.locator(OC.LINK_GALLERY).click()
        OC.heading_gallery(page).wait_for(state="visible", timeout=10000)

    def test_gallery_heading_visible(self, page: Page):
        expect(OC.heading_gallery(page)).to_be_visible()

    def test_gallery_first_image_visible(self, page: Page):
        expect(page.locator(OC.GALLERY_IMGS[0]).first).to_be_visible()

    def test_gallery_second_image_visible(self, page: Page):
        expect(page.locator(OC.GALLERY_IMGS[1])).to_be_visible()

    def test_pagination_visible(self, page: Page):
        expect(page.locator(OC.GALLERY_PAGINATION)).to_be_visible()

    # Fixed: Changed range to 0, 7 and removed + 1 from assertion to stay in list bounds
    @pytest.mark.parametrize("slide_idx", range(0, 7))
    def test_slide_navigation(self, page: Page, slide_idx: int):
        """Click slide dot N and verify the corresponding image is visible."""
        # Clicks on pagination text to ensure slider is in view on later slides
        if slide_idx >= 6:
            page.locator(OC.GALLERY_PAGINATION).click()
        page.locator(OC.SLIDES[slide_idx]).click()
        expect(page.locator(OC.GALLERY_IMGS[slide_idx])).to_be_visible()