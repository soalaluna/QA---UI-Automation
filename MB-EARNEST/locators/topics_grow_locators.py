class TopicsGrowLocators:
    URL_GROW = "https://earnest.metrobank.com.ph/topics/grow"

    # --- Breadcrumbs & Navigation ---
    LINK_GO_BACK        = "role=link[name='Go Back']"
    LINK_TOPICS         = "role=link[name='Topics']"

    # --- Hero Section ---
    HEADING_HERO        = "role=heading[name=/Strengthen your financial/i]"
    TEXT_HERO_SUB       = "text=/Learn how to supplement your/i"
    TEXT_FAST_TRACK     = "text=/Fast track your way to your/i"

    # --- Articles Section ---
    # We use regex and generic links here so the test doesn't break when 
    # marketing swaps out the featured articles next week.
    LINK_READ_ALL       = "role=link[name=/Read all articles/i]"
    ARTICLE_LINKS       = ".c-card-article a" # Generic locator for article cards

    # --- Conversion Modules (E-book & Investing) ---
    HEADING_EBOOK       = "text=/Put Earnest in your pocket/i"
    TEXT_EBOOK_SUB      = "text=/All the practical personal/i"
    LINK_GET_EBOOK      = "role=link[name=/Get the Earnest E-book/i]"

    HEADING_INVEST      = "text=/Ready to invest/i"
    TEXT_INVEST_SUB     = "text=/Get the help you need every/i"
    LINK_EXPLORE_INVEST = "role=link[name=/Explore Earnest Investing/i]"