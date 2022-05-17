from fixtures.constants import OrderNotice, LoginNotice


class TestOrderPage:
    def test_hotel_booking(self, app):
        """
        Бронирование отеля.
        """
        app.order_page.open_login_page()
        app.order_page.login()
        assert app.order_page.success_log_in_text() == LoginNotice.login
        app.order_page.click_button_see_accommodation()
        assert app.order_page.find_button_more() == OrderNotice.BUTTON_MORE
        app.order_page.click_button_more()
        assert app.order_page.find_button_book() == OrderNotice.BUTTON_BOOK
        app.order_page.click_button_book()
        app.order_page.open_basket_page()
        assert OrderNotice.BOOKED in app.order_page.check_book()
