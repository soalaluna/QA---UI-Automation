class PressLocators:

    PRESS_URL            = "https://momentgroup.ph/press"

    # --- Layout & Static Elements ---
    # Using Regex for exact match to avoid Playwright CSS parser errors
    HEADING_COL1         = "#presspage__col1 >> role=heading[name=/^Press$/]"
    HEADING_COL2         = "#presspage__col2 >> role=heading[name='Press']"
    COMBOBOX_BRAND       = "role=combobox"
    
    # --- Contact Info ---
    HEADING_INQUIRIES    = "role=heading[name='Inquiries']"
    TEXT_INQUIRIES_DESC  = "text=For general corporate press"
    LINK_EMAIL           = "role=link[name='press@momentgroup.ph']"

    # --- Filter & Article Dictionary ---
    # Maps the dropdown option to a list of article link locators we expect to see
    # Using the '*=' (contains) operator to prevent truncation errors
    ARTICLES = {
        "All Brands": [ # Default view when the page loads
            "role=link[name*='May 2026 | PhilStar Life']",
            "role=link[name*='April 2026 | Metro.style']",
            "role=link[name*='March 2026 | Nikkei Asia']",
            "role=link[name*='February 2026 | Inquirer.net']"
        ],
        "Manam": [
            "role=link[name*='May 2026 | PhilStar Life']",
            "role=link[name*='November 2025 | The Post']"
        ],
        "Mama Nams": [
            "role=link[name*='October 2025 | Philippine']",
            "role=link[name*='March 2024 | Tatler Asia']",
            "role=link[name*='July 2023 | The Beat Manila']"
        ]
    }