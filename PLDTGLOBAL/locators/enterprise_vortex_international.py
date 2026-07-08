class EnterpriseVortexInternationalLocators:

    URL = "https://www.pldtglobal.com/en/enterprise/pgc-vortex-international"

    # --- Breadcrumbs ---
    # Using regex boundary matching to enforce an exact text match safely
    LINK_ENTERPRISE    = "role=link[name=/^Enterprise$/]"
    TEXT_BREADCRUMB    = "#main >> text='VORTEX'"

    # --- Hero & Content Section ---
    HEADING_MAIN       = "role=heading[name*='VORTEX powered by PLDT Global']"
    TEXT_HERO_DESC     = "text=VORTEX is part of the PLDT"
    LINK_LEARN_MORE    = "role=link[name='Learn More']"
    IMG_BACK_TO        = "section:has-text('Back to') >> img"