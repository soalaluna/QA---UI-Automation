import pytest
from playwright.sync_api import Page, expect
from locators.order_online_locators import OrderOnlineLocators as OL


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def navigate_to_order_online(page: Page):
    page.goto(OL.ORDER_ONLINE_URL, wait_until="domcontentloaded", timeout=60000)
    yield


# ── Header Tests ──────────────────────────────────────────────────────────────

class TestOrderOnlineHeader:

    def test_logo_visible(self, page: Page):
        expect(page.locator(OL.LINK_HAYOP_LOGO)).to_be_visible()

    def test_logo_clickable(self, page: Page):
        page.locator(OL.LINK_HAYOP_LOGO).click()
        expect(page).to_have_url(OL.ORDER_ONLINE_URL)

    def test_delivery_location_button_visible(self, page: Page):
        expect(page.locator(OL.BTN_DELIVERY_LOCATION).nth(1)).to_be_visible()

    def test_cart_button_visible(self, page: Page):
        expect(page.locator(OL.BTN_CART)).to_be_visible()


# ── Menu Section Tests ─────────────────────────────────────────────────────────

class TestMenuSections:

    def test_bakery_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_BAKERY)).to_be_visible()

    def test_starters_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_STARTERS)).to_be_visible()

    def test_mains_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_MAINS)).to_be_visible()

    def test_vegetables_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_VEGETABLES)).to_be_visible()

    def test_rice_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_RICE)).to_be_visible()

    def test_desserts_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_DESSERTS)).to_be_visible()


# ── Menu Item Tests (sample set) ───────────────────────────────────────────────

class TestMenuItems:

    def test_ensaymada_item_visible(self, page: Page):
        expect(page.locator(OL.ITEM_ENSAYMADA)).to_be_visible()

    def test_chicharon_bulaklak_item_visible(self, page: Page):
        expect(page.locator(OL.ITEM_CHICHARON_BULAKLAK)).to_be_visible()

    def test_adobong_pula_item_visible(self, page: Page):
        expect(page.locator(OL.ITEM_ADOBONG_PULA)).to_be_visible()

    def test_buko_pie_item_visible(self, page: Page):
        expect(page.locator(OL.ITEM_BUKO_PIE)).to_be_visible()

    def test_clicking_menu_item_opens_modal_and_closes(self, page: Page):
        """Clicking a menu item should open its detail modal, closable via Close button."""
        page.locator(OL.ITEM_ENSAYMADA).click()
        page.locator(OL.BTN_MODAL_CLOSE).wait_for(state="visible", timeout=10000)
        page.locator(OL.BTN_MODAL_CLOSE).click()


# ── Delivery/Pickup Dialog Tests ──────────────────────────────────────────────

class TestDeliveryPickupDialog:

    @pytest.fixture(autouse=True)
    def open_location_dialog(self, page: Page):
        page.locator(OL.BTN_DELIVERY_LOCATION).nth(1).click()
        OL.tab_pickup(page).wait_for(state="visible", timeout=10000)

    def test_pickup_tab_visible(self, page: Page):
        expect(OL.tab_pickup(page)).to_be_visible()

    def test_delivery_tab_visible(self, page: Page):
        expect(OL.tab_delivery(page)).to_be_visible()

    def test_pickup_outlet_radio_visible(self, page: Page):
        OL.tab_pickup(page).click()
        expect(page.locator(OL.RADIO_OUTLET_HAYOP)).to_be_visible()

    def test_pickup_cancel_confirm_buttons_visible(self, page: Page):
        OL.tab_pickup(page).click()
        expect(page.locator(OL.BTN_DIALOG_CANCEL)).to_be_visible()
        expect(page.locator(OL.BTN_DIALOG_CONFIRM)).to_be_visible()

    def test_delivery_address_field_visible(self, page: Page):
        # Delivery is the default tab on dialog open — no tab switch needed.
        expect(page.locator(OL.FIELD_DELIVERY_ADDRESS)).to_be_visible()

    def test_delivery_address_field_fillable(self, page: Page):
        page.locator(OL.FIELD_DELIVERY_ADDRESS).fill("Singapore")
        expect(page.locator(OL.FIELD_DELIVERY_ADDRESS)).to_have_value("Singapore")

    def test_delivery_address_field_submits_on_enter(self, page: Page):
        field = page.locator(OL.FIELD_DELIVERY_ADDRESS)
        field.fill("Singapore")
        field.press("Enter")
        # TODO: assert on the actual post-submit state (autocomplete list,
        # enabled confirm button, navigation, etc.) once confirmed.


# ── Cart Tests ─────────────────────────────────────────────────────────────────

class TestCart:

    def test_cart_opens_with_empty_state(self, page: Page):
        page.locator(OL.BTN_CART).click()
        expect(page.locator(OL.HEADING_YOUR_CART)).to_be_visible()
        expect(page.get_by_text("Your cart is empty.")).to_be_visible()


# ── Account Menu Tests ─────────────────────────────────────────────────────────
# TODO: BTN_ACCOUNT_MENU is unresolved. get_by_role("img").nth(1) now opens
# the cart dialog instead of the account menu. Replace the click target below
# once the real locator is found via Inspect Element / codegen "Pick locator".

class TestAccountMenu:

    def test_signup_menuitem_visible(self, page: Page):
        page.locator(OL.BTN_ACCOUNT_MENU).click()
        expect(page.locator(OL.MENU_ITEM_SIGNUP)).to_be_visible()

    def test_login_menuitem_visible(self, page: Page):
        page.locator(OL.BTN_ACCOUNT_MENU).click()
        expect(page.locator(OL.MENU_ITEM_LOGIN)).to_be_visible()


# ── Footer Tests ──────────────────────────────────────────────────────────────

class TestOrderOnlineFooter:

    def test_find_us_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_FIND_US)).to_be_visible()

    def test_address_link_opens_popup(self, page: Page):
        """Address link should open Google Maps in a new tab."""
        with page.expect_popup() as popup_info:
            page.locator(OL.LINK_ADDRESS).click()
        popup = popup_info.value
        assert popup.url != ""
        popup.close()

    def test_operating_hours_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_OPERATING_HOURS)).to_be_visible()

    def test_social_heading_visible(self, page: Page):
        expect(page.locator(OL.HEADING_SOCIAL)).to_be_visible()

    def test_make_reservation_link_visible(self, page: Page):
        expect(page.locator(OL.LINK_MAKE_RESERVATION)).to_be_visible()

    def test_atlas_website_link_visible(self, page: Page):
        expect(page.locator(OL.LINK_ATLAS_WEBSITE)).to_be_visible()

    def test_scroll_to_top_button_visible(self, page: Page):
        expect(page.locator(OL.SCROLLER_TOP_BTN)).to_contain_text("TOP")