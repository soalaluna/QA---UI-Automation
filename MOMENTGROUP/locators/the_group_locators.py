class TGLocators:

    URL = "https://momentgroup.ph/the-group"

    # --- Navigation / Breadcrumbs ---
    TAB_THE_GROUP        = "#breadcrumbs-1 >> role=heading[name='The Group']"
    TAB_ABOUT            = "role=heading[name='About'] >> nth=0"
    TAB_PARTNERSHIPS     = "#breadcrumbs-3 >> role=heading[name='Partnerships']"
    TAB_MILESTONES       = "#breadcrumbs-4 >> role=heading[name='Milestones']"
    
    # --- Hero Section ---
    HEADING_MAIN         = "#thegroup_frame1 >> role=heading[name='The Group']"
    TEXT_CREATION        = "text=\"We're all about the creation"
    IMG_BACKGROUND       = ".frame__background >> nth=0"

    # --- About Section ---
    HEADING_BUSINESS     = "role=heading[name='The Business of Food']"
    TEXT_ABOUT_1         = "text=Since 2012, The Moment Group"
    TEXT_ABOUT_2         = "text=In its rosters are Manam"
    TEXT_ABOUT_3         = "text=In 2024, Moment opened its"
    TEXT_ABOUT_4         = "text=At the inaugural launch of >> nth=0"
    TEXT_ABOUT_5         = "text=Now more than 5,000 people"

    # --- The Founders Section ---
    # Added >> nth=0 to fix strict mode violation
    TAB_FOUNDERS         = "role=heading[name*='The Founders'] >> nth=0"
    ICON_FOUNDERS_EXPAND = "role=heading[name*='The Founders'] >> i"
    HEADING_FOUNDERS_ALT = "role=heading[name='The Founders'] >> nth=1"
    
    FOUNDER_ABBA         = "role=heading[name='Abba Napa']"
    ABBA_ROLE            = "role=paragraph >> text=Founder for Creative"
    ABBA_BIO             = "role=paragraph >> text=Abba Napa is an entrepreneur"
    
    FOUNDER_ELIZA        = "role=heading[name='Eliza Antonino']"
    ELIZA_ROLE           = "role=paragraph >> text=Founder and Managing Partner"
    ELIZA_BIO            = "role=paragraph >> text=Eliza Antonino has a career"
    
    FOUNDER_JON          = "role=heading[name='Jon Syjuco']"
    JON_ROLE             = "role=paragraph >> text=Founder for Strategic"
    JON_BIO              = "role=paragraph >> text=Raised in a family with a"

    # --- Partnerships Section ---
    HEADING_PARTNERSHIPS = "#thegroup_frame3-partner >> role=heading[name='Partnerships']"
    TEXT_INTERESTED      = "text=Interested in doing business"

    # --- Milestones Section ---
    HEADING_MILESTONES   = "#thegroup_frame4 >> role=heading[name='Milestones']"
    SLIDER_CONTAINER     = ".year-slider"
    BTN_NEXT             = "role=button[name='Next']"
    BTN_PREV             = "role=button[name='Previous']"
    
    # Updated to years proven to exist in the immediate slider chunk
    MILESTONE_2012       = "role=option[name*='2012']"
    MILESTONE_2013       = "role=option[name*='2013']"
    MILESTONE_2014       = "role=option[name*='2014']"
    MILESTONE_2017       = "role=option[name*='2017']"