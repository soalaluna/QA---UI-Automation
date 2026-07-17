import pytest
from playwright.sync_api import Page, expect
from locators.about_locators import AboutLocators as AL


class TestDebugMapLocation:

    def test_debug_map_on_about_page(self, page: Page):
        """Debug: check whether Zoom in/Reset view exist on the About page
        itself (before any navigation), and whether they're wrapped in a
        link pointing elsewhere. Safe to delete once resolved."""

        page.goto(AL.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        page.locator(AL.NAV_ABOUT).click()
        try:
            page.locator(AL.BTN_ACCEPT_COOKIES).click(timeout=5000)
        except Exception:
            pass
        page.wait_for_url("**/about-us**")

        # Click "Let's Connect" and check state at multiple points BEFORE
        # doing anything else, without waiting for zoom-in visibility
        page.locator(AL.LINK_LETS_CONNECT).click()

        for delay in [0, 300, 800, 1500]:
            page.wait_for_timeout(delay if delay == 0 else 300)
            print(f"\n--- {delay}ms after Let's Connect click ---")
            print(f"URL: {page.url}")
            print(f"Zoom in count: {page.locator(AL.BTN_ZOOM_IN).count()}")
            print(f"Reset view count: {page.locator(AL.BTN_RESET_VIEW).count()}")

        # If Zoom in exists at this point, check its ancestor chain for a
        # wrapping <a> tag that might explain unexpected navigation
        if page.locator(AL.BTN_ZOOM_IN).count() > 0:
            ancestor_info = page.locator(AL.BTN_ZOOM_IN).evaluate(
                """el => {
                    let node = el;
                    const chain = [];
                    for (let i = 0; i < 6 && node; i++) {
                        chain.push({tag: node.tagName, href: node.getAttribute && node.getAttribute('href')});
                        node = node.parentElement;
                    }
                    return chain;
                }"""
            )
            print(f"\nAncestor chain of Zoom in button (up to 6 levels):")
            for a in ancestor_info:
                print(a)

        page.screenshot(path="debug_map_location_final.png", full_page=True)
        print(f"\nFinal URL: {page.url}")