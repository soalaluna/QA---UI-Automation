import re
import pytest
from playwright.sync_api import Page, expect
from locators.error_404_locators import Error404Locators as E404


@pytest.fixture(autouse=True)
def navigate_to_404(page: Page):
    max_retries = 3
    for i in range(max_retries):
        try:
            page.goto(E404.URL_404, wait_until="domcontentloaded", timeout=60000)
            break
        except Exception as e:
            if i == max_retries - 1:
                raise e
            page.wait_for_timeout(3000)
    yield


class TestEarnest404Page:

    def test_404_status_and_ui_visible(self, page: Page):
        response = page.goto(E404.URL_404)
        
        assert response.status == 404, f"Expected network status 404, got {response.status}"
        
        # Fixed: Asserting both headings independently
        expect(page.locator(E404.HEADING_404)).to_be_visible()
        expect(page.locator(E404.HEADING_SOMETHING)).to_be_visible()
        expect(page.locator(E404.BTN_BACK_HOME)).to_be_visible()

    def test_rescue_button_routes_to_home(self, page: Page):
        page.locator(E404.BTN_BACK_HOME).click()
        expect(page).to_have_url("https://earnest.metrobank.com.ph/")