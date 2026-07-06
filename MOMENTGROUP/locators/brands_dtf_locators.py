class DTFLocators:

    DTF_URL              = "https://momentgroup.ph/brands/show/din-tai-fung"
    ORDER_NOW_URL        = "dtf.momentfood.com"

    # --- Brand Info ---
    BRAND_IMAGE          = "role=img >> nth=2"
    LINK_BACK_BRANDS     = "role=link[name*='Brands']"
    HEADING_BRAND        = "role=heading[name*='The award-winning, half-']"
    TEXT_ORDER_ONLINE    = "text=Order online via dtf."
    HEADING_MUST_TRIES   = "role=heading[name='The Must Tries']"
    TEXT_MUST_TRIES      = "text=▪ Pork Xiaolongbao"
    CHEVRON_DOWN         = ".ion-chevron-down"
    TEXT_SOCIAL_HANDLE   = "text=@DINTAIFUNGPH"

    # --- Nav Links ---
    LINK_HOURS_LOCATIONS = "role=link[name='HOURS & LOCATIONS']"
    LINK_GALLERY         = "role=link[name='GALLERY']"
    LINK_ORDER_NOW       = "role=link[name='ORDER NOW']"

    # --- Social Icons ---
    ICON_FACEBOOK        = ".selectedbrand_icon > a > .ion-social-facebook"
    ICON_INSTAGRAM       = ".selectedbrand_icon > a > .ion-social-instagram"

    # --- Locations & Hours ---
    HEADING_LOCATIONS_HOURS = "role=heading[name='Locations & Hours']"
    TEXT_SELECT_BRANCH      = "text=Select a branch"
    BRANCH_COMBOBOX         = "role=combobox"
    MAP_CONTAINER           = "role=region[name='Map']"

    # Helper to get the clickable branch heading in the sidebar
    @staticmethod
    def heading_branch_tab(page, branch_name):
        return page.get_by_role("heading", name=branch_name).first

    # Helper to get the detail heading that appears above the address
    @staticmethod
    def heading_branch_detail(page, branch_name):
        return page.get_by_role("heading", name=branch_name).nth(1)

    # --- Branch Data Dictionary (Address contains, Phone contains) ---
    BRANCHES = {
        "SM Mall of Asia": {
            "address": "role=link[name*='Level 1 South Entertainment']",
            "phone": "role=link[name*='+63 2 8527 1364']"
        },
        "SM North Edsa": {
            "address": "role=link[name*='City Center, Level 2, SM']",
            "phone": "role=link[name*='+63 2 8459 0292']"
        },
        "Uptown": {
            "address": "role=link[name*='G/F, Uptown Parade, 36th St']",
            "phone": "role=link[name*='+632 8712 0467']"
        },
        "Alabang Town Center": {
            "address": "role=link[name*='Ground Floor, Alabang Town']",
            "phone": "role=link[name*='+63 2 8819 2010']"
        },
        "SM City Cebu": {
            "address": "a:has-text('Upper Ground Level, North')",
            "phone": "role=link[name*='+63 947 895']"
        },
        "SM City Clark": {
            "address": "role=link[name*='Level 1, SM City Clark']",
            "phone": "role=link[name*='+63 918 907']"
        },
        "Bonifacio Global City": {
            "address": "role=link[name*='L/G C1, Bonifacio High Street']",
            "phone": "role=link[name*='+63 2 8809 1865']"
        },
        "Power Plant Mall": {
            "address": "role=link[name*='R1 Level, Power Plant Mall']",
            "phone": "role=link[name*='+63 2 700 10763']"
        },
        "SM Megamall": {
            "address": "role=link[name*='G/F, SM Megamall Fashion Hall']",
            "phone": "role=link[name*='+63 919 084 5702']"
        },
        "Greenbelt": {
            "address": "role=link[name*='Level 2, Greenbelt 3']",
            "phone": "role=link[name*='+63 2 7121 1933']"
        }
    }

    # --- Gallery ---
    # Using Regex (/^ ... $/) to force an exact match without breaking the parser
    HEADING_GALLERY      = "role=heading[name=/^Gallery$/]"
    GALLERY_IMG_FIRST    = ".selectedbrand_img >> nth=0"
    GALLERY_PAGINATION   = "text=1234567"
    # Din Tai Fung has 7 pagination dots (0 to 6)
    SLIDES               = [f"#slick-slide0{i}" for i in range(7)]
    GALLERY_IMGS         = [f"div:nth-child({i}) > .selectedbrand_img" for i in range(2, 9)]