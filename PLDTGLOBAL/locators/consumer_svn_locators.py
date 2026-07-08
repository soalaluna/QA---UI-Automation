class PldtSvnLocators:

    SVN_URL = "https://www.pldtglobal.com/en/consumer/smart-virtual-number"

    # --- Nav / Breadcrumb ---
    LINK_CONSUMER          = "role=link[name='Consumer']"  # exact=True

    @staticmethod
    def span_smart_virtual_number(page):
        return page.locator("span").filter(has_text="Smart Virtual Number")

    # --- Page Content ---
    @staticmethod
    def heading_svn(page):
        return page.get_by_role("heading", name="Smart Virtual Number")

    TEXT_SVN_DESCRIPTION   = "text=Smart Virtual Number (SVN) is"
    LINK_LEARN_MORE        = "role=link[name='Learn More']"

    # --- Section Image (breadcrumb area) ---
    @staticmethod
    def section_breadcrumb_img(page):
        """
        Image scoped to the breadcrumb/back-navigation section.
        Uses .filter(has_text=...) to distinguish from other sections
        that may also contain images on the page.
        """
        return page.locator("section").filter(
            has_text="Back to ConsumerConsumerSmart"
        ).locator("img")