
import re


class LoginLocators:

    LOGIN_URL = "https://hayop.atlas.kitchen/login"

    # --- Header / Nav ---
    LINK_HAYOP   = "role=link[name='Hayop']"
    BTN_ORDER_NOW = "role=button[name='Order now']"

    @staticmethod
    def path_nth_2(page):
        """Positional SVG path -- fragile, same caveat as signup_locators."""
        return page.locator("path").nth(2)

    # --- Login Page Content ---
    @staticmethod
    def heading_welcome_back(page):
        return page.get_by_role("heading", name="Welcome back")

    TEXT_LOG_IN_FASTER      = "text=Log in for faster checkouts,"
    TEXT_NO_ACCOUNT_YET     = "text=No account yet? Sign up here"
    INPUT_LABEL_TESTID      = "[data-testid='input-label']"

    @staticmethod
    def phone_country_select(page):
        return page.get_by_label("Phone number country")

    @staticmethod
    def phone_input(page):
        return page.get_by_role("textbox", name="Contact number")

    BTN_LOG_IN              = "role=button[name='Log in']"

    @staticmethod
    def div_or_divider(page):
        """
        The "or" divider between phone login and email login.
        Uses regex filter to avoid substring-matching other elements.
        """
        return page.locator("div").filter(has_text=re.compile(r"^or$")).first

    BTN_CONTINUE_EMAIL      = "role=button[name='Continue with email']"
    POWERED_BY_ATLAS        = "#poweredByAtlasId"

    # --- Links ---
    LINK_SIGN_UP_HERE       = "role=link[name='Sign up here']"