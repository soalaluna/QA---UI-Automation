class ConsumerLocators:

    URL = "https://www.pldtglobal.com/en/consumer"

    # --- Hero Section ---
    IMG_HERO            = "role=img[name*='Everyday Digital Solutions']"
    HEADING_SUB         = "role=heading[name=/^consumer$/i]"
    HEADING_MAIN        = "role=heading[name*='Digital Services for']"
    TEXT_HERO_DESC      = "text=Simple, secure, and"

    # --- Solutions Grid ---
    HEADING_GRID        = "role=heading[name=/^Solutions for Global Filipinos$/]"
    TEXT_GRID_DESC      = "text=Digital services designed to"
    BTN_LEARN_MORE      = "role=link[name='Learn More']"

    SOLUTIONS = {
        "ePadala": {
            "heading": "role=heading[name='ePadala']",
            "desc": "text=ePadala is a service that"
        },
        "Smart Virtual Number": {
            "heading": "role=heading[name='Smart Virtual Number']",
            "desc": "text=Smart Virtual Number (SVN) is"
        },
        "TinBo": {
            "heading": "role=heading[name='TinBo']",
            "desc": "text=Your one-stop digital shop"
        }
    }

    # --- Bottom CTA Section ---
    HEADING_CTA         = "role=heading[name='Reach Out and Stay Connected']"
    TEXT_CTA_DESC       = "text=Have questions or need"
    BTN_INQUIRY         = "role=link[name='Send an Inquiry']"