class MCLocators:

    MO_COOKIES_URL       = "https://momentgroup.ph/brands/show/mo-cookies"
    ORDER_NOW_URL        = "mo.momentfood.com"

    # --- Brand Info ---
    BRAND_IMAGE          = ".selectedbrand_logo"
    LINK_BACK_BRANDS     = "role=link[name*='Brands']" # Fixed icon parsing
    HEADING_BRAND        = "role=heading[name*='The OG #biggerthanyourpalm']"
    TEXT_ORDER_ONLINE    = "text=Order online via mo."
    HEADING_MUST_TRIES   = "role=heading[name='The Must Tries']"
    TEXT_MUST_TRIES      = "text=▪ Chocolate Chip ▪ South"
    CHEVRON_DOWN         = ".ion-chevron-down"
    TEXT_SOCIAL_HANDLE   = "text=@MOCOOKIESFORYOU"

    # --- Nav Links ---
    LINK_HOURS_LOCATIONS = "role=link[name='HOURS & LOCATIONS']"
    LINK_GALLERY         = "role=link[name='GALLERY']"
    LINK_ORDER_NOW       = "role=link[name='ORDER NOW']"

    # --- Social Icons ---
    BRAND_ICON_FIRST     = ".selectedbrand_icon >> nth=0"
    SOCIAL_MEDIA_SECOND  = ".selectedbrand_socialmediaHolder > .inlineBlock-parent > div:nth-child(2)"
    ICON_FACEBOOK        = ".selectedbrand_icon > a > .ion-social-facebook"
    ICON_INSTAGRAM       = ".selectedbrand_icon > a > .ion-social-instagram"

    # --- Locations & Hours ---
    HEADING_LOCATIONS_HOURS = "role=heading[name='Locations & Hours']"
    TEXT_SELECT_BRANCH      = "text=Select a branch"
    BRANCH_COMBOBOX         = "role=combobox"
    MAP_CONTAINER           = "role=region[name='Map']" # Fixed map locator

    # Helper to get the clickable branch heading in the sidebar
    @staticmethod
    def heading_branch_tab(page, branch_name):
        # Added exact=True back so it doesn't click the main page title!
        return page.get_by_role("heading", name=branch_name, exact=True).first

    # Helper to get the detail heading that appears above the address
    @staticmethod
    def heading_branch_detail(page, branch_name):
        # We use .last here because depending on the branch list, it might be the 2nd or 3rd instance
        return page.get_by_role("heading", name=branch_name).last

    # --- Branch Data Dictionary (Address contains, Phone contains) ---
    # Using the '*=' contains logic to avoid truncation errors
    BRANCHES = {
        "Glorietta 4": {    # <--- Changed this from "Glorietta"
            "address": "role=link[name*='Food Choices, 3rd Floor']",
            "phone": "role=link[name*='+63 919 084']"
        },
        "SM Megamall": {
            "address": "role=link[name*='Ground Floor, Mega Fashion']",
            "phone": "role=link[name*='+63 919 084']"
        },
        "Alabang Town Center": {
            "address": "role=link[name*='Upper Ground Floor, Activity']",
            "phone": "role=link[name*='+63 919 073']"
        },
        "Robinsons Place Manila": {
            "address": "role=link[name*='Ground Floor, Pedro Gil Wing']",
            "phone": "role=link[name*='+63 919 084']"
        },
        "Uptown Mall": {
            "address": "role=link[name*='Upper Ground Floor, Uptown']",
            "phone": "role=link[name*='+63 919 084']"
        },
        "Robinsons Magnolia": {
            "address": "role=link[name*='Upper Ground Floor, Robinsons']",
            "phone": "role=link[name*='+63 968 869']"
        },
        "Mall of Asia": {
            "address": "role=link[name*='Level 1, South Entertainment']",
            "phone": "role=link[name*='+63 939 978']"
        },
        "SM North EDSA": {
            "address": "role=link[name*='2nd flr. City Center, SM']",
            "phone": "role=link[name*='+63 919 084']"
        },
        "Greenhills": {
            "address": "a:has-text('G/F Greenhills Mall, Ortigas')",
            "phone": "role=link[name*='+63 919 007']"
        },
        "SM City Cebu": {
            "address": "role=link[name*='Upper Ground Level, North']",
            "phone": "role=link[name*='+63 939 984']"
        },
        "SM City Clark": {
            "address": "role=link[name*='Ground Level, East Mall, SM']",
            "phone": "role=link[name*='+63 998 850']"
        },
        "The Mess Hall": {
            "address": "role=link[name*='2316 Karrivin Plaza, Chino']",
            "phone": "role=link[name*='+63 919 084']"
        },
        "Power Plant Mall": {
            "address": "role=link[name*='Power Plant Mall Rockwell']",
            "phone": "role=link[name*='+63 919 073']"
        }
    }

    # --- Gallery ---
    HEADING_GALLERY      = "role=heading[name=/^Gallery$/]" # Fixed exact match error
    GALLERY_IMG_FIRST    = ".selectedbrand_img >> nth=0"
    GALLERY_PAGINATION   = "text=12345"
    # Mo' Cookies has 5 pagination dots (0 to 4)
    SLIDES               = [f"#slick-slide0{i}" for i in range(5)]
    GALLERY_IMGS         = [f"div:nth-child({i}) > .selectedbrand_img" for i in range(2, 7)]