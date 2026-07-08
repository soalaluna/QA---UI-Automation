class PLDTEdgeSecurityLocators:

    URL = "https://www.pldtglobal.com/en/enterprise/edge-and-security"

    # --- Breadcrumbs ---
    # Using *= (contains) to avoid the strict mode / exact match error
    LINK_ENTERPRISE    = "role=link[name*='Enterprise']"
    TEXT_BREADCRUMB    = "text='Edge and Security'"
    ICON_CHEVRON       = ".lucide-chevron-right"

    # --- Hero & Intro Section ---
    HEADING_MAIN       = "role=heading[name='Edge and Security Solutions']"
    TEXT_HERO_DESC     = "text=Enterprise-grade edge and"
    IMG_BACK_TO        = "section:has-text('Back to') >> img"
    
    # The codegen identified this class for the product card icons
    CARD_ICONS         = ".flex-shrink-0"

    # --- Product Cards Dictionary ---
    PRODUCTS = {
        "Content Delivery Network": {
            "heading": "role=heading[name='Content Delivery Network (CDN)']",
            "desc": "text=Deliver content at scale"
        },
        "Endpoint & Cloud Security": {
            "heading": "role=heading[name*='Endpoint & Cloud Security']",
            "desc": "text=Secure endpoints and cloud workloads"
        },
        "Network Security": {
            "heading": "role=heading[name*='Network Security']",
            "desc": "text=Protect enterprise networks"
        },
        "Authentication and Fraud Prevention": {
            "heading": "role=heading[name*='Authentication and Fraud Prevention']",
            # We use a safe chunk of text to avoid the "Preventiontrengthen" typo in the DOM
            "desc": "text=digital trust using PLDT" 
        },
        "Cloud and Web Edge": {
            "heading": "role=heading[name*='Cloud and Web Edge']",
            "desc": "text=Optimize"
        },
        "IP eXchange": {
            "heading": "role=heading[name*='IP eXchange']",
            "desc": "text=A private, quality"
        }
    }