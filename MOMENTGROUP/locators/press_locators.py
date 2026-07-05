BASE_URL = "https://momentgroup.ph/press"

# ── Core Page Elements ────────────────────────────────────────────────────────
HEADING_PRESS_COL1   = "#presspage__col1 >> role=heading[name='Press' exact=true]"
HEADING_PRESS_COL2   = "#presspage__col2 >> role=heading[name='Press']"
HEADING_INQUIRIES    = "role=heading[name='Inquiries']"
TEXT_INQUIRIES       = "text=For general corporate press"
LINK_EMAIL           = "role=link[name='press@momentgroup.ph']"
DROPDOWN_BRANDS      = "role=combobox"

# ── Select Press Links (Using contains '*=' for robustness) ───────────────────
# Ooma Links
LINK_OOMA_SPOT       = "role=link[name*='August 2025 | Spot.ph Ooma']"
LINK_OOMA_PHILSTAR   = "role=link[name*='April 2025 | Philstar A new']"
LINK_OOMA_ABSCBN     = "role=link[name*=\"April 2025 | ABSCBN What's\"]"

# Din Tai Fung Links
LINK_DTF_INQUIRER    = "role=link[name*='February 2026 | Inquirer.net']"
LINK_DTF_GMA         = "role=link[name*='December 2025 | GMA News']"
LINK_DTF_BIZWORLD    = "role=link[name*='November 2025 | Business World Who needs birthday cake']"

# Mo' Cookies Links
LINK_MO_ABSCBN       = "role=link[name*=\"April 2025 | ABSCBN What's\"]"
LINK_MO_SPOT_APR     = "role=link[name*=\"April 2024 | spot.ph Here's\"]"
LINK_MO_SPOT_JUN     = "role=link[name*='June 2023 | Spot.ph Peanut']"

# The Moment Group (Corporate) Links
LINK_TMG_RAPPLER     = "role=link[name*='December 2025 | Rappler What']"
LINK_TMG_PHILIPPINE  = "role=link[name*='November 2025 | Philippine']"
LINK_TMG_LIFESTYLE   = "role=link[name*='July 2025 | Lifestyle']"

# Pancit Pancitan Links
LINK_PP_GENZ         = "role=link[name*='December 2024 | Gen-Z']"
LINK_PP_ABSCBN       = "role=link[name*='December 2024 | ABS-CBN Manam']"
LINK_PP_GENERIC      = "#contentshow-54"

# Mama Nams Links
LINK_MAMA_PHIL       = "role=link[name*='October 2025 | Philippine']"
LINK_MAMA_TATLER     = "role=link[name*='March 2024 | Tatler Late']"
LINK_MAMA_TATLER_ASIA= "role=link[name*='March 2024 | Tatler Asia Late']"

# Hayop Links
LINK_HAYOP_IWANDER   = "role=link[name*='December 2025 | I Wander']"
LINK_HAYOP_MICHELIN  = "role=link[name*='November 2025 | Michelin']"
LINK_HAYOP_PHILSTAR  = "role=link[name*='November 2025 | Philstar Life']"

# Mess Hall & Catering Links
LINK_MESS_HALL       = "role=link[name*='April 2024 | Primer Mess Hall']"
LINK_CATERING_RAPPLER= "role=link[name*='November 2024 | Rappler LIST']"
LINK_CATERING_TATLER = "role=link[name*='April 2024 | Tatler The best']"