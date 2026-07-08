class PLDTDataCentersLocators:

    URL = "https://www.pldtglobal.com/en/enterprise/pgc-data-centers-and-hyperscale-integration"

    # --- Breadcrumbs ---
    # Using regex boundary matching to enforce an exact text match without strict-mode attributes
    LINK_ENTERPRISE    = "role=link[name=/^Enterprise$/]"
    TEXT_BREADCRUMB    = "span:has-text('Data Centers and Hyperscale')"

    # --- Hero & Content Section ---
    HEADING_MAIN       = "role=heading[name*='Data Centers and Hyperscale']"
    TEXT_HERO_DESC     = "text=Powered by the PLDT Group’s"
    LINK_LEARN_MORE    = "role=link[name='Learn More']"
    IMG_BACK_TO        = "section:has-text('Back to') >> img"