class ReservationLocators:
    BASE_URL            = "https://hayopnimanam.com/"
    RESERVATION_URL     = "https://hayopnimanam.com/reservation/"

    # --- Navigation ---
    NAV_RESERVATIONS        = "nav a:has-text('RESERVATIONS')"

    # --- Reservation Page CTA ---
    LINK_MAKE_RESERVATION   = "a.cta-button[href*='sevenrooms']"

    # --- Footer ---
    FOOTER_INSTAGRAM    = "a[href='https://www.instagram.com/hayop.sg']"
    FOOTER_PRIVACY      = "a[href='https://hayopnimanam.com/privacy-policy/']"
    FOOTER_TERMS        = "a[href='https://hayopnimanam.com/terms-conditions/']"

    # ── SevenRooms Widget ─────────────────────────────────────────────────────
    # Confirmed from live accessibility tree — spinner/stepper style (no calendar)

    # Date stepper
    SR_DATE_DISPLAY     = "button:has-text('Date')"          # e.g. "Tue, 16 Jun Date"
    SR_DATE_INCREMENT   = "button[aria-label='increment Date']"
    SR_DATE_DECREMENT   = "button[aria-label='decrement Date']"

    # Guest stepper
    SR_GUEST_DISPLAY    = "button:has-text('Guest')"         # e.g. "2 Guests" or "1 Guest"
    SR_GUEST_INCREMENT  = "button[aria-label='increment Guest'], button[aria-label='increment Guests']"
    SR_GUEST_DECREMENT  = "button[aria-label='decrement Guest'], button[aria-label='decrement Guests']"

    # Time stepper
    SR_TIME_DISPLAY     = "button:has-text('Time')"          # e.g. "17:00 Time"
    SR_TIME_INCREMENT   = "button[aria-label='increment Time']"
    SR_TIME_DECREMENT   = "button[aria-label='decrement Time']"

    # Search
    SR_SEARCH_BUTTON    = "button:has-text('Search')"

    # Time slot selection — appears after clicking Search
    SR_TIME_SLOT        = "button:has-text('Main Dining'), button:has-text('High Table')"

    # Login — appears after selecting a time slot
    SR_LOGIN_GUEST      = "button:has-text('Continue as Guest')"

    # Guest form fields
    SR_FIELD_FIRST_NAME = "input[placeholder*='First'], [name*='first']"
    SR_FIELD_LAST_NAME  = "input[placeholder*='Last'], [name*='last']"
    SR_FIELD_EMAIL      = "input[placeholder*='email'], input[type='email']"
    SR_FIELD_PHONE      = "input[placeholder*='phone'], input[type='tel']"