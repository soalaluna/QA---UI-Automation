class PLDTConnectivityLocators:

    URL = "https://www.pldtglobal.com/en/enterprise/pgc-global-connectivity"

    # --- Breadcrumbs ---
    LINK_ENTERPRISE    = "role=link[name=/^Enterprise$/]"
    TEXT_BREADCRUMB    = "span:has-text('Global Connectivity')"
    ICON_CHEVRON       = ".lucide.lucide-chevron-right"

    # --- Hero & Intro Section ---
    HEADING_MAIN       = "role=heading[name='Global Connectivity']"
    TEXT_HERO_DESC     = "text=Scalable, secure, and high-"
    IMG_BACK_TO        = "section:has-text('Back to') >> img"
    
    HEADING_PORTFOLIO  = "role=heading[name*='Your Global Connection']"
    TEXT_PORTFOLIO     = "role=paragraph >> text=A portfolio of internet and"
    
    # Generic icon locator found inside the product cards
    CARD_ICONS         = ".gradient-border-card .relative"

    # --- Product Cards Dictionary ---
    PRODUCTS = {
        "Fiber Internet": {
            "heading": "role=heading[name='Fiber Internet for Business']",
            "desc": "text=High-speed, low-latency fiber"
        },
        "Dedicated Internet Access": {
            "heading": "role=heading[name='Dedicated Internet Access']",
            "desc": "text=Premium uncontended bandwidth"
        },
        "Satellite Internet": {
            "heading": "role=heading[name='Satellite Internet']",
            "desc": "text=Wide-"
        },
        "International Ethernet Private Line": {
            "heading": "role=heading[name*='International Ethernet']",
            "desc": "text=LAN-to-LAN interconnection"
        },
        "International Private Leased Circuit": {
            "heading": "role=heading[name*='International Private Leased']",
            "desc": "text=Private point-to-point"
        },
        "IP Transit and Hubbing": {
            "heading": "role=heading[name='IP Transit and Hubbing']",
            "desc": "text=Aggregated, scalable global"
        },
        "iGate": {
            "heading": "role=heading[name='iGate']",
            "desc": "text=A carrier-grade internet"
        },
        "Metro Ethernet": {
            "heading": "role=heading[name='Metro Ethernet']",
            "desc": "text=High-capacity,"
        }
    }