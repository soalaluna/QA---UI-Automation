class ContactUsLocators:

    URL = "https://www.pldtglobal.com/en/contact-us"

    # --- Hero Section ---
    HEADING_MAIN          = "role=heading[name='Contact Us']"
    TEXT_INTRO            = "text=We're here to support your"
    IMG_HERO              = "role=figure >> img"

# --- Form Tabs ---
    HEADING_EXPLORE       = "role=heading[name*='Reach Out and Explore']"
    TEXT_EXPLORE_DESC     = "text=Reach out to learn how our"
    
    TAB_CONSUMER          = "role=button[name='Consumer']"
    TAB_ENTERPRISE        = "role=button[name='Enterprise']"
    TAB_CARRIER           = "role=button[name='Carrier']"
    
    # --- Form Section Headers ---
    TEXT_CONSUMER_TITLE   = "text=All Consumer Inquiries >> nth=0"
    TEXT_ENTERPRISE_TITLE = "text=Global Enterprise >> nth=0"
    TEXT_CARRIER_TITLE    = "text=Carrier Voice >> nth=0"

    BTN_SUBMIT            = "role=button[name='Submit form']"
    
    # --- Data Collection Section ---
    HEADING_DATA          = "role=heading[name='Purpose of Data Collection']"
    TEXT_DATA_DESC        = "text=This collected information is"

    # --- Direct Contact / Sidebar ---
    HEADING_DIRECTLY      = "role=heading[name='Reach Us Directly']"
    TEXT_DIRECTLY_DESC    = "text=Connect with us through phone"
    
    LINK_EMAIL            = "#main >> role=link[name='askus@pldtglobal.com']"
    LINK_PHONE            = "#main >> role=link[name*='(+632) 8886-']"
    LINK_ADDRESS          = "role=link[name*='12F Rufino Pacific Tower']"
    LINK_LINKEDIN         = "role=link[name*='linkedin.com/company/']"
    MAP_IFRAME            = "iframe[title='Location in Google Maps']"

    # --- Form Fields Dictionaries ---
    FIELDS_CONSUMER = [
        "text=Salutation *",
        "role=textbox[name='First Name required']",
        "role=textbox[name='Last Name required']",
        "role=textbox[name='Company required']",
        "role=textbox[name='Email Address required']",
        "text=Industry *",
        "text=Position/Job Title *",
        "role=textbox[name='Message required']"
    ]

    FIELDS_ENTERPRISE = [
        "text=Salutation *",
        "role=textbox[name='First Name required']",
        "role=textbox[name='Last Name required']",
        "role=textbox[name='Company required']",
        "role=textbox[name='Email Address required']",
        "role=textbox[name='Phone required']",
        "role=textbox[name='Mobile required']",
        "text=Industry *",
        "role=textbox[name='City required']",
        "role=textbox[name='State/Province required']",
        "role=textbox[name='Country required']",
        "role=textbox[name='Region required']"
    ]

    FIELDS_CARRIER = [
        "text=Salutation *",
        "role=textbox[name='First Name required']",
        "role=textbox[name='Company required']",
        "role=textbox[name='Phone required']",
        "role=textbox[name='Last Name required']",
        "role=textbox[name='Email Address required']",
        "role=textbox[name='Mobile required']",
        "text=Industry *",
        "role=textbox[name='State/Province required']",
        "role=textbox[name='City required']",
        "role=textbox[name='Country required']",
        "role=textbox[name='Region required']"
    ]