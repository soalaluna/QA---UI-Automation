from playwright.sync_api import Page
from locators.about_locators import AboutLocators as AL


def test_debug_contact_page_direct(page: Page):
    """Debug: go straight to the Contact page (bypassing About/Let's Connect)
    and see what map controls actually exist there, with a generous wait.
    Safe to delete once the real fix is confirmed."""

    page.goto("https://www.pldtglobal.com/en/contact-us", wait_until="domcontentloaded", timeout=60000)
    try:
        page.locator(AL.BTN_ACCEPT_COOKIES).click(timeout=5000)
    except Exception:
        pass

    # Generous wait, then screenshot + check
    page.wait_for_timeout(5000)
    page.screenshot(path="debug_contact_direct_5s.png", full_page=True)

    print(f"\nURL: {page.url}")
    print(f"Zoom in count: {page.locator(AL.BTN_ZOOM_IN).count()}")
    print(f"Reset view count: {page.locator(AL.BTN_RESET_VIEW).count()}")
    print(f"Zoom out count: {page.locator(AL.BTN_ZOOM_OUT).count()}")

    # Dump every aria-labeled button on the whole page
    buttons = page.locator("button[aria-label]").all()
    print(f"\n--- All aria-labeled buttons on Contact page ({len(buttons)}) ---")
    for i, b in enumerate(buttons):
        aria = b.get_attribute("aria-label")
        visible = b.is_visible()
        print(f"[{i}] aria-label={aria!r} visible={visible}")

    # Check for iframes (maybe the map is an embedded Google Maps iframe)
    frames = page.frames
    print(f"\n--- Frames on Contact page ({len(frames)}) ---")
    for i, f in enumerate(frames):
        print(f"[{i}] {f.url}")

    # Check for any element with 'map' in class/id
    map_els = page.locator("[class*='map' i], [id*='map' i]").all()
    print(f"\n--- Elements with 'map' in class/id ({len(map_els)}) ---")
    for i, el in enumerate(map_els):
        tag = el.evaluate("e => e.tagName")
        cls = el.get_attribute("class")
        visible = el.is_visible()
        print(f"[{i}] tag={tag} class={cls!r} visible={visible}")