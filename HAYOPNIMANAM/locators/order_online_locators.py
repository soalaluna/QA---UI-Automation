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
    # get_by_text("Pickup")/"Delivery" without exact=True substring-matches
    # the responsive "Select a delivery/pickup location" duplicates (mobile/
    # tablet/desktop render simultaneously, hidden via CSS) -> strict mode
    # violation / flaky timing. exact=True isolates the real tab element.
    @staticmethod
    def tab_pickup(page):
        return page.get_by_text("Pickup", exact=True)

    @staticmethod
    def tab_delivery(page):
        return page.get_by_text("Delivery", exact=True)

    RADIO_OUTLET_HAYOP     = "role=radio[name='Hayop']"
    FIELD_DELIVERY_ADDRESS = "role=textbox[name='Enter a street name or postal']"
    BTN_DIALOG_CANCEL      = "role=button[name='Cancel']"
    BTN_DIALOG_CONFIRM     = "role=button[name='Confirm']"

    # --- Cart ---
    HEADING_YOUR_CART = "role=heading[name='Your cart']"

    # --- Account Menu ---
    # TODO: get_by_role("img").nth(1) now opens the CART dialog, not the
    # account menu (DOM order changed). Use Inspect Element / "Pick locator"
    # on the actual account/login icon and replace BTN_ACCOUNT_MENU below.
    BTN_ACCOUNT_MENU  = "ROLE_OR_TESTID_TBD"
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