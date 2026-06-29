"""
Locators for the Press page - momentgroup.ph/press
Only contains clickable/interactive elements.
"""


class PressLocators:

    # --- URLs ---
    BASE_URL  = "https://momentgroup.ph/"
    PRESS_URL = "https://momentgroup.ph/press/"

    # --- Navigation ---
    NAV_PRESS = "a:has-text('Press')"

    # --- Brand Filter Dropdown ---
    BRAND_FILTER = "role=combobox"

    # --- Press Section ---
    PRESS_HEADING = "#presspage__col1 >> role=heading[name='Press']"

    # --- Article Cards ---
    # Articles are plain <a> tags with target="_blank" linking to external press URLs
    # Scoped to #presspage__col1 to exclude header/footer social links (Facebook, Instagram, TikTok)
    ARTICLE_LINKS = "#presspage__col1 a[target='_blank'][href^='http']"

    # --- Contact Email ---
    EMAIL_PRESS = "a[href='mailto:press@momentgroup.ph']"