import pytest
from playwright.sync_api import Page, expect
from locators.brands_moment_catering_locators import MCL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_moment_catering(page: Page):
    page.goto(MCL.MOMENT_CATERING_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Hero & Brand Info ──────────────────────────────────────────────────────────

class TestHeroSection:

    def test_hero_headings_and_text_visible(self, page: Page):
        expect(page.locator(MCL.HEADING_MAIN)).to_be_visible()
        expect(page.locator(MCL.TEXT_MAKE_HAPPEN)).to_be_visible()
        expect(page.locator(MCL.TEXT_EXPERIENCES)).to_be_visible()
        
    def test_hero_images_visible(self, page: Page):
        expect(page.locator(MCL.IMG_BRAND)).to_be_visible()

    def test_back_to_brands_link_navigates(self, page: Page):
        expect(page.locator(MCL.LINK_BACK_BRANDS)).to_be_visible()
        page.locator(MCL.LINK_BACK_BRANDS).click()
        page.wait_for_load_state("networkidle")
        assert "brands" in page.url


# ── Downloads ──────────────────────────────────────────────────────────────────

class TestDownloads:

    def test_sales_kit_download(self, page: Page):
        """Verifies that the Download link points to a valid file URL."""
        
        # Target the actual <a> tag inside the hidden container
        link_locator = page.locator(MCL.LINK_DOWNLOAD).locator("a")
        
        # 1. Verify the link exists in the DOM
        expect(link_locator).to_have_count(1)
        
        # 2. Extract the href attribute directly
        href = link_locator.get_attribute("href")
        
        # 3. Assert the href exists and is not empty
        assert href is not None
        assert href.strip() != ""

# ── Gallery & Lightbox ─────────────────────────────────────────────────────────

class TestGallery:

    def test_gallery_layout_visible(self, page: Page):
        expect(page.locator(MCL.HEADING_GALLERY)).to_be_visible()
        expect(page.locator(MCL.GALLERY_PAGINATION)).to_be_visible()

    @pytest.mark.parametrize("slide_idx", range(0, 4))
    def test_slide_navigation(self, page: Page, slide_idx: int):
        """Click slide dot N and verify the corresponding image is visible."""
        page.locator(MCL.SLIDES[slide_idx]).click()
        page.wait_for_timeout(500) # Give Slick slider time to animate
        expect(page.locator(MCL.GALLERY_IMGS[slide_idx])).to_be_visible()

    def test_gallery_lightbox_interaction(self, page: Page):
        """Verifies clicking a gallery image opens the lightbox, and the close button works."""
        # Click the currently active slide image
        page.locator(MCL.ACTIVE_SLIDE_IMG).click()
        
        # Verify Lightbox opens and Close button is visible
        expect(page.locator(MCL.BTN_LIGHTBOX_CLOSE)).to_be_visible()
        
        # Close the Lightbox
        page.locator(MCL.BTN_LIGHTBOX_CLOSE).click()
        
        # Verify Lightbox closes
        expect(page.locator(MCL.BTN_LIGHTBOX_CLOSE)).not_to_be_visible()


# ── Cuisines ───────────────────────────────────────────────────────────────────

class TestCuisines:

    def test_cuisines_layout_visible(self, page: Page):
        expect(page.locator(MCL.HEADING_CUISINES)).to_be_visible()
        expect(page.locator(MCL.TEXT_FILIPINO)).to_be_visible()
        expect(page.locator(MCL.TEXT_EUROMED)).to_be_visible()
        expect(page.locator(MCL.TEXT_CARVINGS)).to_be_visible()
        expect(page.locator(MCL.TEXT_COCKTAILS)).to_be_visible()
        expect(page.locator(MCL.TEXT_COCKTAILS_DESC)).to_be_visible()

    def test_cuisine_blocks_visible(self, page: Page):
        expect(page.locator(MCL.CUISINE_INFO_1)).to_be_visible()
        expect(page.locator(MCL.CUISINE_INFO_2)).to_be_visible()
        expect(page.locator(MCL.CUISINE_INFO_3)).to_be_visible()
        expect(page.locator(MCL.CUISINE_INFO_4)).to_be_visible()
        expect(page.locator(MCL.CUISINE_INFO_5)).to_be_visible()
        
    def test_cuisine_elements_clickable(self, page: Page):
        # Interact with the elements as simulated by the codegen
        page.locator(MCL.TEXT_FILIPINO).click()
        page.locator(MCL.CUISINE_INFO_1).click()
        page.locator(MCL.CUISINE_INFO_2).click()


# ── Locations ──────────────────────────────────────────────────────────────────

class TestLocations:

    def test_locations_layout_visible(self, page: Page):
        expect(page.locator(MCL.HEADING_LOCATIONS)).to_be_visible()
        
        # Venue Catering
        expect(page.locator(MCL.TEXT_VENUE_CATERING)).to_be_visible()
        expect(page.locator(MCL.TEXT_BRINGS_YOUR)).to_be_visible()
        
        # Accredited Venues
        expect(page.locator(MCL.TEXT_ACCREDITED)).to_be_visible()
        expect(page.locator(MCL.TEXT_MOA_ARENA)).to_be_visible()
        
        # Mess Hall
        expect(page.locator(MCL.TEXT_MESS_HALL)).to_be_visible()

    def test_location_images_visible(self, page: Page):
        expect(page.locator(MCL.IMG_LOC_F3_1)).to_be_visible()
        expect(page.locator(MCL.IMG_LOC_F3_2)).to_be_visible()
        expect(page.locator(MCL.IMG_LOC_F3_3)).to_be_visible()
        expect(page.locator(MCL.LOC_ROW)).to_be_visible()
        expect(page.locator(MCL.IMG_LOC_P2_1)).to_be_visible()
        expect(page.locator(MCL.IMG_LOC_P2_2)).to_be_visible()


# ── Contact / How Can We Help ──────────────────────────────────────────────────

class TestContact:

    def test_contact_layout_visible(self, page: Page):
        expect(page.locator(MCL.HEADING_HELP)).to_be_visible()
        expect(page.locator(MCL.TEXT_INQUIRIES)).to_be_visible()
        expect(page.locator(MCL.TEXT_EVENTS_EMAIL)).to_be_visible()
        expect(page.locator(MCL.TEXT_CONCERNS)).to_be_visible()
        expect(page.locator(MCL.TEXT_SPEAK_FREELY)).to_be_visible()
        expect(page.locator(MCL.TEXT_HOLLER)).to_be_visible()
        expect(page.locator(MCL.TEXT_HOURS)).to_be_visible()
        expect(page.locator(MCL.IMG_HELP_SECTION)).to_be_visible()
        
    def test_email_link_has_mailto_intent(self, page: Page):
        """Verifies the email link is properly configured with a mailto: href."""
        expect(page.locator(MCL.LINK_EMAIL_ACTION)).to_be_visible()
        href = page.locator(MCL.LINK_EMAIL_ACTION).get_attribute("href")
        assert "mailto:events@momentgroup.ph" in href