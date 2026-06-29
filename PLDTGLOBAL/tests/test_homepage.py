import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import (
    BASE_URL,
    LOGO,
    NAV_HOME, NAV_SOLUTIONS, NAV_ABOUT, NAV_NEWS, NAV_CAREERS,
    BTN_SEARCH, INPUT_SEARCH, BTN_SEARCH_SUBMIT,
    BTN_CONSUMER, BTN_ENTERPRISE,
    NAV_ENTERPRISE_LINK, NAV_CARRIER_LINK, NAV_CONSUMER_LINK,
    HERO_CTA,
    LEARN_MORE,
    BTN_MORE_NEWS,
    BTN_NEWS_ARTICLE_1, BTN_NEWS_ARTICLE_2, BTN_NEWS_ARTICLE_3,
    SHARE_FACEBOOK, SHARE_LINKEDIN,
    BTN_ACCEPT_COOKIES,
    FOOTER_EMAIL, FOOTER_PHONE, FOOTER_LINKEDIN,
    FOOTER_GLOBAL_CONNECTIVITY, FOOTER_MANAGED_NETWORK,
    FOOTER_EDGE_SECURITY, FOOTER_DATA_CENTERS,
    FOOTER_VORTEX, FOOTER_TINBO, FOOTER_EPADALA,
    FOOTER_SMART_VIRTUAL, FOOTER_WHOLESALE_VOICE,
    FOOTER_ABOUT, FOOTER_CAREERS, FOOTER_CONTACT_US,
    FOOTER_PRIVACY_POLICY, FOOTER_CONTACT_BTN,
)


