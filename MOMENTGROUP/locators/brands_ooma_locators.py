class OomaLocators:

    OOMA_URL             = "https://momentgroup.ph/brands/show/ooma"
    HOURS_LOCATIONS_URL  = "https://momentgroup.ph/brands/show/ooma#hours-and-locations"
    GALLERY_URL          = "https://momentgroup.ph/brands/show/ooma#gallery"
    ORDER_NOW_URL        = "https://ooma.momentfood.com/"

    # --- Brand Info ---
    BRAND_IMAGE          = "role=img"          # nth(2) in tests
    LINK_BACK_BRANDS     = "role=link[name*='Brands']" # Fixed icon spacing issue

    @staticmethod
    def heading_brand(page):
        return page.get_by_role("heading", name="A bold take on Japanese")

    TEXT_ORDER_ONLINE    = "text=Order online via ooma."
    HEADING_MUST_TRIES   = "role=heading[name='The Must Tries']"
    TEXT_MUST_TRIES      = "text=▪ Ebi Tempura ▪ Hanger Steak"
    CHEVRON_DOWN         = ".ion-chevron-down"
    TEXT_SOCIAL_HANDLE   = "text=@OOMA_PH"

    # --- Nav Links ---
    LINK_HOURS_LOCATIONS = "role=link[name='HOURS & LOCATIONS']"
    LINK_GALLERY         = "role=link[name='GALLERY']"
    LINK_ORDER_NOW       = "role=link[name='ORDER NOW']"

    # --- Social Icons ---
    BRAND_ICON_FIRST     = ".selectedbrand_icon"   # .first in tests
    SOCIAL_MEDIA_SECOND  = ".selectedbrand_socialmediaHolder > .inlineBlock-parent > div:nth-child(2)"
    ICON_FACEBOOK        = ".selectedbrand_icon > a > .ion-social-facebook"
    ICON_INSTAGRAM       = ".selectedbrand_icon > a > .ion-social-instagram"

    # --- Locations & Hours (shared across branches) ---
    @staticmethod
    def heading_locations_hours(page):
        return page.get_by_role("heading", name="Locations & Hours")

    TEXT_LOCATIONS_HOURS_INTRO = "text=Locations & Hours SM City"
    TEXT_SELECT_BRANCH         = "text=Select a branch"
    BRANCH_COMBOBOX            = "role=combobox"
    
    # Fixed broken Google maps inner container
    MAP_CONTAINER              = "role=region[name='Map']" 

    # --- Branch: SM City Cebu (default) ---
    @staticmethod
    def heading_sm_cebu_first(page):
        return page.get_by_role("heading", name="SM City Cebu").first

    @staticmethod
    def heading_sm_cebu_detail(page):
        return page.get_by_role("heading", name="SM City Cebu").nth(1)

    LINK_SM_CEBU_ADDRESS  = "a:has-text('Upper Ground Level, North')"
    LINK_SM_CEBU_PHONE    = "role=link[name='+63 939 970 0170\u202c']"
    TEXT_SM_CEBU_HOURS    = "text=10AM - 9PM (Mon-Thurs) 10AM"

    # --- Branch: Bonifacio High Street ---
    @staticmethod
    def heading_bhs(page):
        return page.get_by_role("heading", name="Bonifacio High Street")

    @staticmethod
    def heading_bhs_detail(page):
        return page.get_by_role("heading", name="Bonifacio High Street").nth(1)

    LINK_BHS_ADDRESS     = "role=link[name*='L1, C3 Bonifacio High Street']" # Fixed truncation
    LINK_BHS_PHONE       = "role=link[name*='+63 919 084']"
    TEXT_BHS_HOURS       = "text=AM-10 PM (Mon-Sun)"

    # --- Branch: Greenbelt ---
    @staticmethod
    def heading_greenbelt(page):
        return page.get_by_role("heading", name="Greenbelt")

    @staticmethod
    def heading_greenbelt_detail(page):
        return page.get_by_role("heading", name="Greenbelt").nth(1)

    LINK_GREENBELT_ADDRESS = "role=link[name*='Level 2, Greenbelt 3']" # Fixed truncation
    LINK_GREENBELT_PHONE   = "role=link[name*='+63 2 7576 8446']"
    TEXT_GREENBELT_HOURS   = "text=11AM-9PM (Mon-Sunday)"

    # --- Branch: Power Plant Mall ---
    @staticmethod
    def heading_power_plant(page):
        return page.get_by_role("heading", name="Power Plant Mall")

    @staticmethod
    def heading_power_plant_detail(page):
        return page.get_by_role("heading", name="Power Plant Mall").nth(1)

    LINK_POWER_PLANT_ADDRESS = "role=link[name*='Concourse Level, Power Plant']" # Fixed truncation
    LINK_POWER_PLANT_PHONE   = "role=link[name*='+63 919 084']"
    TEXT_POWER_PLANT_HOURS   = "text=11 AM-9 PM (Mon-Fri) 10 AM-10"

    # --- Branch: Salcedo ---
    @staticmethod
    def heading_salcedo(page):
        return page.get_by_role("heading", name="Salcedo")

    @staticmethod
    def heading_salcedo_detail(page):
        return page.get_by_role("heading", name="Salcedo").nth(1)

    LINK_SALCEDO_ADDRESS = "role=link[name*='G/F, Paseo Heights']" # Fixed truncation
    LINK_SALCEDO_PHONE   = "role=link[name*='+63 2 8814 3795']"
    TEXT_SALCEDO_HOURS   = "text=AM-11 PM (Mon-Sun)"

    # --- Branch: SM Megamall ---
    @staticmethod
    def heading_sm_megamall(page):
        return page.get_by_role("heading", name="SM Megamall")

    @staticmethod
    def heading_sm_megamall_detail(page):
        return page.get_by_role("heading", name="SM Megamall").nth(1)

    LINK_SM_MEGAMALL_ADDRESS = "role=link[name*='3F, Mega Fashion Hall']" # Fixed truncation
    LINK_SM_MEGAMALL_PHONE   = "role=link[name*='+63 919 084']"
    TEXT_SM_MEGAMALL_HOURS   = "text=AM-10 PM (Mon-Sun)"

    # --- Branch: Molito ---
    @staticmethod
    def heading_molito(page):
        return page.get_by_role("heading", name="Molito")

    @staticmethod
    def heading_molito_detail(page):
        return page.get_by_role("heading", name="Molito").nth(1)

    LINK_MOLITO_ADDRESS  = "a:has-text('GF Building 8, Molito')"
    LINK_MOLITO_PHONE    = "role=link[name*='+63 2 8256 3621']" # Fixed truncation
    TEXT_MOLITO_HOURS    = "text=AM-10 PM (Mon-Sun)"

    # --- Gallery ---
    @staticmethod
    def heading_gallery(page):
        return page.get_by_role("heading", name="Gallery", exact=True)

    GALLERY_IMG_FIRST    = ".selectedbrand_img"       # .first in tests
    GALLERY_PAGINATION   = "text=12345678"
    # Slick slide dot IDs for navigation
    SLIDES = [f"#slick-slide0{i}" for i in range(8)]
    # nth-child CSS selectors for each gallery image (1-indexed in CSS = slides 1-8)
    GALLERY_IMGS = [f"div:nth-child({i}) > .selectedbrand_img" for i in range(2, 10)]