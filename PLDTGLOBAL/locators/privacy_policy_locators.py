class PrivacyPolicyLocators:

    URL = "https://www.pldtglobal.com/en/privacy-policy"

    # --- Breadcrumbs & Header ---
    # Fix: Use role=navigation instead of the invalid label= engine
    LINK_HOME           = "role=navigation[name='Breadcrumb'] >> role=link[name='Home']"
    TEXT_BREADCRUMB     = "role=navigation[name='Breadcrumb'] >> text=Privacy Policy"
    HEADING_MAIN        = "role=heading[name='Privacy Policy']"
    
    # OneTrust specific header section
    IMG_OT_LOGO         = "#otnotice-section-eaed14ae-a1f2-475d-b194-82e140848b4b >> role=img"
    TEXT_OT_TITLE       = "#otnotice-section-eaed14ae-a1f2-475d-b194-82e140848b4b >> text=Privacy Policy"

    # --- Introduction ---
    TEXT_CORP_WEBSITE   = "text=PLDT Global Inc. Corporate"
    # Fix: Updated to match the actual Privacy Policy text from the DOM
    TEXT_PGI_INTRO      = "text=respects your fundamental right to privacy"

    # --- Section: Why we collect your personal data ---
    # Use get_by_role for the heading to be precise
    HEADING_WHY_COLLECT = "strong:has-text('Why we collect your personal data')"
    
    # Use get_by_role for the rights list items
    BULLETS_RIGHTS = [
        "role=listitem >> text='Request access to the personal data'",
        "role=listitem >> text='Request a rectification of your personal data'",
        "role=listitem >> text='Request the erasure of your personal data'",
        "role=listitem >> text='Request the restriction of'",
        "role=listitem >> text='Request portability of your'"
    ]
    TEXT_VISIT_CONTACT  = "text=As you visit the"  # Partial match to dodge curly quotes
    
    # Unique bullets under the repeated "We collect and process your" text
    BULLETS_COLLECT = [
        "text=To facilitate your engagement",
        "text=To facilitate the beginning",
        "text=To ensure efficient",
        "text=To facilitate your communication with our Enterprise Group",
        "text=To facilitate your communication with our Carrier team"
    ]
    
    TEXT_PROCESS_B      = "text=We process your personal"
    TEXT_PUBLIC_AUTH    = "text=To assist public authorities"

    # --- Section: Disclosure ---
    HEADING_DISCLOSE    = "text=When we disclose your"
    TEXT_DISCLOSE_INTRO = "text=In some instances, we may be"
    TEXT_SHARE_MIGHT    = "text=This means we might share"
    TEXT_SERVICE_PROVS  = "text=Our service providers and"
    TEXT_LAW_ENFORCE    = "text=Law enforcement and"

    # --- Section: Protection & Retention ---
    HEADING_PROTECT     = "text=How we protect your personal"
    TEXT_INTEGRITY      = "text=The integrity,"
    TEXT_SAFEGUARDS     = "text=We also put in place the"
    TEXT_KEEP_PROTECT   = "text=We keep and protect your"
    TEXT_ONLY_NECESSARY = "text=We keep your information only"
    TEXT_RESTRICT       = "text=We restrict access to your"
    TEXT_NOTIFY         = "text=We promptly notify you and"
    TEXT_UPDATE         = "text=We let you update your"

    # --- Section: User Choices ---
    HEADING_CHOICES = "text=/What your choices are/i"
    TEXT_AFFORDED       = "text=You are afforded certain"
    
    # Unique rights bullets
    BULLETS_RIGHTS = [
        "text=Request access to the",
        "text=Request a rectification of",
        "text=Request the erasure of your",
        "text=Request the restriction of",
        "text=Request portability of your"
    ]

    TEXT_MOREOVER_RIGHT = "text=You moreover have a right to"
    TEXT_TO_THE_EXTENT  = "text=To the extent that the"
    TEXT_EXERCISE       = "text=To exercise any of these"
    TEXT_COMPLAINT      = "text=If, despite our commitment"

    # --- Footer / Contact Info ---
    # Fix: Removed the strict regex and trailing period to match the raw HTML
    TEXT_COMPANY_NAME   = "text=PLDT GLOBAL INC."
    TEXT_ADDRESS_1      = "text=/F Ramon Cojuangco Bldg"
    TEXT_ADDRESS_2      = "text=Makati Avenue, Makati City"
    LINK_PRIVACY_EMAIL  = "role=link[name='dataprivacy@pldtglobal.com']"
    TEXT_END_NOTICE     = "text=END OF PRIVACY NOTICE"