class OrderOnlineLocators:
    # --- Entry Point (from main site) ---
    ORDER_ONLINE_NAV_BTN    = "a[href='https://hayop.atlas.kitchen/']:has-text('ORDER ONLINE')"
    ORDER_ONLINE_HERO_BTN   = "a.cta-2:has-text('order online')"

    # --- Homepage (hayop.atlas.kitchen) ---
    LOCATION_DROPDOWN       = "text=Select a delivery/pickup"
    LOCATION_SEARCH_INPUT   = "input[name='Enter a street name or postal']"

    # --- Sign Up Page (/signup) ---
    SIGNUP_PHONE_INPUT      = "input[name='Contact number'], [placeholder*='Contact number']"
    SIGNUP_EMAIL_INPUT      = "input[name='Enter your email'], [placeholder*='email']"
    SIGNUP_NAME_INPUT       = "input[name='Name'], [placeholder*='Name']"

    # --- Login Page (/login) ---
    LOGIN_PHONE_INPUT       = "input[name='Contact number'], [placeholder*='Contact number']"
    LOGIN_COUNTRY_SELECT    = "label[for*='Phone'] select, select[aria-label*='Phone number country']"

    # --- Item Page (/items/443-buko-pie) ---
    ITEM_SPECIAL_NOTES      = "textarea[placeholder*='special'], input[placeholder*='special']"
    ADD_TO_CART_BTN         = "button:has-text('Add to cart'), button:has-text('Add to Cart')"