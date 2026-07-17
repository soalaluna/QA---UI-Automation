import pytest
from playwright.sync_api import Page, expect
from locators.about_locators import AboutLocators as AL


class TestDebugResetView:

    @pytest.fixture(autouse=True)
    def navigate_to_about(self, page: Page):
        page.goto(AL.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        page.locator(AL.NAV_ABOUT).click()
        try:
            page.locator(AL.BTN_ACCEPT_COOKIES).click(timeout=5000)
        except Exception:
            pass
        page.wait_for_url("**/about-us**")
        page.locator(AL.LINK_LETS_CONNECT).click()
        page.locator(AL.BTN_ZOOM_IN).wait_for(state="visible", timeout=20000)

    def test_debug_reset_view_timing(self, page: Page):
        """Debug: click Zoom in multiple times and check Reset view's count/
        visibility at increasing intervals. Safe to delete once
        test_reset_view_clickable is confirmed fixed."""

        print(f"\nReset view count BEFORE any click: {page.locator(AL.BTN_RESET_VIEW).count()}")

        # Click zoom in once
        page.locator(AL.BTN_ZOOM_IN).click()
        for wait_ms in [500, 1000, 2000, 3000, 5000]:
            page.wait_for_timeout(500)
            count = page.locator(AL.BTN_RESET_VIEW).count()
            print(f"After ~{wait_ms}ms since first zoom-in click: Reset view count={count}")

        page.screenshot(path="debug_after_1_zoom.png", full_page=True)

        # Click zoom in several more times in case one click isn't enough
        # of a state change to trigger Reset view's appearance
        for i in range(4):
            page.locator(AL.BTN_ZOOM_IN).click()
            page.wait_for_timeout(300)

        page.wait_for_timeout(1000)
        count_after_multiple = page.locator(AL.BTN_RESET_VIEW).count()
        print(f"\nReset view count AFTER 5 total zoom-in clicks: {count_after_multiple}")
        page.screenshot(path="debug_after_5_zooms.png", full_page=True)

        # Dump all aria-labeled buttons currently on the page, for reference
        buttons = page.locator("button[aria-label]").all()
        print(f"\n--- All aria-labeled buttons currently on page ---")
        for i, b in enumerate(buttons):
            aria = b.get_attribute("aria-label")
            visible = b.is_visible()
            print(f"[{i}] aria-label={aria!r} visible={visible}")