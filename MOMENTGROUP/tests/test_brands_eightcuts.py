import pytest
from playwright.sync_api import Page, expect
from locators.brands_eightcuts_locators import EightCutsLocators as EC

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


@pytest.fixture(autouse=True)
def navigate(page: Page):
    page.goto(EC.BASE_URL, wait_until="domcontentloaded", timeout=60000)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    yield


# ── Brand Info Tests ──────────────────────────────────────────────────────────

class TestBrandInfo:

    def test_brand_image_visible(self, page: Page):
        expect(page.locator(EC.IMG_BRAND)).to_be_visible()

    def test_about_text_visible(self, page: Page):
        expect(page.locator(EC.HEADING_ABOUT)).to_be_visible()

    def test_order_online_text_visible(self, page: Page):
        expect(page.locator(EC.TEXT_ORDER_ONLINE)).to_be_visible()

    def test_must_tries_heading_visible(self, page: Page):
        expect(page.locator(EC.HEADING_MUST_TRIES)).to_be_visible()

    def test_must_tries_text_visible(self, page: Page):
        expect(page.locator(EC.TEXT_MUST_TRIES)).to_be_visible()

    def test_chevron_down_visible(self, page: Page):
        expect(page.locator(EC.ICON_CHEVRON_DOWN)).to_be_visible()

    def test_social_handle_visible(self, page: Page):
        expect(page.locator(EC.TEXT_SOCIAL_HANDLE)).to_be_visible()


# ── Navigation Link Tests ─────────────────────────────────────────────────────

class TestNavLinks:

    def test_back_brands_link_attached(self, page: Page):
        expect(page.locator(EC.LINK_BACK_BRANDS).first).to_be_attached()

    def test_back_brands_link_navigates(self, page: Page):
        page.locator(EC.LINK_BACK_BRANDS).first.click()
        expect(page).to_have_url("https://momentgroup.ph/brands")

    def test_hours_locations_link_visible(self, page: Page):
        expect(page.locator(EC.LINK_HOURS_LOCATIONS)).to_be_visible()

    def test_gallery_link_visible(self, page: Page):
        expect(page.locator(EC.LINK_GALLERY)).to_be_visible()

    def test_order_now_link_visible(self, page: Page):
        expect(page.locator(EC.LINK_ORDER_NOW)).to_be_visible()

    def test_order_now_link_navigates(self, page: Page):
        page.locator(EC.LINK_ORDER_NOW).click()
        expect(page).not_to_have_url(EC.BASE_URL)


# ── Social Icon Tests ─────────────────────────────────────────────────────────

class TestSocialIcons:

    def test_brand_icon_first_visible(self, page: Page):
        expect(page.locator(EC.BRAND_ICON_FIRST).first).to_be_visible()

    def test_social_media_second_visible(self, page: Page):
        expect(page.locator(EC.SOCIAL_MEDIA_SECOND)).to_be_visible()

    def test_facebook_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(EC.ICON_FACEBOOK).click()
        popup = popup_info.value
        assert "facebook.com" in popup.url
        popup.close()

    def test_instagram_opens_new_tab(self, page: Page):
        with page.expect_popup() as popup_info:
            page.locator(EC.ICON_INSTAGRAM).click()
        popup = popup_info.value
        assert "instagram.com" in popup.url
        popup.close()


# ── Locations & Hours Tests ───────────────────────────────────────────────────

