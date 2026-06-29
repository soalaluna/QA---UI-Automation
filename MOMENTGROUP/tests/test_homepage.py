import pytest
from playwright.sync_api import Page, expect
from locators.homepage_locators import HomepageLocators

URL = "https://momentgroup.ph/"

DISABLE_ANIMATIONS = "*, *::before, *::after { animation: none !important; transition: none !important; opacity: 1 !important; visibility: visible !important; }"


def test_page_title(page: Page):
    """Page title should match 'Home | The Moment Group'"""
    page.goto(URL)
    expect(page).to_have_title("Home | The Moment Group")


def test_logo_visible(page: Page):
    """TMG logo should be visible on the page"""
    page.goto(URL)
    expect(page.locator(HomepageLocators.LOGO).first).to_be_visible()


def test_navigation_links_visible(page: Page):
    """All nav links should be present on the page"""
    page.goto(URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    expect(page.get_by_role("link", name="BRANDS").first).to_be_visible()
    expect(page.get_by_role("link", name="The Group").first).to_be_visible()
    expect(page.get_by_role("link", name="Press").first).to_be_visible()
    expect(page.get_by_role("link", name="Careers").first).to_be_visible()
    expect(page.get_by_role("link", name="Loyalty").first).to_be_visible()
    expect(page.get_by_role("link", name="Communications").first).to_be_visible()


def test_hero_tagline_visible(page: Page):
    """Hero tagline 'We are where you want to eat' should be visible"""
    page.goto(URL)
    page.add_style_tag(content=DISABLE_ANIMATIONS)
    expect(page.get_by_text("We are where you want to", exact=False).first).to_be_visible()


def test_social_media_links_visible(page: Page):
    """Facebook, Instagram, and TikTok links should be present"""
    page.goto(URL)
    expect(page.locator(HomepageLocators.SOCIAL_FACEBOOK).first).to_be_attached()
    expect(page.locator(HomepageLocators.SOCIAL_INSTAGRAM).first).to_be_attached()
    expect(page.locator(HomepageLocators.SOCIAL_TIKTOK).first).to_be_attached()


def test_brand_items_present(page: Page):
    """All brand links should be present in the brands section"""
    page.goto(URL)
    expect(page.locator(HomepageLocators.BRAND_HAYOP)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_MANAM)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_8CUTS)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_OOMA)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_DIN_TAI_FUNG)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_MO_COOKIES)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_THE_MESS_HALL)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_PANCIT)).to_be_attached()
    expect(page.locator(HomepageLocators.BRAND_MAMA_NAMS)).to_be_attached()