class ReservationLocators:

    # --- URLs ---
    RESERVATION_URL = "https://hayopnimanam.com/reservation/"

    # --- CTA ---
    LINK_MAKE_RESERVATION = "a[href='https://www.sevenrooms.com/reservations/hayop']"  # opens popup (SevenRooms)

    # --- Operating Hours ---
    TEXT_LUNCH_LABEL  = "text=Lunch"
    TEXT_LUNCH_HOURS  = "text=Tuesdays – Saturdays | 11:"
    TEXT_DINNER_LABEL = "text=Dinner"
    TEXT_DINNER_HOURS = "text=5:00pm"  # unique substring avoids en-dash character mismatch

    # --- Address ---
    TEXT_ADDRESS = "main >> text=104 Amoy Street, Singapore"

    # --- Content Card ---
    CARD_RESERVATION_INFO = "div:has-text('make a reservation Lunch')"