class MenuDessertLocators:

    MENU_DESSERT_URL = "https://hayopnimanam.com/menu/?current_menu=menu-3"

    # --- Page Header ---
    TEXT_BEHIND_THE_TASTE = "text=behind the taste"

    # --- Menu Tab Navigation (swiper, scoped by carousel slide label) ---
    @staticmethod
    def swiper_tab(page, slide_label: str, tab_text: str):
        return page.get_by_label(slide_label).get_by_text(tab_text)

    TEXT_MAIN_MENU     = "text=main menu"
    TEXT_TSIBOG_COMBO  = "text=tsibog combo"
    TEXT_MINATAMIS     = "text=minatamis"
    TEXT_DRINKS        = "text=drinks"

    # --- Dessert Section ---
    @staticmethod
    def heading_dessert(page):
        return page.get_by_role("heading", name="dessert")

    @staticmethod
    def paragraph_a_la_carte(page):
        return page.get_by_role("paragraph").filter(has_text="a la carte")

    # Halo-halo
    TEXT_HALO_HALO          = "text=Halo-halo"
    TEXT_SHAVED_ICE_UBE     = "text=Shaved ice, ube halaya, nata"

    # Mais con Hielo
    TEXT_MAIS_CON_HIELO     = "text=Mais con Hielo"
    TEXT_SHAVED_ICE_CORN    = "text=Shaved ice, sweet corn milk,"

    # Manam's Ube Shake
    TEXT_UBE_SHAKE          = "text=Manam’s Ube Shake"
    TEXT_HOUSEMADE_UBE_SORBETES = "text=Housemade purple yam sorbetes, coconut cream, white sago"  # exact

    # Turon
    TEXT_TURON_14           = "text=Turon 14"

    @staticmethod
    def paragraph_crisp_caramelized_banana(page):
        return page.get_by_role("paragraph").filter(has_text="Crisp caramelized banana")

    # Buko Pie
    TEXT_BUKO_PIE           = "text=Buko Pie"
    TEXT_COCONUT_PARMESAN_CRUMBLE = "text=Coconut and parmesan crumble"

    # Patis Caramel Tart
    TEXT_PATIS_CARAMEL_TART = "text=Patis Caramel Tart"
    TEXT_DARK_CHOCOLATE_GANACHE = "text=Dark chocolate ganache with"

    # Manam's Buko Pandan Shake
    TEXT_BUKO_PANDAN_SHAKE_15 = "text=Manam's Buko Pandan Shake 15"
    TEXT_HOUSE_COCONUT_BLEND  = "text=House coconut blend, white sago, and green pandan gulaman"  # exact

    # Sorbetes
    TEXT_SORBETES_6          = "text=Sorbetes 6"
    TEXT_HOUSE_MADE_ICE_CREAM_UBE = "text=House-made ice cream Ube"