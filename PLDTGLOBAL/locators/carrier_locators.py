import re


class PldtCarrierLocators:

    CARRIER_URL = "https://www.pldtglobal.com/en/carrier"

    # --- Hero Section ---
    @staticmethod
    def heading_carrier_grade(page):
        return page.get_by_role("heading", name="Carrier-Grade Connectivity")

    TEXT_RELIABLE_VOICE    = "text=Reliable international voice"
    LINK_LEARN_MORE        = "role=link[name='Learn More']"  # use .first in tests

    # --- Built for Global Carrier Section ---
    IMG_BUILT_FOR_GLOBAL = "role=img[name*='Built for Global Carrier']"
    OVERLAY_TOP_LEFT       = ".absolute.top-0.left-0"        # use .first in tests

    @staticmethod
    def heading_carrier_exact(page):
        return page.get_by_role("heading", name="carrier", exact=True)

    # --- Carrier Solutions Portfolio ---
    @staticmethod
    def heading_carrier_solutions(page):
        return page.get_by_role("heading", name="Carrier Solutions Portfolio")

    TEXT_FOCUSED_SUITE     = "text=A focused suite of"

    @staticmethod
    def section_carrier_img(page):
        """Image scoped to the Carrier Solutions section via has_text filter."""
        return page.locator("section").filter(
            has_text="carrierCarrier Solutions"
        ).locator("img")

    # --- Wholesale Voice ---
    @staticmethod
    def heading_wholesale_voice(page):
        return page.get_by_role("heading", name="Wholesale Voice")

    TEXT_HIGH_QUALITY      = "text=High-quality international"

    @staticmethod
    def link_learn_more_exact(page):
        """
        'Learn More' link matched by exact full text using regex.
        Distinguishes from partial-text matches on the same page.
        """
        return page.locator("a").filter(has_text=re.compile(r"^Learn More$"))

    @staticmethod
    def div_nth_5(page):
        """
        CAUTION: positional div selector — fragile, may shift if page
        layout changes. Codegen recorded this as a tab/section toggle.
        Replace with a stable locator if one becomes available.
        """
        return page.locator("div").nth(5)