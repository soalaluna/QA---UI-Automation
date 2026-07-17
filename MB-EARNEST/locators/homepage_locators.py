class HomepageLocators:

    URL = "https://earnest.metrobank.com.ph/"

    # --- Header Navigation ---
    # Using Regex to ignore dynamic dates/versions in the logo alt text
    LOGO_MAIN            = "role=link[name=/MB-YIGH-logo/i]"
    NAV_EXPLORE          = "role=link[name='Explore Topics']"
    NAV_EBOOK            = "role=link[name='Download E-book']"
    NAV_MONEYGURADO      = "role=link[name='Moneygurado']"
    NAV_HANDS            = "role=link[name='H.A.N.D.S.']"

    # --- Hero & Top Banners ---
    # Regex prevents breaking when marketing changes the banner filename month-to-month
    HERO_BANNER_IMG      = "role=img[name=/Earnest web banner/i]"
    HERO_HEADING         = "role=heading[name=/Your trusted financial/i]"
    MONEYGURADO_BANNER   = "text=/Pagdating sa pera, moneygurado muna/i"

    # --- Earnest Learning Topics ---
    HEADING_LEARNING     = "text=Earnest Learning"
    TOPIC_MANAGE_HEADING = "role=heading[name='Manage']"
    TOPIC_MANAGE_ICON    = "role=img[name=/icons MANAGE/i]"
    TOPIC_GROW_HEADING   = "role=heading[name='Grow']"
    TOPIC_GROW_ICON      = "role=img[name=/icons GROW/i]"
    TOPIC_PROTECT_HEADING= "role=heading[name='Protect']"
    TOPIC_PROTECT_ICON   = "role=img[name=/icons PROTECT/i]"
    
    # Standardizing the Learn More buttons to avoid brittle auto-generated IDs
    BTN_LEARN_MORE       = "role=link[name='Learn More']"

    # --- Video Player ---
    IFRAME_VIDEO         = "iframe[title*='Moneygurado']"
    BTN_PLAY_VIDEO       = "role=button[name='Play video']"

    # --- Articles & Resources ---
    HEADING_MONEY_TALK   = "role=heading[name='Let’s talk about money']"
    HEADING_EBOOK        = "role=heading[name='Put Earnest in your pocket']"
    BTN_GET_EBOOK        = "role=link[name='Get the Earnest E-book']"
    
    IMG_HANDS            = "role=img[name=/HANDS Web article/i]"
    HEADING_HANDS        = "role=heading[name=/A practical guide to navigate/i]"

    # --- Bottom CTAs ---
    HEADING_INVEST       = "role=heading[name='Ready to invest?']"
    LINK_INVEST          = "role=link[name='Explore Earnest Investing']"
    HEADING_COMMUNITY    = "role=heading[name='Get trusted advice on']"
    LINK_COMMUNITY       = "role=link[name='Join the Earnest Community']"

    # --- Footer ---
    TEXT_PRESENTED_BY    = "contentinfo >> text=Presented by:"
    IMG_MB_LOGO_FOOTER   = "role=link[name=/option-2/i]"
    LINK_VISIT_MB        = "role=link[name='Visit Metrobank site']"
    
    TEXT_INQUIRIES       = "contentinfo >> text=For inquiries, please call"
    LINK_BSP             = "role=link[name='www.bsp.gov.ph']"
    TEXT_PDIC            = "contentinfo >> text=Deposits are insured by PDIC"
    
    SEAL_DPO             = "role=img[name='DPO Seal']"
    SEAL_PDIC            = "role=img[name='PDIC Seal']"
    SEAL_BIR             = "role=img[name='BIR Seal']"
    
    # Regex handles the copyright year changing automatically
    TEXT_COPYRIGHT       = "text=/©\\d{4} Metrobank. All Rights Reserved/i"
    LINK_SIGN_UP         = "role=link[name='Sign up to Stay Informed']"

    # Social Media List
    SOCIAL_LINKS         = ".social-item > li > a"