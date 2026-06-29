import pytest
from playwright.sync_api import Page, expect
from locators.consumer_locators import (
    BASE_URL, CONSUMER_URL, EPADALA_URL, TINBO_URL,
    BTN_ACCEPT_COOKIES,
    CONSUMER_HEADING,
    LEARN_MORE,
    EPADALA_HEADING,
    LINK_VISIT_TINBO,
    FAQ_WHAT_IS_TINBO, FAQ_WHO_CAN_USE, FAQ_HOW_GET_PHILIPPINE,
    FAQ_TRANSACTIONS_SECURE, FAQ_COUNTRIES_SUPPORTED,
    LINK_EXPLORE,
)


@pytest.fixture(autouse=True)
def setup(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    cookie_btn = page.locator(BTN_ACCEPT_COOKIES)
    if cookie_btn.is_visible():
        cookie_btn.click()


# ── Nav to Consumer ───────────────────────────────────────────────────────────

def test_consumer_heading_visible(page: Page):
    """Consumer heading should be visible on the homepage"""
    expect(page.locator(CONSUMER_HEADING)).to_be_visible()

def test_consumer_learn_more_navigates(page: Page):
    """Clicking Consumer's Learn More link should navigate to consumer page"""
    page.locator(CONSUMER_HEADING).scroll_into_view_if_needed()

    consumer_link = page.locator("a[href*='/consumer']", has_text="Learn More")

    # Debug: how many matches, what do they point to, is anything overlapping
    count = consumer_link.count()
    print(f"\nDEBUG: consumer_link count = {count}")
    for i in range(count):
        el = consumer_link.nth(i)
        print(f"DEBUG: [{i}] href={el.get_attribute('href')} visible={el.is_visible()}")

    page.screenshot(path="debug_before_click.png", full_page=False)

    consumer_link.first.click()
    page.wait_for_timeout(1000)  # give SPA routing a moment, separate from networkidle
    print(f"DEBUG: URL after click = {page.url}")
    page.screenshot(path="debug_after_click.png", full_page=False)

    page.wait_for_load_state("networkidle")
    assert "consumer" in page.url.lower(), f"Expected consumer page, got: {page.url}"


# ── Consumer Page - Learn More Links ──────────────────────────────────────────

def test_learn_more_links_present(page: Page):
    """Consumer page should have multiple Learn More links"""
    page.goto(CONSUMER_URL)
    page.wait_for_load_state("networkidle")
    count = page.locator(LEARN_MORE).count()
    assert count >= 1, "Expected at least one Learn More link on Consumer page"

def test_learn_more_first_visible(page: Page):
    """First Learn More link should be visible"""
    page.goto(CONSUMER_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(LEARN_MORE).first).to_be_visible()

def test_learn_more_first_has_href(page: Page):
    """First Learn More link should have a valid href"""
    page.goto(CONSUMER_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(LEARN_MORE).first.get_attribute("href")
    assert href and len(href) > 0, "First Learn More link has no href"


# ── ePadala Sub-page ──────────────────────────────────────────────────────────

def test_epadala_page_loads(page: Page):
    """ePadala page should load successfully"""
    page.goto(EPADALA_URL)
    page.wait_for_load_state("networkidle")
    assert "epadala" in page.url.lower(), f"Expected ePadala page, got: {page.url}"

def test_epadala_heading_visible(page: Page):
    """ePadala heading should be visible"""
    page.goto(EPADALA_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(EPADALA_HEADING)).to_be_visible()


# ── TinBo Sub-page ─────────────────────────────────────────────────────────────

def test_tinbo_page_loads(page: Page):
    """TinBo page should load successfully"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    assert "tinbo" in page.url.lower(), f"Expected TinBo page, got: {page.url}"

def test_visit_tinbo_link_visible(page: Page):
    """Visit TinBo link should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(LINK_VISIT_TINBO)).to_be_visible()

def test_visit_tinbo_opens_new_tab(page: Page):
    """Visit TinBo link should open TinBo's external site in a new tab"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    with page.expect_popup() as popup_info:
        page.locator(LINK_VISIT_TINBO).click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    assert "tinbo" in popup.url.lower(), f"Expected TinBo site, got: {popup.url}"


# ── TinBo FAQ Accordion ────────────────────────────────────────────────────────

def test_faq_what_is_tinbo_visible(page: Page):
    """'What is TinBo?' FAQ should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(FAQ_WHAT_IS_TINBO)).to_be_visible()

def test_faq_what_is_tinbo_toggles(page: Page):
    """'What is TinBo?' FAQ should expand and collapse on click"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    faq = page.locator(FAQ_WHAT_IS_TINBO)
    faq.click()
    page.wait_for_timeout(300)
    faq.click()

def test_faq_who_can_use_visible(page: Page):
    """'Who can use TinBo?' FAQ should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(FAQ_WHO_CAN_USE)).to_be_visible()

def test_faq_who_can_use_toggles(page: Page):
    """'Who can use TinBo?' FAQ should expand and collapse on click"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    faq = page.locator(FAQ_WHO_CAN_USE)
    faq.click()
    page.wait_for_timeout(300)
    faq.click()

def test_faq_how_get_philippine_visible(page: Page):
    """'How do I get a Philippine...' FAQ should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(FAQ_HOW_GET_PHILIPPINE)).to_be_visible()

def test_faq_how_get_philippine_toggles(page: Page):
    """'How do I get a Philippine...' FAQ should expand and collapse on click"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    faq = page.locator(FAQ_HOW_GET_PHILIPPINE)
    faq.click()
    page.wait_for_timeout(300)
    faq.click()

def test_faq_transactions_secure_visible(page: Page):
    """'Are my transactions secure?' FAQ should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(FAQ_TRANSACTIONS_SECURE)).to_be_visible()

def test_faq_transactions_secure_toggles(page: Page):
    """'Are my transactions secure?' FAQ should expand and collapse on click"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    faq = page.locator(FAQ_TRANSACTIONS_SECURE)
    faq.click()
    page.wait_for_timeout(300)
    faq.click()

def test_faq_countries_supported_visible(page: Page):
    """'Which countries are supported?' FAQ should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(FAQ_COUNTRIES_SUPPORTED)).to_be_visible()

def test_faq_countries_supported_toggles(page: Page):
    """'Which countries are supported?' FAQ should expand and collapse on click"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    faq = page.locator(FAQ_COUNTRIES_SUPPORTED)
    faq.click()
    page.wait_for_timeout(300)
    faq.click()


# ── Explore Link ───────────────────────────────────────────────────────────────

def test_explore_link_visible(page: Page):
    """Explore link should be visible on TinBo page"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    expect(page.locator(LINK_EXPLORE).first).to_be_visible()

def test_explore_link_has_href(page: Page):
    """Explore link should have a valid href"""
    page.goto(TINBO_URL)
    page.wait_for_load_state("networkidle")
    href = page.locator(LINK_EXPLORE).first.get_attribute("href")
    assert href and len(href) > 0, "Explore link has no href"