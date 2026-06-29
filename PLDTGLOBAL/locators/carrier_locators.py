CARRIER_URL     = "https://www.pldtglobal.com/en/carrier"

# --- Navigation ---
NAV_CARRIER             = "role=navigation >> role=link[name='Carrier']"
CARRIER_LINK_MAIN       = "#main >> role=link[name='Carrier']"

# --- Learn More Links ---
# First "Learn More" is non-functional / does not navigate (anchor or placeholder)
LEARN_MORE_FIRST        = "role=link[name='Learn More']"   # use .first — does NOT navigate
LEARN_MORE_SECOND       = "role=link[name='Learn More']"   # use .nth(1) — navigates to Wholesale Voice