class TestLocationsHours:

    @pytest.fixture(autouse=True)
    def go_to_hours(self, page: Page):
        page.locator(EC.LINK_HOURS_LOCATIONS).click()
        page.wait_for_timeout(500)

    def test_locations_hours_heading_visible(self, page: Page):
        expect(page.locator(EC.HEADING_LOCATIONS_HOURS)).to_be_visible()

    def test_select_branch_text_visible(self, page: Page):
        expect(page.locator(EC.TEXT_SELECT_BRANCH)).to_be_visible()

    def test_branch_dropdown_visible(self, page: Page):
        expect(page.locator(EC.DROPDOWN_BRANCH)).to_be_visible()

    def test_uptown_bgc_details_visible(self, page: Page):
        expect(page.locator(EC.TEXT_UPTOWN_ADDRESS)).to_be_visible()
        expect(page.locator(EC.LINK_UPTOWN_PHONE)).to_be_visible()
        expect(page.locator(EC.TEXT_UPTOWN_HOURS)).to_be_visible()

    def test_greenhills_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_GREENHILLS).click()
        expect(page.locator(EC.LINK_GREENHILLS_ADDRESS)).to_be_visible()
        expect(page.locator(EC.LINK_GREENHILLS_PHONE)).to_be_visible()
        expect(page.locator(EC.TEXT_GREENHILLS_HOURS)).to_be_visible()

    def test_alabang_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_ALABANG).click()
        expect(page.locator(EC.LINK_ALABANG_ADDRESS)).to_be_visible()

    def test_power_plant_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_POWER_PLANT).click()
        expect(page.locator(EC.LINK_POWER_PLANT_ADDRESS)).to_be_visible()

    def test_salcedo_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_SALCEDO).click()
        expect(page.locator(EC.LINK_SALCEDO_ADDRESS)).to_be_visible()

    def test_serendra_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_SERENDRA).click()
        expect(page.locator(EC.LINK_SERENDRA_ADDRESS)).to_be_visible()

    def test_sm_moa_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_SM_MOA).click()
        expect(page.locator(EC.LINK_SM_MOA_ADDRESS)).to_be_visible()

    def test_sm_megamall_branch_clickable(self, page: Page):
        page.locator(EC.HEADING_SM_MEGAMALL).click()
        expect(page.locator(EC.LINK_SM_MEGAMALL_ADDRESS)).to_be_visible()

    def test_map_container_visible(self, page: Page):
        expect(page.locator(EC.MAP_CONTAINER)).to_be_visible()


# ── Gallery Tests ─────────────────────────────────────────────────────────────

class TestGallery:

    @pytest.fixture(autouse=True)
    def go_to_gallery(self, page: Page):
        page.locator(EC.LINK_GALLERY).click()
        page.wait_for_timeout(500)

    def test_gallery_heading_visible(self, page: Page):
        expect(page.locator(EC.HEADING_GALLERY)).to_be_visible()

    def test_gallery_first_image_visible(self, page: Page):
        expect(page.locator(EC.IMG_GALLERY_FIRST).first).to_be_visible()

    def test_gallery_second_image_visible(self, page: Page):
        expect(page.locator(EC.IMG_GALLERY_SECOND)).to_be_visible()

    def test_pagination_visible(self, page: Page):
        expect(page.locator(EC.TEXT_PAGINATION)).to_be_visible()

    def test_slide_01_clickable(self, page: Page):
        page.locator(EC.SLIDE_01).click()
        expect(page.locator(EC.SLIDE_01)).to_be_attached()

    def test_slide_02_clickable(self, page: Page):
        page.locator(EC.SLIDE_02).click()
        expect(page.locator(EC.SLIDE_02)).to_be_attached()

    def test_slide_03_clickable(self, page: Page):
        page.locator(EC.SLIDE_03).click()
        expect(page.locator(EC.SLIDE_03)).to_be_attached()

    def test_slide_04_clickable(self, page: Page):
        page.locator(EC.SLIDE_04).click()
        expect(page.locator(EC.SLIDE_04)).to_be_attached()

    def test_slide_05_clickable(self, page: Page):
        page.locator(EC.SLIDE_05).click()
        expect(page.locator(EC.SLIDE_05)).to_be_attached()

    def test_slide_06_clickable(self, page: Page):
        page.locator(EC.SLIDE_06).click()
        expect(page.locator(EC.SLIDE_06)).to_be_attached()