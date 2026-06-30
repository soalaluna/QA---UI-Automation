class MenuAlaCarteLocators:

    MENU_ALA_CARTE_URL = "https://hayopnimanam.com/menu/?current_menu=menu-0"

    # --- Page Header ---
    TEXT_THE_MENU         = "text=the menu"  # exact
    TEXT_BEHIND_THE_TASTE = "text=behind the taste"

    # --- Menu Tab Navigation (swiper) ---
    # The swiper-wrapper id was confirmed stale (auto-generated, doesn't
    # match the live DOM). Each carousel slide instead exposes a stable
    # accessible group name ("1 / 5", "2 / 5", ...), and "a la carte" text
    # is ambiguous on its own (also matches the page's <h1>), so we scope
    # to the specific slide group by that stable name.
    @staticmethod
    def swiper_tab(page, slide_label: str, label: str):
        return page.get_by_role("group", name=slide_label).get_by_text(label)

    TEXT_MAIN_MENU       = "text=main menu"
    TEXT_TSIBOG_COMBO    = "text=tsibog combo"
    TEXT_DESSERT_MINATAMIS = "text=dessert minatamis"
    TEXT_DRINKS_INUMIN   = "text=drinks inumin"

    # --- A La Carte Section ---
    @staticmethod
    def heading_a_la_carte(page):
        return page.get_by_role("heading", name="a la carte")

    TEXT_ABOUT_THE_MENU   = "text=about the menu"
    TEXT_FILIPINO_FOOD_AS_IT_IS = "text=Filipino food as it is, at"

    @staticmethod
    def filtered_div_filipino_food(page):
        """
        CAUTION: positional (.nth(3)) generic <div> filter -- fragile,
        see module docstring. Replace with a more specific locator if
        a stable attribute becomes available.
        """
        return page.locator("div").filter(has_text="Filipino food as it is, at").nth(3)

    TEXT_HAYOP_PANTRY_LIST = "text=While the hayop pantry list"