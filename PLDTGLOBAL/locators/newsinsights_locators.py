class NewsInsightsLocators:

    URL = "https://www.pldtglobal.com/en/news-and-insights"

    # --- Hero Section ---
    HEADING_SUB         = "h3:has-text('News & Insights')"
    HEADING_MAIN        = "role=heading[name*='News and Insights from PLDT']"
    TEXT_HERO_DESC      = "text=Stay updated with official"
    IMG_HERO            = "role=img[name*='/uploads/']"

    # --- Filter Tabs & Grid Header ---
    HEADING_GRID        = "h2:has-text('News & Insights')"
    TAB_ALL             = "role=button[name=/^All$/]"  # Using regex to ensure exact match without syntax errors
    TAB_NEWS            = "role=button[name='News Articles']"
    TAB_EVENTS          = "role=button[name='Events']"

    # --- Sample Article Card (First card on the grid) ---
    # We use nth=0 so the test doesn't fail on strict-mode violations when multiple cards exist
    LINK_ARTICLE        = "role=link[name*='PLDT Global Joins Community Effort'] >> nth=0"
    BTN_READ_MORE       = "role=button[name*='Read more article'] >> nth=0"
    TEXT_SHARE_TO       = "text=Share to >> nth=0"
    BTN_SHARE_FB        = "role=link[name='Share on Facebook'] >> nth=0"
    BTN_SHARE_LI        = "role=link[name='Share on Linkedin'] >> nth=0"

    # --- Pagination ---
    TEXT_PAGINATION     = "text=1234"
    BTN_PAGE_2          = "role=button[name='Page 2']"
    BTN_PAGE_3          = "role=button[name='Page 3']"
    BTN_PAGE_4          = "role=button[name='Page 4']"
    BTN_NEXT_PAGE       = "role=button[name='Next Page']"

    # --- Explore Solutions (Footer Section) ---
    HEADING_EXPLORE     = "role=heading[name='Explore Our Solutions']"
    TEXT_EXPLORE_DESC   = "text=Explore our offerings to"

    # Dictionary for parameterized testing of the bottom cards
    SOLUTIONS = {
        "Enterprise": {
            "desc": "role=paragraph >> text=Experience our carrier-",
            "btn": "role=link[name='Explore'] >> nth=0"
        },
        "Carrier": {
            "desc": "role=paragraph >> text=Our data center offers a",
            "btn": "role=link[name='Explore'] >> nth=1"
        },
        "Consumer": {
            "desc": "role=paragraph >> text=Expand your business by",
            "btn": "role=link[name='Explore'] >> nth=2"
        }
    }