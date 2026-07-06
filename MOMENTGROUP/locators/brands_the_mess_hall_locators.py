class TMHLocators:

    THE_MESS_HALL_URL    = "https://momentgroup.ph/brands/show/the-mess-hall"
    ORDER_NOW_URL        = "momentfood.com" # Broadened to catch any momentfood subdomain

    # --- Brand Info ---
    BRAND_IMAGE          = "role=img >> nth=2"
    LINK_BACK_BRANDS     = "role=link[name*='Brands']"
    HEADING_BRAND        = "role=heading[name*='Our neighborhood cafeteria']"
    TEXT_INTRO           = "text=The Moment Group’s private"
    HEADING_MUST_TRIES   = "role=heading[name='The Must Tries']"
    TEXT_MUST_TRIES      = "text=▪ Manam House Crispy Sisig ▪"
    CHEVRON_DOWN         = ".ion-chevron-down"
    TEXT_SOCIAL_HANDLE   = "text=@THEMOMENTGROUP"

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
    MAP_CONTAINER           = "role=region[name='Map']"

    @staticmethod
    def heading_branch_tab(page, branch_name):
        return page.get_by_role("heading", name=branch_name, exact=True).first

    @staticmethod
    def heading_branch_detail(page, branch_name):
        return page.get_by_role("heading", name=branch_name).last

    # --- Branch Data Dictionary (Address contains, Phone contains) ---
    BRANCHES = {
        "The Moplex": {
            "address": "role=link[name*='2316 Karrivin Plaza, Chino']",
            "phone": "role=link[name*='09190845719']"
        }
    }

    # --- Gallery ---
    HEADING_GALLERY      = "role=heading[name=/^Gallery$/]"
    GALLERY_IMG_FIRST    = ".selectedbrand_img >> nth=0"
    GALLERY_PAGINATION   = "text=12345678910111213"
    
    # The Mess Hall has 13 slides (indices 0 to 12). 
    # Notice Slick slider appends the index raw, so index 10 becomes #slick-slide010
    SLIDES               = [f"#slick-slide0{i}" for i in range(13)]
    
    # The CSS layout uses nth-child(2) through nth-child(14) for the 13 images
    GALLERY_IMGS         = [f"div:nth-child({i}) > .selectedbrand_img" for i in range(2, 15)]