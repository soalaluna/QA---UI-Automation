class TinboLocators:

    URL = "https://www.pldtglobal.com/en/consumer/tinbo"

    # --- Breadcrumbs ---
    LINK_CONSUMER       = "role=link[name=/^Consumer$/i]"
    TEXT_BREADCRUMB     = "text=Tinbo >> nth=0"

    # --- Hero Section ---
    HEADING_MAIN        = "role=heading[name=/^TinBo$/]"
    TEXT_HERO_DESC      = "text=Your one-stop digital shop for global Filipinos"
    BTN_VISIT_TINBO     = "role=link[name='Visit TinBo']"

    # --- Key Stats Section ---
    TEXT_STATS_500K     = "text=500k + Downloads"
    TEXT_STATS_100      = "text=100+ Countries"
    TEXT_STATS_MINS     = "text=minutes"

    # --- Features Section ---
    HEADING_FEATURES    = "h2:has-text('Key Features')"
    TEXT_FEATURES_DESC  = "role=paragraph >> text=With TinBo, you’re never far"

    FEATURES = {
        "ePadala": "text=TinBo ePadala",
        "Load Padala": "text=Load Padala to the Philippines",
        "Shopping & Food": "text=Shopping, food, health & >> nth=0",
        "Prepaid Load": "role=listitem >> text=Prepaid load service for"
    }

    # --- Industry Application Section ---
    HEADING_INDUSTRY    = "role=heading[name='Industry Application']"
    TEXT_INDUSTRY_DESC  = "text=TinBo helps industries extend"
    
    # We use nth=0 for the Financial Services heading to avoid matching the image alt text
    HEADING_FINANCIAL   = "role=heading[name='Financial Services'] >> nth=0"
    TEXT_FINANCIAL      = "role=paragraph >> text=Ensure secure, real-time"
    HEADING_BPO         = "role=heading[name='BPO & Contact Centers']"
    TEXT_BPO            = "role=paragraph >> text=Support high-volume"
    IMG_INDUSTRY        = "role=img[name='Financial Services']"

    # --- Partners Section ---
    HEADING_PARTNERS    = "role=heading[name='Powered by trusted networks']"
    TEXT_PARTNERS_DESC  = "text=TinBo works hand-in-hand with"
    PARTNER_CAROUSEL    = ".swiper-horizontal"

    # --- FAQ Section ---
    HEADING_FAQ         = "role=heading[name='FAQ’s']"
    TEXT_FAQ_DESC       = "text=Find helpful information and"
    
    # Using a dictionary to map each FAQ question button
    FAQS = {
        "What is TinBo": "role=button[name='What is TinBo?']",
        "Who can use": "role=button[name='Who can use TinBo?']",
        # Update: Match the exact name from the error log DOM
        "How do I get number": "role=button[name='How do I get a Philippine virtual number?']",
        "Are transactions secure": "role=button[name='Are my transactions secure?']",
        "Supported countries": "role=button[name='Which countries are supported?']"
    }
    
    # The answer text that expands (The codegen saw the exact same answer duplicated for every question)
    TEXT_FAQ_ANSWER     = "text=Anyone abroad holding a"

    # --- Explore Solutions (Footer Section) ---
    HEADING_EXPLORE     = "role=heading[name='More Ways We Can Help']"
    TEXT_EXPLORE_DESC   = "text=Explore our offerings to"
    BTN_SLIDE_NEXT      = "role=button[name='next slide button']"
    BTN_SLIDE_PREV      = "role=button[name='previous slide button']"

    SOLUTIONS = {
        "e-Padala": {
            "title": "role=heading[name='e-Padala']",
            "btn": "role=link[name='Explore'] >> nth=0"
        },
        "Managed Network": {
            "title": "role=heading[name='Managed Network & Cloud']",
            "btn": "role=link[name='Explore'] >> nth=1"
        },
        "Edge Security": {
            "title": "role=heading[name='Edge and Security Solutions']",
            "btn": "role=link[name='Explore'] >> nth=2"
        }
    }