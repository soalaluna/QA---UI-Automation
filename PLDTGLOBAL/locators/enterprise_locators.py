class EnterpriseLocators:

    URL = "https://www.pldtglobal.com/en/enterprise"

    # --- Hero Section ---
    IMG_HERO            = "role=img[name*='Powering Enterprise Networks']"
    HEADING_SUB         = "role=heading[name=/^enterprise$/]"
    HEADING_MAIN        = "role=heading[name*='Solutions that Power a']"
    TEXT_HERO_DESC      = "text=Accelerate your digital"

    # --- Solutions Grid ---
    BTN_LOAD_MORE       = "role=button[name='Load More Solutions']"
    BTN_LEARN_MORE      = "role=link[name='Learn More']"

    SOLUTIONS = {
        "Enterprise Solutions": {
            "heading": "role=heading[name='Enterprise Solutions']",
            "desc": "text=PGC delivers enterprises"
        },
        "Data Centers": {
            # Changed to *= (contains) to handle "Integration" being added to the end
            "heading": "role=heading[name*='Data Centers and Hyperscale']",
            "desc": "text=Powered by the PLDT Group’s"
        },
        "Edge & Security": {
            "heading": "role=heading[name='Edge and Security Solutions']",
            "desc": "text=Enterprise-grade edge and"
        },
        "Global Connectivity": {
            "heading": "role=heading[name='Global Connectivity']",
            "desc": "text=Scalable, secure, and high-"
        },
        "Managed Network": {
            "heading": "role=heading[name='Managed Network and Cloud']",
            "desc": "text=Engineered on PLDT’s global"
        },
        "VORTEX": {
            "heading": "role=heading[name='VORTEX powered by PLDT Global']",
            "desc": "text=VORTEX is part of the PLDT"
        }
    }

    # --- Bottom CTA Section ---
    HEADING_CTA         = "role=heading[name='Reach Out and Stay Connected']"
    TEXT_CTA_DESC       = "text=Have questions or need"
    BTN_INQUIRY         = "role=link[name='Send an Inquiry']"