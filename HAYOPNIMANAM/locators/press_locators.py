from playwright.sync_api import Locator, Page


class PressPage:
    """Page Object Model for the Hayop ni Manam Press page."""

    BASE_URL = "https://hayopnimanam.com/"
    PRESS_URL = "https://hayopnimanam.com/press/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self) -> None:
        """Navigate to the press page via the homepage nav link."""
        self.page.goto(self.BASE_URL)
        self.page.add_style_tag(content=(
            "*, *::before, *::after { animation: none !important; "
            "transition: none !important; opacity: 1 !important; "
            "visibility: visible !important; }"
        ))
        self.page.get_by_role("link", name="Go to Page PRESS").click()
        self.page.wait_for_url("**/press/**")

    def goto_pagination_page(self, page_number: int) -> None:
        """Click through pagination buttons to reach the given page number.

        Waits for network activity to settle after each click instead of a
        fixed timeout. Paginated content here is re-rendered async (no full
        page navigation), so a fixed 300ms delay could race a later click
        against an in-progress render when jumping multiple pages ahead
        (e.g. straight to page 3+), causing intermediate clicks to land on
        stale content or get swallowed.
        """
        if page_number == 1:
            return
        for n in range(2, page_number + 1):
            self.page.get_by_role("button", name=str(n)).click()
            try:
                self.page.wait_for_load_state("networkidle", timeout=5000)
            except Exception:
                pass  # some sites never fully idle (analytics/polling) — non-fatal
            self.page.wait_for_timeout(300)  # small buffer for any final paint

    def link(self, name: str) -> Locator:
        """Return a press article link by partial text match against its card content."""
        return self.page.locator("a").filter(has_text=name)

    # --- Featured / header content on page 1 ---------------------------

    @property
    def featured_date(self) -> Locator:
        return self.page.get_by_text("CNA Lifestyle", exact=False)

    @property
    def featured_source(self) -> Locator:
        return self.page.get_by_text("CNA Lifestyle", exact=False)

    @property
    def featured_image(self) -> Locator:
        return self.page.locator("img").first

    @property
    def featured_heading(self) -> Locator:
        return self.page.get_by_role("heading", level=2).first

    @property
    def read_more_link(self) -> Locator:
        return self.page.get_by_role("link", name="read more", exact=True)

    @property
    def press_features_label(self) -> Locator:
        return self.page.get_by_text("press features", exact=False)

    @property
    def pagination_summary(self) -> Locator:
        return self.page.get_by_role("button", name="2")

    # --- Footer ----------------------------------------------------------

    @property
    def footer_instagram(self) -> Locator:
        return self.page.locator("a[href='https://www.instagram.com/hayop.sg']")

    @property
    def footer_privacy(self) -> Locator:
        return self.page.locator("a[href='https://hayopnimanam.com/privacy-policy/']")

    @property
    def footer_terms(self) -> Locator:
        return self.page.locator("a[href='https://hayopnimanam.com/terms-conditions/']")


# Mapping of (link visible name, pagination page it appears on)
# Update these names/pages to match the live site if they change.
PRESS_LINKS = [
    ("read more", 1),
    ("The Moment Group", 1),
    ("Hayop – Overseas Outpost of", 1),
    ("Filipino restaurant Hayop", 1),
    ("hayop, Manam's sister", 1),
    ("Best eats of 2024: Best", 1),
    ("At Hayop, the joys of", 2),
    ("Hayop: Singapore's First Fine", 2),
    ("Hayop is a joyous", 2),
    ("Food Picks: Filipino fare at", 2),
    ("From adobo to zipyu thee", 2),
    ("Review: Hayop, a beast of", 3),
    ("Manam spin-off", 3),
]