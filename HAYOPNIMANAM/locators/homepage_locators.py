class HomepageLocators:

    # --- URLs ---
    BASE_URL = "https://hayopnimanam.com/"

    # --- Navigation Links ---
    NAV_MENU         = "a[aria-label='Go to Page MENU']"
    NAV_ABOUT        = "a[aria-label='Go to Page ABOUT']"
    NAV_PRESS        = "a[aria-label='Go to Page PRESS']"
    NAV_CONTACT      = "a[aria-label='Go to Page CONTACT']"
    NAV_RESERVATIONS = "a[aria-label='Go to Page RESERVATIONS']"
    NAV_ORDER_ONLINE = "a[aria-label='Go to Page ORDER ONLINE']"  # opens popup
    NAV_HOMEPAGE     = "a[aria-label='Homepage'] >> nth=0"

    # --- Hero / CTA Buttons ---
    # Use aria-label to uniquely target the hero section buttons
    BTN_MAKE_RESERVATION = "a[aria-label='make a reservation']"
    BTN_ORDER_ONLINE     = "a.cta-2[aria-label='order online']"   # opens popup
    BTN_SEE_THE_MENU     = "a:has-text('see the menu')"

    # --- Footer ---
    FOOTER_INSTAGRAM = "a[href='https://www.instagram.com/hayop.sg']"
    FOOTER_PRIVACY   = "a[href='https://hayopnimanam.com/privacy-policy/']"
    FOOTER_TERMS     = "a[href='https://hayopnimanam.com/terms-conditions/']"