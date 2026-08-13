class EarnestHomepageLocators:
    URL = "https://earnest.metrobank.com.ph/"

    # --- Hero & Introductory Section ---
    HERO_BANNER        = "role=img[name=/Earnest web banner/i]"
    HEADING_TRUSTED    = "role=heading[name=/Your trusted financial/i]"
    
    # --- Topic Cards (Manage, Grow, Protect) ---
    TOPIC_CARDS        = ".c-card-topic"
    TOPIC_NAMES        = ["Manage", "Grow", "Protect"]

    # --- Embedded Video ---
    VIDEO_FRAME        = 'iframe[title*="Moneygurado"]'
    VIDEO_OVERLAY      = "cued-overlay"
    BTN_PLAY           = "role=button[name='Play video']"
    BTN_PAUSE          = "role=button[name='Pause video']"

    # --- Feature Headings ---
    HEADING_TALK_MONEY = "role=heading[name=/Let’s talk about money/i]"
    HEADING_HANDS      = "role=heading[name=/A practical guide to navigate/i]"
    HEADING_INVEST     = "role=heading[name=/Ready to invest/i]"
    HEADING_ADVICE     = "role=heading[name=/Get trusted advice on/i]"

    # --- Call-to-Action Links ---
    LINK_EBOOK         = "role=link[name=/Get the Earnest E-book/i]"
    LINK_INVEST        = "role=link[name=/Explore Earnest Investing/i]"
    LINK_COMMUNITY     = "role=link[name=/Join the Earnest Community/i]"