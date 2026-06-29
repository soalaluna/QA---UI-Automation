"""
Locators for the Press page - hayopnimanam.com/press
Only contains clickable/interactive elements.
Note: Article titles with smart quotes (') use partial text to avoid
      encoding mismatches between the selector and the DOM.
"""


class PressLocators:

    # --- URLs ---
    BASE_URL  = "https://hayopnimanam.com/"
    PRESS_URL = "https://hayopnimanam.com/press/"

    # --- Navigation ---
    NAV_PRESS = "a[aria-label='Go to Page PRESS']"

    # --- Press Articles (all open in popup) ---
    # Page 1
    ARTICLE_CNA                 = "a:has-text('read more')"
    ARTICLE_MOMENT_GROUP        = "a:has-text('The Moment Group')"       # smart quote in full title
    ARTICLE_OVERSEAS_OUTPOST    = "a:has-text('Hayop \u2013 Overseas Outpost of')"
    ARTICLE_FILIPINO_RESTAURANT = "a:has-text('Filipino restaurant Hayop')"
    ARTICLE_SISTER              = "a:has-text('hayop, Manam')"           # smart quote in full title
    ARTICLE_BEST_EATS           = "a:has-text('Best eats of 2024: Best')"

    # Page 2
    ARTICLE_JOYS_OF             = "a:has-text('At Hayop, the joys of')"
    ARTICLE_FIRST_FINE          = "a:has-text('Hayop: Singapore')"       # smart quote in full title
    ARTICLE_JOYOUS              = "a:has-text('Hayop is a joyous')"
    ARTICLE_FOOD_PICKS          = "a:has-text('Food Picks: Filipino fare at')"
    ARTICLE_ADOBO               = "a:has-text('From adobo to zipyu thee')"

    # Page 3
    ARTICLE_BEAST_OF            = "a:has-text('Review: Hayop, a beast of')"
    ARTICLE_NEW_ALERT           = "a:has-text('New restaurant alert: Hayop')"
    ARTICLE_SPIN_OFF_OPENING    = "a:has-text('Manam is opening a spin-off')"
    ARTICLE_SPIN_OFF_TO         = "a:has-text('Manam spin-off')"         # smart quote in full title
    ARTICLE_SPIN_OFF_IS         = "a:has-text('hayop, a Manam Spin-Off, Is')"

    # Page 4
    ARTICLE_BY_MOMENT_GROUP     = "a:has-text('Hayop by The Moment Group')"

    # --- Pagination ---
    BTN_PAGE_1 = "button:has-text('1')"
    BTN_PAGE_2 = "button:has-text('2')"
    BTN_PAGE_3 = "button:has-text('3')"
    BTN_PAGE_4 = "button:has-text('4')"
    BTN_PREV   = "button:first-of-type"
    BTN_NEXT   = "button:nth-of-type(5)"

    # --- Footer ---
    FOOTER_INSTAGRAM = "a[href='https://www.instagram.com/hayop.sg']"
    FOOTER_PRIVACY   = "a[href='https://hayopnimanam.com/privacy-policy/']"
    FOOTER_TERMS     = "a[href='https://hayopnimanam.com/terms-conditions/']"