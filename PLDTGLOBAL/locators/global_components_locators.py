class GlobalLocators:

    URL = "https://www.pldtglobal.com/en"

    # --- Global Header ---
    HEADER_LOGO         = "header >> role=link[name='PLDT Global Corporation Logo']"
    LINK_HOME           = "header >> role=link[name='Home']"
    LINK_ABOUT          = "header >> role=link[name='About']"
    LINK_NEWS           = "header >> role=link[name='News & Insights']"
    LINK_CAREERS        = "header >> role=link[name='Careers']"
    BTN_SEARCH          = "header >> role=button[name='search button']"
    
    # FIX 1: Removed 'header >>' because this button exists outside the semantic <header> tag
    BTN_CONTACT_US      = "role=link[name=/contact us button/i]"

    # --- Cookie Banner (OneTrust) ---
    BANNER_TEXT         = "text=We use cookies and other tracking technologies"
    BTN_ACCEPT_ALL      = "role=button[name='Accept All Cookies']"
    BTN_PREFERENCES     = "role=button[name*='Preferences']"
    
    # Cookie Preference Center Modal
    MODAL_HEADING       = "role=heading[name='We Use Cookies']"
    
    # FIX 2: Use Regex (/.../i) to bypass OneTrust's hidden screen reader text (e.g., "Always Active")
    BTN_STRICTLY_NEC    = "role=button[name=/Strictly Necessary Cookies/i]"
    TEXT_STRICTLY_DESC  = "text=These cookies are necessary"
    BTN_FUNCTIONAL      = "role=button[name=/Functional Cookies/i]"
    TEXT_FUNCT_DESC     = "text=These cookies make your"
    BTN_PERFORMANCE     = "role=button[name=/Performance Cookies/i]"
    TEXT_PERF_DESC      = "text=We use these cookies to"
    BTN_TARGETING       = "role=button[name=/Targeting Cookies/i]"
    TEXT_TARGET_DESC    = "text=Based on your browsing"
    BTN_SAVE_PREFS      = "role=button[name='Save My Preferences']"

    # --- Global Footer ---
    FOOTER_LOGO         = "footer >> role=img[name='PLDT Global Corporation Logo']"
    FOOTER_HEADING      = "footer >> role=heading[name='Your Growth and Innovation Partner']"
    
    # Direct Contact & Socials
    LINK_EMAIL          = "footer >> role=link[name='askus@pldtglobal.com']"
    LINK_PHONE          = "footer >> role=link[name*='(+632)']"
    LINK_LINKEDIN       = "footer >> role=link[name='Follow us on Linkedin']"

    # Sitemap Dictionaries for iterative testing
    FOOTER_SITEMAP = {
        "Enterprise": [
            "footer >> role=link[name='Enterprise Solutions']",
            "footer >> role=link[name='Global Connectivity']",
            "footer >> role=link[name='Managed Network and Cloud']",
            "footer >> role=link[name='Edge and Security Solutions']",
            "footer >> role=link[name='Data Centers and Hyperscale']",
            "footer >> role=link[name='VORTEX']"
        ],
        "Consumer": [
            "footer >> role=link[name='Consumer Solutions']",
            "footer >> role=link[name='TinBo']",
            "footer >> role=link[name='ePadala']",
            "footer >> role=link[name='Smart Virtual Number']"
        ],
        "Carrier": [
            "footer >> role=link[name='Carrier']",
            "footer >> role=link[name='Wholesale Voice']"
        ],
        "Company": [
            "footer >> role=link[name='About']",
            "footer >> role=link[name='Careers']",
            "footer >> role=link[name='Contact Us']"
        ]
    }

    # Legal
    # Regex to handle dynamic years (e.g., © 2024, © 2026) without breaking tests
    TEXT_COPYRIGHT      = "text=/© \\d{4} PLDT Inc\\. All Rights Reserved/i"
    LINK_COOKIE_POL     = "footer >> role=link[name='Cookie Policy']"
    LINK_PRIVACY_POL    = "footer >> role=link[name='Privacy Policy']"