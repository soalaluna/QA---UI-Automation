class PPLocators:

    PANCIT_URL           = "https://momentgroup.ph/brands/show/pancit-pancitan"
    ORDER_NOW_URL        = "momentfood.com"

    # --- Brand Info ---
    BRAND_IMAGE          = "#selectedbrandpage >> role=img >> nth=0"
    LINK_BACK_BRANDS     = "role=link[name*='Brands']"
    HEADING_BRAND        = "role=heading[name*=\"Moment's first delivery-only\"]"
    TEXT_ORDER_ONLINE    = "text=Order online via"
    HEADING_MUST_TRIES   = "role=heading[name='The Must Tries']"
    TEXT_MUST_TRIES      = "text=▪ Pancit Sisig ▪ Pancit Squid"
    CHEVRON_DOWN         = ".ion-chevron-down"
    TEXT_SOCIAL_HANDLE   = "text=@pancitpancitan"

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
        "Alabang": {
            "address": "role=link[name*='GF Building 8, Molito']",
            "phone": "role=link[name*='+63 9190 845']"
        },
        "Makati": {
            "address": "role=link[name*='R3, Power Plant Mall']",
            "phone": "role=link[name*='+63 9190 733']"
        },
        "Manila": {
            "address": "role=link[name*='L1, Midtown Wing Robinson’s']",
            "phone": "role=link[name*='+63 9190 845']"
        },
        "Bacoor": {
            "address": "role=link[name*='Upper Ground Level, SM City']",
            "phone": "role=link[name*='+63 9190 845']"
        },
        "Baguio": {
            "address": "role=link[name*='Upper Ground Level, Sunset']",
            "phone": "role=link[name*='4246 4003']"
        },
        "BGC": {
            "address": "role=link[name*='G/F, Net Park, 4th Avenue']",
            "phone": "role=link[name*='+63 9190 845']"
        },
        "Clark": {
            "address": "role=link[name*='G/F, Manuel A. Roxas Hwy']",
            "phone": "role=link[name*='499 7548']"
        },
        "Cubao": {
            "address": "role=link[name*='Coliseum Plaza, GF Gateway']",
            "phone": "role=link[name*='+63 2 7001']"
        },
        "Eastwood": {
            "address": "role=link[name*='Ground Floor, Eastwood Mall']",
            "phone": "role=link[name*='4246 4003']"
        },
        "Fairview": {
            "address": "role=link[name*='Lower Ground Level, Parkway']",
            "phone": "role=link[name*='+63 9620 893']"
        },
        "Malolos": {
            "address": "role=link[name*='Level 1, Robinsons Malolos']",
            "phone": "role=link[name*='4792 5263']"
        },
        "Mandaluyong": {
            "address": "role=link[name*='3/F Mega Fashion Hall, SM']",
            "phone": "role=link[name*='+63 2 8370']"
        },
        "Muntinlupa": {
            "address": "role=link[name*='Upper Ground Floor of']",
            "phone": "role=link[name*='+63 9690 493']"
        },
        "New Manila": {
            "address": "role=link[name*='Space 01166 level 1 Robinson']",
            "phone": "role=link[name*='+63 2 8584']"
        },
        "SM North EDSA": {
            "address": "role=link[name*='2/F, City Center, SM City']",
            "phone": "role=link[name*='+63 2 8367']"
        },
        "Ortigas": {
            "address": "role=link[name*='G/F, The Podium, ADB Avenue']",
            "phone": "role=link[name*='+63 9190 845']"
        },
        "Parañaque": {
            "address": "role=link[name*='Ground Floor, Ayala Malls']",
            "phone": "role=link[name*='+63 9190 733']"
        }
    }

    # --- Gallery ---
    HEADING_GALLERY      = "role=heading[name=/^Gallery$/]"
    GALLERY_IMG_FIRST    = ".selectedbrand_img >> nth=0"
    GALLERY_PAGINATION   = "text=12345"
    
    # Pancit Pancitan has 5 slides (indices 0 to 4)
    SLIDES               = [f"#slick-slide0{i}" for i in range(5)]
    GALLERY_IMGS         = [f"div:nth-child({i}) > .selectedbrand_img" for i in range(2, 7)]