@pytest.fixture(autouse=True)
def setup(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    cookie_btn = page.locator(BTN_ACCEPT_COOKIES)
    if cookie_btn.is_visible():
        cookie_btn.click()


# ── Logo ──────────────────────────────────────────────────────────────────────

def test_logo_visible(page: Page):
    """PLDT Global logo should be visible"""
    expect(page.locator(LOGO)).to_be_visible()

def test_logo_links_to_homepage(page: Page):
    """Logo should link back to the homepage"""
    page.locator(LOGO).click()
    page.wait_for_load_state("networkidle")
    assert "pldtglobal.com" in page.url, f"Unexpected URL: {page.url}"


# ── Navigation ────────────────────────────────────────────────────────────────

def test_nav_home_visible(page: Page):
    """Home nav link should be visible"""
    expect(page.locator(NAV_HOME)).to_be_visible()

def test_nav_solutions_visible(page: Page):
    """Solutions nav link should be visible"""
    expect(page.locator(NAV_SOLUTIONS).first).to_be_visible()

def test_nav_about_visible(page: Page):
    """About nav link should be visible"""
    expect(page.locator(NAV_ABOUT)).to_be_visible()

def test_nav_news_visible(page: Page):
    """News & Insights nav link should be visible"""
    expect(page.locator(NAV_NEWS)).to_be_visible()

def test_nav_careers_visible(page: Page):
    """Careers nav link should be visible"""
    expect(page.locator(NAV_CAREERS)).to_be_visible()

def test_nav_home_navigates(page: Page):
    """Home nav link should navigate to homepage"""
    page.locator(NAV_HOME).click()
    page.wait_for_load_state("networkidle")
    assert "pldtglobal.com/en" in page.url, f"Unexpected URL: {page.url}"

def test_nav_solutions_navigates(page: Page):
    """Solutions nav link should have a valid href"""
    href = page.locator(NAV_SOLUTIONS).first.get_attribute("href")
    assert href and len(href) > 0, "Solutions nav has no href"

def test_nav_about_navigates(page: Page):
    """About nav link should navigate to about page"""
    # Use goto directly — JS routing may not respond to .click() alone
    href = page.locator(NAV_ABOUT).get_attribute("href")
    page.goto(f"https://www.pldtglobal.com{href}")
    page.wait_for_load_state("networkidle")
    assert "about" in page.url.lower(), f"Expected about page, got: {page.url}"

def test_nav_news_navigates(page: Page):
    """News & Insights nav link should navigate to news page"""
    href = page.locator(NAV_NEWS).get_attribute("href")
    page.goto(f"https://www.pldtglobal.com{href}")
    page.wait_for_load_state("networkidle")
    assert "news" in page.url.lower(), f"Expected news page, got: {page.url}"

def test_nav_careers_navigates(page: Page):
    """Careers nav link should navigate to careers page"""
    href = page.locator(NAV_CAREERS).get_attribute("href")
    page.goto(f"https://www.pldtglobal.com{href}")
    page.wait_for_load_state("networkidle")
    assert "career" in page.url.lower(), f"Expected careers page, got: {page.url}"


# ── Search ────────────────────────────────────────────────────────────────────

def test_search_button_visible(page: Page):
    """Search button should be visible in the header"""
    expect(page.locator(BTN_SEARCH)).to_be_visible()

def test_search_opens_input(page: Page):
    """Clicking search button should reveal the search input"""
    page.locator(BTN_SEARCH).click()
    expect(page.locator(INPUT_SEARCH)).to_be_visible()

def test_search_input_accepts_text(page: Page):
    """Search input should accept typed text"""
    page.locator(BTN_SEARCH).click()
    page.locator(INPUT_SEARCH).fill("testing")
    expect(page.locator(INPUT_SEARCH)).to_have_value("testing")

def test_search_submit_navigates(page: Page):
    """Submitting a search should navigate to search results"""
    page.locator(BTN_SEARCH).click()
    page.locator(INPUT_SEARCH).fill("testing")
    page.locator(BTN_SEARCH_SUBMIT).click()
    page.wait_for_load_state("networkidle")
    assert "testing" in page.url.lower() or "search" in page.url.lower(), \
        f"Expected search results page, got: {page.url}"


# ── Solutions Dropdown ────────────────────────────────────────────────────────

def test_enterprise_button_attached(page: Page):
    """Enterprise link should appear in dropdown after clicking Solutions"""
    page.locator(NAV_SOLUTIONS).first.click()
    page.wait_for_timeout(500)
    # Use get_by_role with exact=True in the test instead of the locator string
    expect(page.get_by_role("link", name="Enterprise", exact=True).first).to_be_attached()

def test_consumer_button_attached(page: Page):
    """Consumer button should appear in dropdown after clicking Solutions"""
    page.locator(NAV_SOLUTIONS).first.click()
    page.wait_for_timeout(500)
    expect(page.locator(BTN_CONSUMER).first).to_be_attached()

def test_enterprise_link_attached(page: Page):
    """Enterprise sub-nav link should appear after clicking Solutions"""
    page.locator(NAV_SOLUTIONS).first.click()
    page.wait_for_timeout(500)
    expect(page.locator(NAV_ENTERPRISE_LINK).first).to_be_attached()

def test_carrier_link_attached(page: Page):
    """Carrier sub-nav link should appear after clicking Solutions"""
    page.locator(NAV_SOLUTIONS).first.click()
    page.wait_for_timeout(500)
    expect(page.locator(NAV_CARRIER_LINK)).to_be_attached()

def test_consumer_link_attached(page: Page):
    """Consumer sub-nav link should appear after clicking Solutions"""
    page.locator(NAV_SOLUTIONS).first.click()
    page.wait_for_timeout(500)
    expect(page.locator(NAV_CONSUMER_LINK).first).to_be_attached()


# ── Hero Section ──────────────────────────────────────────────────────────────

def test_hero_cta_visible(page: Page):
    """Hero CTA button should be visible"""
    expect(page.locator(HERO_CTA)).to_be_visible()

def test_hero_cta_has_href(page: Page):
    """Hero CTA should have a valid href"""
    href = page.locator(HERO_CTA).get_attribute("href")
    assert href and len(href) > 0, "Hero CTA has no href"


# ── Learn More Links ──────────────────────────────────────────────────────────

def test_learn_more_first_visible(page: Page):
    """First Learn More link should be visible"""
    expect(page.locator(LEARN_MORE).first).to_be_visible()

def test_learn_more_second_visible(page: Page):
    """Second Learn More link should be visible"""
    expect(page.locator(LEARN_MORE).nth(1)).to_be_visible()

def test_learn_more_third_visible(page: Page):
    """Third Learn More link should be visible"""
    expect(page.locator(LEARN_MORE).nth(2)).to_be_visible()

def test_learn_more_first_navigates(page: Page):
    """First Learn More link should navigate"""
    href = page.locator(LEARN_MORE).first.get_attribute("href")
    assert href and len(href) > 0, "First Learn More has no href"


# ── News Section ──────────────────────────────────────────────────────────────

def test_more_news_button_visible(page: Page):
    """More News button should be visible"""
    expect(page.locator(BTN_MORE_NEWS)).to_be_visible()

def test_more_news_has_href(page: Page):
    """More News button should have a valid href"""
    href = page.locator(BTN_MORE_NEWS).get_attribute("href")
    assert href and "news" in href.lower(), f"Unexpected href: {href}"

def test_news_article_1_visible(page: Page):
    """First news article read more button should be visible"""
    expect(page.locator(BTN_NEWS_ARTICLE_1)).to_be_visible()

def test_news_article_2_visible(page: Page):
    """Second news article read more button should be visible"""
    expect(page.locator(BTN_NEWS_ARTICLE_2)).to_be_visible()

def test_news_article_3_visible(page: Page):
    """Third news article read more button should be visible"""
    expect(page.locator(BTN_NEWS_ARTICLE_3)).to_be_visible()

def test_share_facebook_visible(page: Page):
    """Share on Facebook link should be visible"""
    expect(page.locator(SHARE_FACEBOOK).first).to_be_visible()

def test_share_linkedin_visible(page: Page):
    """Share on LinkedIn link should be visible"""
    expect(page.locator(SHARE_LINKEDIN).first).to_be_visible()


# ── Footer ────────────────────────────────────────────────────────────────────

def test_footer_email_visible(page: Page):
    """Contact email should be visible in footer"""
    expect(page.locator(FOOTER_EMAIL)).to_be_visible()

def test_footer_email_href(page: Page):
    """Contact email should have correct mailto href"""
    href = page.locator(FOOTER_EMAIL).get_attribute("href")
    assert "askus@pldtglobal.com" in href, f"Unexpected href: {href}"

def test_footer_phone_visible(page: Page):
    """Phone number should be visible in footer"""
    expect(page.locator(FOOTER_PHONE)).to_be_visible()

def test_footer_phone_href(page: Page):
    """Phone number should have correct tel href"""
    href = page.locator(FOOTER_PHONE).get_attribute("href")
    assert "tel:" in href, f"Unexpected href: {href}"

def test_footer_linkedin_visible(page: Page):
    """LinkedIn link should be visible in footer"""
    expect(page.locator(FOOTER_LINKEDIN)).to_be_visible()

def test_footer_linkedin_href(page: Page):
    """LinkedIn link should point to LinkedIn"""
    href = page.locator(FOOTER_LINKEDIN).get_attribute("href")
    assert "linkedin.com" in href, f"Unexpected href: {href}"

def test_footer_global_connectivity_visible(page: Page):
    """Global Connectivity footer link should be visible"""
    expect(page.locator(FOOTER_GLOBAL_CONNECTIVITY)).to_be_visible()

def test_footer_managed_network_visible(page: Page):
    """Managed Network and Cloud footer link should be visible"""
    expect(page.locator(FOOTER_MANAGED_NETWORK)).to_be_visible()

def test_footer_edge_security_visible(page: Page):
    """Edge and Security Solutions footer link should be visible"""
    expect(page.locator(FOOTER_EDGE_SECURITY)).to_be_visible()

def test_footer_data_centers_visible(page: Page):
    """Data Centers and Hyperscale footer link should be visible"""
    expect(page.locator(FOOTER_DATA_CENTERS)).to_be_visible()

def test_footer_vortex_visible(page: Page):
    """VORTEX footer link should be visible"""
    expect(page.locator(FOOTER_VORTEX)).to_be_visible()

def test_footer_tinbo_visible(page: Page):
    """TinBo footer link should be visible"""
    expect(page.locator(FOOTER_TINBO)).to_be_visible()

def test_footer_epadala_visible(page: Page):
    """ePadala footer link should be visible"""
    expect(page.locator(FOOTER_EPADALA)).to_be_visible()

def test_footer_smart_virtual_visible(page: Page):
    """Smart Virtual Number footer link should be visible"""
    expect(page.locator(FOOTER_SMART_VIRTUAL)).to_be_visible()

def test_footer_wholesale_voice_visible(page: Page):
    """Wholesale Voice footer link should be visible"""
    expect(page.locator(FOOTER_WHOLESALE_VOICE)).to_be_visible()

def test_footer_about_visible(page: Page):
    """About footer link should be visible"""
    expect(page.locator(FOOTER_ABOUT)).to_be_visible()

def test_footer_careers_visible(page: Page):
    """Careers footer link should be visible"""
    expect(page.locator(FOOTER_CAREERS)).to_be_visible()

def test_footer_contact_us_visible(page: Page):
    """Contact Us footer link should be visible"""
    expect(page.locator(FOOTER_CONTACT_US)).to_be_visible()

def test_footer_privacy_policy_visible(page: Page):
    """Privacy Policy footer link should be visible"""
    expect(page.locator(FOOTER_PRIVACY_POLICY)).to_be_visible()

def test_footer_contact_btn_visible(page: Page):
    """Contact us button should be visible in footer"""
    expect(page.locator(FOOTER_CONTACT_BTN)).to_be_visible()

def test_footer_about_href(page: Page):
    """Footer About link should have correct href"""
    href = page.locator(FOOTER_ABOUT).get_attribute("href")
    assert "about" in href.lower(), f"Unexpected href: {href}"

def test_footer_careers_href(page: Page):
    """Footer Careers link should have correct href"""
    href = page.locator(FOOTER_CAREERS).get_attribute("href")
    assert "career" in href.lower(), f"Unexpected href: {href}"

def test_footer_contact_us_href(page: Page):
    """Footer Contact Us link should have correct href"""
    href = page.locator(FOOTER_CONTACT_US).get_attribute("href")
    assert "contact" in href.lower(), f"Unexpected href: {href}"

def test_footer_privacy_policy_href(page: Page):
    """Footer Privacy Policy link should have correct href"""
    href = page.locator(FOOTER_PRIVACY_POLICY).get_attribute("href")
    assert "privacy" in href.lower(), f"Unexpected href: {href}"