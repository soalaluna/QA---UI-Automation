"""
Locators for The Group page - momentgroup.ph/the-group
Only contains clickable/interactive elements.
"""


class TheGroupLocators:
    BASE_URL  = "https://momentgroup.ph/"
    GROUP_URL = "https://momentgroup.ph/the-group/"  # no hash — actual landing URL

    # --- Navigation ---
    NAV_THE_GROUP = "link[name='The Group']"

    # --- Section Headings ---
    HEADING_THE_GROUP    = "#thegroup_frame1 >> role=heading[name='The Group']"
    HEADING_ABOUT        = "role=heading[name='About']"
    HEADING_PARTNERSHIPS = "#breadcrumbs-3 >> role=heading[name='Partnerships']"
    HEADING_MILESTONES   = "#breadcrumbs-4 >> role=heading[name='Milestones']"

    # --- Breadcrumb Tabs ---
    BREADCRUMB_1 = "#breadcrumbs-1"
    BREADCRUMB_3 = "#breadcrumbs-3"
    BREADCRUMB_4 = "#breadcrumbs-4"

    # --- Founders Section ---
    # Two "The Founders" headings exist (white + black versions) — use exact=True to target the visible one
    HEADING_FOUNDERS = "h5.frame-title.color-black:has-text('The Founders')"
    FOUNDER_ABBA     = "role=heading[name='Abba Napa']"
    FOUNDER_ELIZA    = "role=heading[name='Eliza Antonino']"
    FOUNDER_JON      = "role=heading[name='Jon Syjuco']"