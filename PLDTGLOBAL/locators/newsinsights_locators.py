class NewsInsightsLocators:

    # --- URLs ---
    BASE_URL = "https://www.pldtglobal.com/en"
    NEWS_URL = "https://www.pldtglobal.com/en/news-and-insights"

    # --- Navigation ---
    NAV_NEWS_INSIGHTS = "role=link[name='News & Insights']"

    # --- Article Cards (generic, sample-based) ---
    BTN_READ_MORE_FIRST   = "role=button[name^='Read more article']"
    LINK_READ_ARTICLE_FIRST = "role=link[name^='Read article']"
    LINK_SHARE_FACEBOOK   = "role=link[name='Share on Facebook']"
    LINK_SHARE_LINKEDIN   = "role=link[name='Share on Linkedin']"
    LINK_EXPLORE          = "role=link[name='Explore']"

    # --- Pagination ---
    BTN_PAGE_2        = "role=button[name='Page 2']"
    BTN_PAGE_3        = "role=button[name='Page 3']"
    BTN_PAGE_4        = "role=button[name='Page 4']"
    BTN_PREV_PAGE     = "role=button[name='Previous Page']"
    BTN_NEXT_PAGE     = "role=button[name='Next Page']"

    # --- Category Filter Tabs ---
    TAB_NEWS_ARTICLES = "role=button[name='News Articles']"
    TAB_EVENTS        = "role=button[name='Events']"