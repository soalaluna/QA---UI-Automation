class MenuDrinksLocators:

    MENU_DRINKS_URL = "https://hayopnimanam.com/menu/?current_menu=menu-4"

    # --- Alcoholic Section (inuman) ---
    @staticmethod
    def heading_alcoholic_inuman(page):
        return page.get_by_role("heading", name="alcoholic inuman")

    TEXT_COCKTAILS_22       = "text=Cocktails 22 $"
    TEXT_ALAT_SALTY         = "text=Alat | Salty Tequila, Fresh"
    TEXT_ASIM_SOUR          = "text=Asim | Sour Sloe Gin,"
    TEXT_TAMIS_SWEET        = "text=Tamis | Sweet Sake, Chamomile"
    TEXT_ANGHANG_SPICY      = "text=Anghang | Spicy Vodka,"
    TEXT_MALINAMNAM_UMAMI   = "text=Malinamnam | Umami Coconut"
    TEXT_PAIT_BITTER        = "text=Pait | Bitter Dark Rum, Decaf"

    TEXT_PHILIPPINE_BEERS   = "text=Philippine Beers"

    @staticmethod
    def listitem_san_miguel_light(page):
        return page.get_by_role("listitem").filter(has_text="San Miguel Light 15 $")

    @staticmethod
    def listitem_engkanto(page):
        return page.get_by_role("listitem").filter(has_text="Engkanto 18 $")

    @staticmethod
    def listitem_wines_sakes(page):
        return page.get_by_role("listitem").filter(has_text="Wines & Sakes")

    @staticmethod
    def listitem_please_ask(page):
        return page.get_by_role("listitem").filter(has_text="Please ask for our")

    # --- Non-Alcoholic Section (inumin) ---
    @staticmethod
    def heading_non_alcoholic_inumin(page):
        return page.get_by_role("heading", name="non-alcoholic inumin")

    TEXT_SHAKES_15          = "text=Shakes 15 $"
    TEXT_UBE_SHAKE_HOUSEMADE = "text=Manam's Ube Shake Housemade"
    TEXT_BUKO_PANDAN_SHAKE  = "text=Manam's Buko Pandan Shake House coconut blend, white sago, and green pandan"

    TEXT_CANNED_SODAS_6     = "text=Canned Sodas 6 $"
    TEXT_COCA_COLA          = "text=Coca-Cola"
    TEXT_SPRITE             = "text=Sprite"

    TEXT_COFFEE             = "text=Coffee"  # exact
    TEXT_ESPRESSO_4_5       = "text=Espresso 4.5 $"
    TEXT_BLACK_COFFEE_5     = "text=Black Coffee 5 $"
    TEXT_FLAT_WHITE_6       = "text=Flat White 6 $"
    TEXT_LATTE_6            = "text=Latte 6 $"
    TEXT_CAPPUCCINO_6       = "text=Cappuccino 6 $"

    @staticmethod
    def listitem_tea_6(page):
        return page.get_by_role("listitem").filter(has_text="Tea 6 $")

    TEXT_OOLONG_TEA         = "text=Oolong Tea"
    TEXT_GREEN_TEA          = "text=Green Tea"
    TEXT_CHAMOMILE_TEA      = "text=Chamomile Tea"