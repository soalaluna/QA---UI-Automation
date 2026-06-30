class TermsConditionsLocators:

    TERMS_CONDITIONS_URL = "https://hayopnimanam.com/terms-conditions/"

    # --- Page Header ---
    @staticmethod
    def heading_terms_conditions(page):
        return page.get_by_role("heading", name="terms & conditions")

    TEXT_EFFECTIVE_DATE = "text=Effective Date: May 31,"

    # --- Covenant ---
    @staticmethod
    def heading_covenant(page):
        return page.get_by_role("heading", name="Covenant")

    TEXT_WHEN_YOU_VISIT       = "text=When you visit our website"
    TEXT_FURTHER_BY_ACCESSING = "text=Further, by accessing, using"
    TEXT_IF_YOU_DO_NOT_AGREE  = "text=If you do not agree with any"

    # --- Amendments to the Terms and Conditions ---
    @staticmethod
    def heading_amendments(page):
        return page.get_by_role("heading", name="Amendments to the Terms and")

    TEXT_HNM_MAY_FROM_TIME    = "text=Hayop Ni Manam may from time"
    TEXT_HNM_SHALL_INFORM     = "text=Hayop Ni Manam shall inform"
    TEXT_CHANGES_IN_TERMS     = "text=Changes in the Terms and"
    TEXT_IF_YOU_CONTINUE      = "text=If you continue to use,"

    # --- Definition of Terms ---
    @staticmethod
    def heading_definition_of_terms(page):
        return page.get_by_role("heading", name="Definition of Terms:")

    TEXT_UNLESS_CONTEXT       = "text=Unless the context otherwise"
    TEXT_INTERPRETATION       = "text=Interpretation: Any reference"

    # --- General Use of Services ---
    @staticmethod
    def heading_general_use_of_services(page):
        return page.get_by_role("heading", name="General Use of Services:")

    TEXT_AGREE_TO_COMPLY      = "text=You agree to comply with any"
    TEXT_HNM_IS_SINGAPORE     = "text=Hayop ni Manam is a Singapore"
    TEXT_MUST_BE_EIGHTEEN     = "text=You must at least be eighteen"
    TEXT_AVAILABILITY         = "text=Availability of Hayop ni"
    TEXT_RIGHT_NOT_OBLIGATION = "text=Right, but not obligation, to"
    TEXT_ADDITIONAL_TERMS     = "text=Additional terms. In addition"
    TEXT_CREATING_ACCOUNT     = "text=Creating your account"  # exact
    TEXT_PASSWORD             = "text=Password. During registration"
    TEXT_INFORMATION_CREATING = "text=Information. In creating your"
    TEXT_SHARING_HNM          = "text=SharingHayop Ni Manam shares"

    # --- Use of Services ---
    @staticmethod
    def heading_use_of_services(page):
        return page.get_by_role("heading", name="Use of Services", exact=True)

    TEXT_RESTRICTIONS_USE     = "text=Restrictions. Use of the"
    TEXT_GENERAL_TC_HEADING   = "text=General Terms and Conditions"
    TEXT_GENERAL_TC_BODY      = "text=General Terms and Conditions. You agree: To access and/or use the Services only"
    TEXT_PURPORTED_USE        = "text=Purported use/access. You"
    TEXT_AGREE_TO_BE_BOUND    = "text=You agree to be bound by any"

    # --- Intellectual Property ---
    TEXT_INTELLECTUAL_PROPERTY = "text=Intellectual Property"  # exact
    TEXT_OWNERSHIP             = "text=Ownership: The Intellectual"
    TEXT_RESTRICTED_USE        = "text=Restricted use: No part or"
    TEXT_TRADEMARKS_REGISTERED = "text=The Trademarks are registered"

    # --- Third-Party Links ---
    TEXT_THIRD_PARTY_LINKS_HEADING = "text=Third-Party Links"  # exact
    TEXT_CERTAIN_CONTENT           = "text=Certain content, products and"
    TEXT_WEBSITE_MAY_CONTAIN       = "text=The Website may contain links"
    TEXT_MAY_LINK_TO_HOMEPAGE      = "text=You may link to the homepage"
    TEXT_MAY_USE_FEATURES          = "text=You may use these features"
    TEXT_WEBSITE_FROM_WHICH        = "text=The website from which you"
    TEXT_AGREE_TO_COOPERATE        = "text=You agree to cooperate with"
    TEXT_WE_MAY_DISABLE            = "text=We may disable all or any"
    TEXT_THIRD_PARTY_LINKS_BODY    = "text=These third-party links on"
    TEXT_HNM_NOT_LIABLE_INCONV     = "text=Hayop Ni Manam shall not be liable for any inconvenience, inaccuracy, harm or"

    # --- User Comments, Feedbacks, and Suggestions ---
    @staticmethod
    def heading_user_comments(page):
        return page.get_by_role("heading", name="User Comments, Feedbacks, and")

    TEXT_WE_APPRECIATE_HEARING = "text=We appreciate hearing from"
    TEXT_OWN_EXCLUSIVELY        = "text=own, exclusively, all now"
    TEXT_NOT_BE_SUBJECT         = "text=not be subject to any"
    TEXT_ENTITLED_UNRESTRICTED  = "text=be entitled to unrestricted"

    # --- Cookies ---
    @staticmethod
    def heading_cookies(page):
        return page.get_by_role("heading", name="Cookies")

    TEXT_PLATFORM_EMPLOYS_COOKIES = "text=This Platform employs cookies"
    TEXT_WE_MAY_USE_THIRD_PARTY    = "text=We may use third-party"
    TEXT_MAY_REFUSE_TO_ACCEPT      = "text=You may refuse to accept"

    # --- Representations and Warranties ---
    TEXT_REPS_AND_WARRANTIES_HEADING = "text=Representations and Warranties"
    TEXT_WHILE_WE_AIM                 = "text=While we aim to give Hayop Ni"
    TEXT_ACCEPT_AND_UNDERSTAND        = "text=You accept and understand"
    TEXT_EXCEPT_AS_OTHERWISE          = "text=Except as otherwise provided"
    TEXT_IN_NO_CASE_SHALL             = "text=In no case shall Hayop Ni"

    # --- Risk and Liability ---
    @staticmethod
    def heading_risk_and_liability(page):
        return page.get_by_role("heading", name="Risk and Liability")

    TEXT_RISK_OF_DAMAGE        = "text=Risk of or damage to or loss"
    TEXT_LIABILITY_OF_HNM      = "text=The liability of Hayop Ni"
    TEXT_NOT_LIABLE_LOSS_DELAY = "text=Hayop Ni Manam shall not be liable for any loss, damage, or delay arising from"
    TEXT_CLAIMS_FOR_LOSS       = "text=Any claims for loss, damage"

    # --- Payment ---
    @staticmethod
    def heading_payment(page):
        return page.get_by_role("heading", name="Payment")

    TEXT_RESERVATION_POLICY    = "text=Hayop Ni Manam’s Reservation"
    TEXT_PAYMENT_METHODS       = "text=Payment Methods: We accept"
    TEXT_PAYMENT_PROCESSING    = "text=Payment Processing: All"
    TEXT_REFUND_POLICY         = "text=Refund Policy: Our refund"
    TEXT_PAYMENT_METHODS_MAY_BE = "text=The payment methods may be"
    TEXT_YOU_AGREE_THAT        = "text=You agree that you are"

    # --- Notices ---
    @staticmethod
    def heading_notices(page):
        return page.get_by_role("heading", name="Notices")

    TEXT_NOTICES_FROM_US      = "text=Notices from us shall be sent"
    TEXT_GIVE_NOTICE_TO_US    = "text=You may give notice to us in"

    # --- Termination ---
    @staticmethod
    def heading_termination(page):
        return page.get_by_role("heading", name="Termination")

    TEXT_YOU_MAY_TERMINATE    = "text=You may terminate the"

    # --- General Provisions ---
    @staticmethod
    def heading_general_provisions(page):
        return page.get_by_role("heading", name="General Provisions")

    TEXT_CUMULATIVE_RIGHTS    = "text=Cumulative rights and"
    TEXT_NO_WAIVER            = "text=No waiver: Our failure to"
    TEXT_SEVERABILITY         = "text=Severability: If at any time"
    TEXT_RIGHTS_OF_THIRD_PARTIES = "text=Rights of third parties: A"
    TEXT_GOVERNING_LAW        = "text=Governing law: Use of Hayop"
    TEXT_AMENDMENTS_BY_NOTICE = "text=Amendments: We may by notice"
    TEXT_CORRECTION_OF_ERRORS = "text=Correction of errors: Any"
    TEXT_CURRENCY             = "text=Currency: Money references"
    TEXT_ENTIRE_AGREEMENT     = "text=Entire agreement: These Terms"
    TEXT_BINDING_AND_CONCLUSIVE = "text=Binding and conclusive: You"
    TEXT_ASSIGNMENT           = "text=Assignment: You may not"
    TEXT_FORCE_MAJEURE        = "text=Force Majeure: We shall not"

    # --- How to reach Hayop Ni Manam ---
    @staticmethod
    def heading_how_to_reach(page):
        return page.get_by_role("heading", name="How to reach Hayop Ni Manam")

    TEXT_SHOULD_YOU_HAVE_Q    = "text=Should you have any questions"
    LINK_EMAIL_AMOY_STREET    = "role=link[name='amoy.street@hayopnimanam.com']"
    LINK_EMAIL_MOMENT_GROUP   = "role=link[name='momentgroup@hayopnimanam.com']"
    TEXT_CONTACT_NO           = "text=Contact No: +65 8028"

    @staticmethod
    def paragraph_email_amoy_street(page):
        return page.get_by_role("paragraph").filter(has_text="Email: amoy.street@")

    IMG_KALACHUHI = "role=img[name='kalachuhi']"