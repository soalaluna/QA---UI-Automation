class MCL:

    MOMENT_CATERING_URL = "https://momentgroup.ph/brands/show2/moment-catering"

    # --- Hero & Brand Info ---
    HEADING_MAIN         = "role=heading[name='MOMENT CATERING']"
    TEXT_MAKE_HAPPEN     = "text=MAKE YOUR MOMENT HAPPEN"
    TEXT_EXPERIENCES     = "text=Dining experiences created"
    IMG_BRAND            = "role=img[name='Moment Catering']"
    
    # We removed the 'hide' class selector logic in the test 
    # and kept the base selector here.
    LINK_DOWNLOAD        = ".selectedbrand_download" 
    LINK_BACK_BRANDS     = "role=link[name*='Brands']"

    # --- Gallery ---
    HEADING_GALLERY      = "role=heading[name=/^GALLERY$/]"
    GALLERY_PAGINATION   = "text=1234"
    SLIDES               = [f"#slick-slide0{i}" for i in range(4)]
    GALLERY_IMGS         = [f"div:nth-child({i}) > .selectedbrand_img >> nth=0" for i in range(2, 6)]
    ACTIVE_SLIDE_IMG     = ".selectedbrand_imgHolder.slick-current > .selectedbrand_img >> nth=0"
    BTN_LIGHTBOX_CLOSE   = ".lg-close"

    # --- Cuisines ---
    HEADING_CUISINES     = "role=heading[name=/^CUISINES$/]"
    TEXT_FILIPINO        = "role=paragraph >> text=/^FILIPINO$/"
    CUISINE_INFO_1       = ".cuisine-info >> nth=0"
    CUISINE_INFO_2       = ".col-6.cuisine-2 > .cuisine-info"
    CUISINE_INFO_3       = ".col-6.cuisine-3 > .cuisine-info"
    CUISINE_INFO_4       = ".col-6.cuisine-4 > .cuisine-info"
    CUISINE_INFO_5       = ".col-6.cuisine-5 > .cuisine-info"
    
    TEXT_EUROMED         = ".EuroMed"
    TEXT_CARVINGS        = ".Carvings"
    TEXT_COCKTAILS       = ".Cocktails"
    
    # Updated to be strict about the paragraph element to avoid strict mode violations
    TEXT_COCKTAILS_DESC  = "role=paragraph >> text=/^COCKTAILS \\* SPIRITS/"

    # --- Locations ---
    HEADING_LOCATIONS    = "role=heading[name=/^LOCATIONS$/]"
    TEXT_VENUE_CATERING  = "text=VENUE CATERING"
    TEXT_BRINGS_YOUR     = "text=Moment Catering brings your"
    TEXT_ACCREDITED      = "text=ACCREDITED VENUES"
    TEXT_MOA_ARENA       = "text=The Mall of Asia Arena The"
    
    IMG_LOC_F3_1         = ".f3-img1"
    IMG_LOC_F3_2         = ".f3-img2 >> nth=0"
    IMG_LOC_F3_3         = ".f3-img3 >> nth=0"
    
    TEXT_MESS_HALL       = "role=paragraph >> text=/^MESS HALL \\+ TEST KITCHEN$/"
    LOC_ROW              = ".row.f3-inner-p2-row3"
    IMG_LOC_P2_1         = ".img-cover.loc-p2 >> nth=0"
    IMG_LOC_P2_2         = ".f3-img2.img-cover.loc-p2"

    # --- Contact / How Can We Help ---
    HEADING_HELP         = "role=heading[name='HOW CAN WE HELP?']"
    TEXT_INQUIRIES       = "text=INQUIRIES:"
    TEXT_EVENTS_EMAIL    = "text=e. events@momentgroup.ph"
    TEXT_CONCERNS        = "text=CONCERNS:"
    TEXT_SPEAK_FREELY    = "text=Email us at speakfreely@"
    TEXT_HOLLER          = "text=HOLLER AT US:"
    TEXT_HOURS           = "text=We take inquries on Mondays-"
    IMG_HELP_SECTION     = ".col-8 > .img-cover"
    
    LINK_EMAIL_ACTION    = "role=link[name='events@momentgroup.ph']"