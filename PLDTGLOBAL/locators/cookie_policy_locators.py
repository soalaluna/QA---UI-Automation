class CookiePolicyLocators:

    COOKIE_POLICY_URL = "https://www.pldtglobal.com/en/cookie-policy"

    # --- Breadcrumb ---
    @staticmethod
    def breadcrumb_home_link(page):
        return page.get_by_label("Breadcrumb").get_by_role("link", name="Home")

    @staticmethod
    def breadcrumb_cookie_policy_text(page):
        return page.get_by_label("Breadcrumb").get_by_text("Cookie Policy")

    # --- Page Header ---
    @staticmethod
    def heading_cookie_policy(page):
        return page.get_by_role("heading", name="Cookie Policy")

    TEXT_COOKIE_POLICY_TITLE  = "text=COOKIE POLICY"        
    TEXT_CORPORATE_SECTION    = "text=PLDT Global Inc. Corporate"
    
    # Updated: Using a partial CSS match to avoid the curly/smart quote (“”) text formatting trap
    TEXT_PGI_IS               = "text=is committed to safeguarding your personal information"

    # --- What Are Cookies ---
    TEXT_WHAT_ARE_COOKIES     = "text=What are cookies?"
    TEXT_COOKIE_DEFINITION    = "text=A cookie is a small text file"

    # --- How PLDT OL Uses Cookies ---
    TEXT_HOW_PLDT_USES        = "text=How does PLDT OL use cookies?"
    TEXT_FOLLOWING_SUMMARY    = "text=The following is a summary of"

    @staticmethod
    def underline_strictly_necessary(page):
        return page.locator("u").filter(has_text="Strictly Necessary Cookies")

    TEXT_STRICTLY_NECESSARY_DESC = "text=PGI uses cookies that are"

    @staticmethod
    def underline_functional(page):
        return page.locator("u").filter(has_text="Functional Cookies")

    TEXT_FUNCTIONAL_DESC      = "text=Functional cookies enhance"

    @staticmethod
    def underline_performance(page):
        return page.locator("u").filter(has_text="Performance Cookies")

    TEXT_PERFORMANCE_DESC     = "text=Performance cookies generate"

    @staticmethod
    def underline_targeting(page):
        return page.locator("u").filter(has_text="Targeting Cookies")

    TEXT_TARGETING_DESC       = "text=Targeting cookies allows the"

    # --- Options ---
    TEXT_WHAT_ARE_OPTIONS     = "text=What are your options with"
    TEXT_YOU_HAVE_OPTIONS     = "text=You have a number of options"
    TEXT_TO_CHANGE_BROWSER    = "text=To change your browser"

    # --- Browser Settings Links ---
    TEXT_GOOGLE_CHROME_INTRO  = "text=Google Chrome https://support"
    
    # Updated: Using CSS href selectors because the DOM links lack accessible text
    LINK_CHROME_SETTINGS      = "a[href*='chrome']"
    TEXT_IE                   = "text=Microsoft Internet Explorer"
    LINK_IE_SETTINGS          = "a[href*='microsoft']"
    TEXT_SAFARI               = "text=Apple Safari"
    LINK_SAFARI_SETTINGS      = "a[href*='apple']"
    TEXT_FIREFOX              = "text=Mozilla Firefox"
    LINK_FIREFOX_SETTINGS     = "a[href*='mozilla']"

    # --- Cookie List Section Header ---
    @staticmethod
    def heading_cookie_list(page):
        return page.get_by_role("heading", name="Cookie List")

    TEXT_COOKIE_LIST_INTRO    = "text=A cookie is a small piece of"

    # --- Strictly Necessary Cookies Table ---
    @staticmethod
    def heading_strictly_necessary_table(page):
        return page.get_by_role("heading", name="Strictly Necessary Cookies")

    @staticmethod
    def strictly_necessary_desc(page):
        return page.locator("#ot-sdk-cookie-policy-v2").get_by_text("These cookies are necessary")

    COL_COOKIE_SUBGROUP_0     = "role=columnheader[name='Cookie Subgroup']"  # .first
    COL_COOKIES_0             = "role=columnheader[name='Cookies']"          # .first
    COL_COOKIES_USED_0        = "role=columnheader[name='Cookies used']"     # .first
    CELL_PLDTGLOBAL_COM       = "role=cell[name='www.pldtglobal.com']"
    CELL_FIRST_PARTY_0        = "role=cell[name='First Party']"              # .first
    
    # Updated: Regex /.../i to bypass hidden "Opens in a new Tab" screen reader text
    LINK_OPTANON_CONSENT      = "role=link[name=/OptanonConsent/i]"
    LINK_OPTANON_ALERT_CLOSED = "role=link[name=/OptanonAlertBoxClosed/i]"

    # --- Functional Cookies Table ---
    @staticmethod
    def heading_functional_table(page):
        return page.get_by_role("heading", name="Functional Cookies")

    @staticmethod
    def functional_desc(page):
        return page.locator("#ot-sdk-cookie-policy-v2").get_by_text("These cookies make your")

    # Updated: Regex with ^ anchor to prevent matching c.clarity.ms or www.clarity.ms by accident
    LINK_CLARITY_MS_EXACT     = "role=link[name=/^clarity\\.ms/i]"   
    LINK_C_CLARITY_MS         = "role=link[name=/^c\\.clarity\\.ms/i]"
    LINK_WWW_CLARITY_MS       = "role=link[name=/^www\\.clarity\\.ms/i]"

    @staticmethod
    def functional_c_bing_label(page):
        return page.get_by_role("table", name="Functional Cookies").get_by_label(
            "c.bing.com Opens in a new Tab"
        )

    CELL_MUID_0               = "text=MUID"                                  # .first
    CELL_MR_SM_ANONCHK        = "text=MR, SM, ANONCHK"
    CELL_CLID                 = "text=CLID"
    CELL_SRM_B                = "text=SRM_B"
    CELL_THIRD_PARTY_0        = "text=Third Party"                           # .first/nth

    # --- Performance Cookies Table ---
    @staticmethod
    def heading_performance_table(page):
        return page.get_by_role("heading", name="Performance Cookies")

    @staticmethod
    def performance_desc(page):
        return page.locator("#ot-sdk-cookie-policy-v2").get_by_text("We use these cookies to")

    CELL_PLDTGLOBAL_COM_EXACT = "role=cell[name='pldtglobal.com']"          # exact
    
    # Updated: Regex to bypass hidden "Opens in a new Tab" text
    LINK_GA_XXXXXXXXXX        = "role=link[name=/_ga_xxxxxxxxxx/i]"

    @staticmethod
    def performance_c_bing_label(page):
        return page.get_by_role("table", name="Performance Cookies").get_by_label(
            "c.bing.com Opens in a new Tab"
        )

    CELL_MR_EXACT             = "text=MR"                                    # exact
    CELL_FIRST_PARTY_1        = "role=cell[name='First Party']"              # .nth(1)

    # Additional performance popup links
    # Updated: Added regex here as well to future-proof them
    LINK_GA                   = "role=link[name=/^_ga /i]" 
    LINK_CLSK                 = "role=link[name=/_clsk/i]"
    LINK_CLCK                 = "role=link[name=/_clck/i]"

    # --- Targeting Cookies Table ---
    @staticmethod
    def heading_targeting_table(page):
        return page.get_by_role("heading", name="Targeting Cookies")

    @staticmethod
    def targeting_desc(page):
        return page.locator("#ot-sdk-cookie-policy-v2").get_by_text("Based on your browsing")

    # Updated: Regex with ^ anchor for exact start match
    LINK_BING_COM_EXACT       = "role=link[name=/^bing\\.com/i]"     
    CELL_MUID_1               = "role=cell[name='MUID']"                     # .nth(1)
    CELL_THIRD_PARTY_5        = "text=Third Party"                           # .nth(5)