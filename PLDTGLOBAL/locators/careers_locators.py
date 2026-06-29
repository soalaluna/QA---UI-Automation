class CareersLocators:

    # --- URLs ---
    BASE_URL    = "https://www.pldtglobal.com/en"
    CAREERS_URL = "https://www.pldtglobal.com/en/careers"

    # --- Navigation ---
    NAV_CAREERS = "nav >> role=link[name='Careers']"

    # --- Job Listing Cards ---
    LINK_APPLY        = "role=link[name='Apply']"
    LINK_GO_TO_LINKEDIN = "role=link[name='Go to LinkedIn']"  # opens popup
    LINK_APPLY_NOW     = "role=link[name='Apply Now']"        # page footer CTA

    # --- Application Form ---
    BTN_SUBMIT_APPLICATION_FORM = "role=button[name='Submit Application Form']"
    FIELD_SALUTATION             = "role=combobox[name='Salutation *']"
    FIELD_FIRST_NAME             = "role=textbox[name='First Name *']"
    FIELD_LAST_NAME              = "role=textbox[name='Last Name *']"
    FIELD_EMAIL                  = "role=textbox[name='Email Address *']"
    FIELD_CONTACT_NUMBER         = "role=textbox[name='Contact No. *']"
    FIELD_LINKEDIN_URL           = "role=textbox[name='LinkedIn Profile URL']"
    BTN_UPLOAD_ICON              = ".lucide.lucide-upload"
    FILE_INPUT                   = "#main"