class Error404Locators:
    URL_404 = "https://earnest.metrobank.com.ph/this-page-definitely-does-not-exist"

    # --- 404 Specific Elements (Split into actual DOM elements) ---
    HEADING_404         = "role=heading[name='Error 404']"
    HEADING_SOMETHING   = "role=heading[name='Something went wrong']"
    BTN_BACK_HOME       = "role=link[name='Back to Homepage']"
