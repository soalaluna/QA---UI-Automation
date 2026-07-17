import pytest
from playwright.sync_api import Page, expect
from locators.about_locators import AboutLocators as AL


class TestDebugMapCrash:

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

    def test_debug_map_crash(self, page: Page):
        """Debug: capture console errors/network failures around the moment
        the map widget disappears after a Zoom in click.
        Safe to delete once the root cause is confirmed."""

        console_messages = []
        page.on("console", lambda msg: console_messages.append(f"[{msg.type}] {msg.text}"))

        page_errors = []
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))

        failed_requests = []
        page.on("requestfailed", lambda req: failed_requests.append(
            f"{req.method} {req.url} — {req.failure}"
        ))

        print(f"\nURL before click: {page.url}")
        print(f"Reset view count before click: {page.locator(AL.BTN_RESET_VIEW).count()}")
        print(f"Zoom in count before click: {page.locator(AL.BTN_ZOOM_IN).count()}")

        page.locator(AL.BTN_ZOOM_IN).click()
        page.wait_for_timeout(2000)

        print(f"\nURL after click + 2s: {page.url}")
        print(f"Reset view count after: {page.locator(AL.BTN_RESET_VIEW).count()}")
        print(f"Zoom in count after: {page.locator(AL.BTN_ZOOM_IN).count()}")

        page.screenshot(path="debug_map_crash.png", full_page=True)

        print(f"\n--- Console messages ({len(console_messages)}) ---")
        for m in console_messages:
            print(m)

        print(f"\n--- Page errors ({len(page_errors)}) ---")
        for e in page_errors:
            print(e)

        print(f"\n--- Failed network requests ({len(failed_requests)}) ---")
        for r in failed_requests:
            print(r)

        # Dump whatever HTML remains where the map widget used to be
        try:
            container_html = page.locator("body").inner_html()[:3000]
            print(f"\n--- Body HTML snippet (first 3000 chars) ---")
            print(container_html)
        except Exception as e:
            print(f"Could not read body HTML: {e}")