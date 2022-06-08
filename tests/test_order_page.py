import allure
from fixtures.constants import LoginNotice


class TestOrderPage:
    @allure.feature("order page")
    @allure.story("Hotel booking.")
    def test_hotel_booking(self, app):
        """
        Hotel booking.
        """
        app.order_page.open_login_page()
        app.order_page.login()
        assert app.order_page.success_log_in_text() == LoginNotice.login
        app.order_page.click_button_see_accommodation()
        assert app.order_page.find_button_more() == LoginNotice.BUTTON_MORE
        app.order_page.click_button_more()
        assert app.order_page.find_button_book() == LoginNotice.BUTTON_BOOK
        app.order_page.click_button_book()
        app.order_page.open_basket_page()
        assert LoginNotice.BOOKED in app.order_page.check_book()
