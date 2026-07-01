class MenuLunchLocators:

    MENU_LUNCH_SETS_URL = "https://hayopnimanam.com/menu/?current_menu=menu-2"

    # --- Page Header ---
    TEXT_BEHIND_THE_TASTE = "text=behind the taste"

    # --- Menu Tab Navigation (swiper, scoped by carousel slide label) ---
    @staticmethod
    def swiper_tab(page, slide_label: str, tab_text: str):
        return page.get_by_label(slide_label).get_by_text(tab_text)

    TEXT_MAIN_MENU         = "text=main menu"
    TEXT_TSIBOG_COMBO      = "text=tsibog combo"
    TEXT_MINATAMIS         = "text=minatamis"
    TEXT_DRINKS            = "text=drinks"

    # --- Lunch Sets Section ---
    @staticmethod
    def heading_lunch_sets(page):
        return page.get_by_role("heading", name="lunch sets")

    TEXT_COMES_WITH_CHOICE = "text=comes with your choice of"

    # Lechon Kawali
    @staticmethod
    def span_lechon_kawali(page):
        return page.locator("span").filter(has_text="Lechon Kawali")

    @staticmethod
    def paragraph_golden_fried_duroc(page):
        return page.get_by_role("paragraph").filter(has_text="Golden fried Grain-fed Duroc")

    # Inihaw na Baboy
    TEXT_INIHAW_NA_BABOY     = "text=Inihaw na Baboy"
    TEXT_OVEN_BRAISED        = "text=Oven-braised then Charcoal-"

    # Adobong Pula
    TEXT_ADOBONG_PULA        = "text=Adobong Pula"
    TEXT_CORN_FED_CHICKEN    = "text=Corn-fed heritage French chicken and fried chicken flakes Sukang Sasa, toyo,"

    # Adobong Dilaw
    @staticmethod
    def span_adobong_dilaw(page):
        return page.locator("span").filter(has_text="Adobong Dilaw")

    TEXT_GRAIN_FED_DUROC_TURMERIC = "text=Grain-fed Duroc pork belly Turmeric, sukang tuba, ginger, calamansi"  # exact

    # Chicken Inasal
    TEXT_CHICKEN_INASAL_29   = "text=Chicken Inasal 29"
    TEXT_CHARCOAL_GRILLED_HALF_CHICKEN = "text=Charcoal-grilled corn-fed heritage French spring half chicken Annatto,"

    # Inasal na Panga
    TEXT_INASAL_NA_PANGA     = "text=Inasal na Panga 36 P"

    @staticmethod
    def paragraph_charcoal_grilled_maguro_jaw(page):
        return page.get_by_role("paragraph").filter(has_text="Charcoal-grilled maguro jaw")

    # Manam's Crispy Palabok
    @staticmethod
    def span_crispy_palabok(page):
        return page.locator("span").filter(has_text="Manam’s Crispy Palabok")

    TEXT_CHARRED_BABY_CUTTLEFISH = "text=Charred baby cuttlefish,"

    # Manam's Tapsilog
    TEXT_TAPSILOG             = "text=Manam’s Tapsilog"
    TEXT_HOUSE_CURED_ANGUS    = "text=Manam’s house-cured Angus"

    # Wild Mushroom & Tofu Kare-Kare
    @staticmethod
    def span_wild_mushroom_kare_kare(page):
        return page.locator("span").filter(has_text="Wild Mushroom & Tofu Kare-")

    TEXT_MAITAKE_PORTOBELLO   = "text=Maitake, Portobello, King Oyster, fried tofu and tofu pillow Peanut and miso"

    # --- Top Up Section ---
    @staticmethod
    def heading_top_up(page):
        return page.get_by_role("heading", name="top up")

    TEXT_PLUS_7_VEG_OR_DESSERT = "text=+$7 for vegetable or dessert"
    TEXT_CHOICE_OF_VEGETABLES  = "text=choice of vegetables"

    # Gising Gising
    TEXT_GISING_GISING        = "text=Gising Gising P"

    @staticmethod
    def paragraph_winged_bean_tofu(page):
        return page.get_by_role("paragraph").filter(has_text="Winged bean and tofu crumble")

    # Laing
    TEXT_LAING                = "text=Laing P"
    TEXT_TARO_LEAVES_COCONUT  = "text=Taro leaves in coconut Bagoong, fish sauce, bird’s eye chili"

    @staticmethod
    def paragraph_sauteed_kale(page):
        return page.get_by_role("paragraph").filter(has_text="Sautéed kale Spinach, garlic")

    # Adobong Gulay
    TEXT_ADOBONG_GULAY        = "text=Adobong Gulay P"
    TEXT_CHOICE_OF_DESSERT    = "text=choice of dessert"

    # Turon
    TEXT_TURON                = "text=Turon"  # exact

    @staticmethod
    def paragraph_crisp_caramelized_banana(page):
        return page.get_by_role("paragraph").filter(has_text="Crisp caramelized banana")

    # Ensaymada
    TEXT_ENSAYMADA            = "text=Ensaymada"
    TEXT_WARM_HOUSE_MADE_BRIOCHE = "text=Warm house-made brioche"