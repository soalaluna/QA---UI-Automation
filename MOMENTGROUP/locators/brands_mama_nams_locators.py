class MNLocators:

    MAMA_NAMS_URL        = "https://momentgroup.ph/brands/show/mama-nams"

    # --- Brand Info ---
    BRAND_IMAGE          = "role=img >> nth=2"
    LINK_BACK_BRANDS     = "role=link[name*='Brands']"
    HEADING_BRAND        = "role=heading[name*='Mama Nams is a modern-day']"
    TEXT_ORDER_ONLINE    = "text=Order online via mamanams."
    HEADING_MUST_TRIES   = "role=heading[name='The Must Tries']"
    TEXT_MUST_TRIES      = "text=▪ Chicken Paa at Petso"
    CHEVRON_DOWN         = ".ion-chevron-down"

    # --- Nav Links ---
    LINK_HOURS_LOCATIONS = "role=link[name='HOURS & LOCATIONS']"
    LINK_GALLERY         = "role=link[name='GALLERY']"
    # Note: Codegen did not detect an 'ORDER NOW' anchor link for this specific page

    # --- Social Icons ---
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
        "Arnaiz": {
            "address": "role=link[name*='832A Arnaiz Avenue']",
            "phone": "role=link[name*='+63 2 8552 3739']"
        }
    }

    # --- Gallery ---
    HEADING_GALLERY      = "role=heading[name=/^Gallery$/]"
    GALLERY_IMG_FIRST    = ".selectedbrand_img >> nth=0"
    GALLERY_PAGINATION   = "text=12345"
    
    # Standard Slick slider locators 
    SLIDES               = [f"#slick-slide0{i}" for i in range(5)]
    GALLERY_IMGS         = [f"div:nth-child({i}) > .selectedbrand_img" for i in range(2, 7)]