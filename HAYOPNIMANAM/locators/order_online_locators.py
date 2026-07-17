class OrderOnlineLocators:

    # --- URLs ---
    ORDER_ONLINE_URL = "https://hayop.atlas.kitchen/"

    # --- Header ---
    LINK_HAYOP_LOGO       = "role=link[name='Hayop']"
    BTN_DELIVERY_LOCATION = "text=Select a delivery/pickup"
    BTN_CART              = "role=button[name='$0.00']"

    # --- Menu Section Headings ---
    HEADING_BAKERY     = "role=heading[name='Bakery']"
    HEADING_STARTERS   = "role=heading[name='Starters']"
    HEADING_MAINS      = "role=heading[name='Mains']"
    HEADING_VEGETABLES = "role=heading[name='Vegetables']"
    HEADING_RICE       = "role=heading[name='Rice']"
    HEADING_DESSERTS   = "role=heading[name='Desserts']"

    # --- Menu Items (sample set, by data-testid) ---
    ITEM_ENSAYMADA          = "[data-testid='Ensaymada-menu-item']"
    ITEM_CHICHARON_BULAKLAK = "[data-testid='Chicharon Bulaklak-menu-item']"
    ITEM_ADOBONG_PULA       = "[data-testid='Adobong Pula-menu-item']"
    ITEM_BUKO_PIE           = "[data-testid='Buko Pie-menu-item']"

    # --- Menu Item Detail Modal ---
    BTN_MODAL_CLOSE = "role=button[name='Close']"
    BTN_ITEM_ADD    = "[data-testid='Ensaymada-menu-item'] >> [data-testid='button']"

    # --- Delivery/Pickup Dialog ---
    # Tabs are targeted via their stable DOM IDs (#pickup / #delivery) rather
    # than text matching — the site renders both tabs as plain <a> elements
    # inside the same nav, and ID selectors avoid any risk of duplicate/
    # responsive text nodes or accessibility-tree timing quirks.
    @staticmethod
    def tab_pickup(page):
        return page.locator("#pickup")

    @staticmethod
    def tab_delivery(page):
        return page.locator("#delivery")

    RADIO_OUTLET_HAYOP     = "role=radio[name='Hayop']"

    # Changed from exact match to contains match: the field's real accessible
    # name is "Enter a street name or postal code" (previous string was
    # missing the trailing word "code", so exact matching never found it).
    FIELD_DELIVERY_ADDRESS = "role=textbox[name*='street name or postal']"

    BTN_DIALOG_CANCEL      = "role=button[name='Cancel']"
    BTN_DIALOG_CONFIRM     = "role=button[name='Confirm']"

    # --- Cart ---
    HEADING_YOUR_CART = "role=heading[name='Your cart']"

    # --- Account Menu ---
    # The account icon is a plain <div> (no button/link role, no alt text) —
    # an SVG person-silhouette wrapped in a rounded div. Confirmed via debug
    # test: clicking it reveals "Sign up" / "Log in" menu items.
    BTN_ACCOUNT_MENU  = "div.rounded-full.bg-header"
    MENU_ITEM_SIGNUP  = "role=menuitem[name='Sign up']"
    MENU_ITEM_LOGIN   = "role=menuitem[name='Log in']"

    # --- Footer ---
    HEADING_FIND_US         = "role=heading[name='Find us']"
    LINK_ADDRESS            = "role=link[name='104 Amoy Street, Singapore 069924']"
    HEADING_OPERATING_HOURS = "role=heading[name='Operating Hours']"
    HEADING_SOCIAL          = "role=heading[name='Social']"
    LINK_MAKE_RESERVATION   = "role=link[name='Make a reservation']"
    LINK_ATLAS_WEBSITE      = "role=link[name='atlas website']"
    SCROLLER_TOP_BTN        = "#scroller"