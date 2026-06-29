class AboutLocators:
    BASE_URL    = "https://hayopnimanam.com/"
    ABOUT_URL   = "https://hayopnimanam.com/who-we-are/"

    # --- Navigation ---
    NAV_ABOUT           = "nav a:has-text('ABOUT')"

    # --- About Page Tabs ---
    # Tabs are plain text labels (lowercase): hayop / about us / the moment group / our founders / partners / about singapore
    TAB_MOMENT_GROUP    = "text='the moment group'"
    TAB_PARTNERS        = "text='partners'"

    # --- Footer ---
    FOOTER_INSTAGRAM    = "a[href='https://www.instagram.com/hayop.sg']"
    FOOTER_PRIVACY      = "a[href='https://hayopnimanam.com/privacy-policy/']"
    FOOTER_TERMS        = "a[href='https://hayopnimanam.com/terms-conditions/']"