BASE_URL    = "https://www.pldtglobal.com/en"

# ── Logo ──────────────────────────────────────────────────────────────────────
LOGO                        = "role=link[name='PLDT Global Corporation Logo']"

# ── Navigation ────────────────────────────────────────────────────────────────
NAV_HOME                    = "role=link[name='Home']"
NAV_SOLUTIONS               = "role=link[name='Solutions']"
# FIX: Scope to navigation to avoid matching footer links
NAV_ABOUT                   = "role=navigation >> a[href='/en/about-us']"
NAV_NEWS                    = "a[href='/en/news-and-insights']"  # only in nav, not footer
NAV_CAREERS                 = "role=navigation >> a[href='/en/careers']"

# ── Search ────────────────────────────────────────────────────────────────────
BTN_SEARCH                  = "role=button[name='search button']"
INPUT_SEARCH                = "role=textbox[name='Search']"
BTN_SEARCH_SUBMIT           = "form >> role=button[name='search button']"

# ── Solutions Dropdown ────────────────────────────────────────────────────────
# FIX: Scope to nav dropdown specifically (not footer Enterprise Solutions link)
BTN_ENTERPRISE              = "role=link[name='Enterprise', exact=True]"
BTN_CONSUMER                = "a[href='/en/consumer']"

# ── Solutions Sub-nav Links ───────────────────────────────────────────────────
NAV_ENTERPRISE_LINK         = "role=link[name='Enterprise']"
NAV_CARRIER_LINK            = "role=navigation >> role=link[name='Carrier']"
NAV_CONSUMER_LINK           = "role=link[name='Consumer']"

# ── Hero Section ──────────────────────────────────────────────────────────────
HERO_CTA                    = "role=link[name=\"Let's Build What's Next\"]"

# ── Learn More Links ──────────────────────────────────────────────────────────
LEARN_MORE                  = "role=link[name='Learn More']"

# ── News Section ──────────────────────────────────────────────────────────────
BTN_MORE_NEWS               = "role=link[name='More News']"
BTN_NEWS_ARTICLE_1          = "role=button[name='Read more article: PLDT Global Joins Community Effort to Support Migrant Workers in Hong Kong']"
BTN_NEWS_ARTICLE_2          = "role=button[name='Read more article: PLDT Global builds the growth rails connecting brands to the overseas Filipino market']"
BTN_NEWS_ARTICLE_3          = "role=button[name=\"Read more article: Insights, Connections, & Exciting Opportunities at Sync City '26\"]"
SHARE_FACEBOOK              = "role=link[name='Share on Facebook']"
SHARE_LINKEDIN              = "role=link[name='Share on Linkedin']"

# ── Cookie Banner ─────────────────────────────────────────────────────────────
BTN_ACCEPT_COOKIES          = "role=button[name='Accept All Cookies']"

# ── Footer ────────────────────────────────────────────────────────────────────
FOOTER_EMAIL                = "role=link[name='askus@pldtglobal.com']"
FOOTER_PHONE                = "role=link[name='(+632) 8886-4578']"
FOOTER_LINKEDIN             = "role=link[name='Follow us on Linkedin']"
FOOTER_GLOBAL_CONNECTIVITY  = "role=link[name='Global Connectivity']"
FOOTER_MANAGED_NETWORK      = "role=link[name='Managed Network and Cloud']"
FOOTER_EDGE_SECURITY        = "role=link[name='Edge and Security Solutions']"
FOOTER_DATA_CENTERS         = "role=link[name='Data Centers and Hyperscale']"
FOOTER_VORTEX               = "role=link[name='VORTEX']"
FOOTER_TINBO                = "role=link[name='TinBo']"
FOOTER_EPADALA              = "role=link[name='ePadala']"
FOOTER_SMART_VIRTUAL        = "role=link[name='Smart Virtual Number']"
FOOTER_WHOLESALE_VOICE      = "role=link[name='Wholesale Voice']"
FOOTER_ABOUT                = "footer >> role=link[name='About']"
FOOTER_CAREERS              = "footer >> role=link[name='Careers']"
FOOTER_CONTACT_US           = "footer >> role=link[name='Contact Us']"
FOOTER_PRIVACY_POLICY       = "role=link[name='Privacy Policy']"
FOOTER_CONTACT_BTN          = "role=link[name='contact us button']"