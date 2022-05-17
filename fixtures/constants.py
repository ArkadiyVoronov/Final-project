"""Константы, в т.ч. тексты ошибок и уведомлений."""


class RegNotice:
    LOG_IN = "Log in"
    ERROR_PASSWORD = "The two password fields didn’t match."
    ERROR_AGE = "You are young!"
    ERROR_PASSWORD_NUMERIC = "This password is entirely numeric."
    ERROR_PASSWORD_COMMON = "This password is too common."
    ERROR_RE_REG = "A user with that username already exists."


class LoginNotice:
    login = "qwerty"
    password = "L38H84G4f53"
    email = "qwerty345@gmail.com"
    ERROR_LOGIN = "Please enter a correct username and password. Note that both fields may be case-sensitive."
    INDEX_TEXT = "Rest, which you deserve"


class OrderNotice:
    INDEX_TEXT = "Rest, which you deserve"
    BUTTON_MORE = "More"
    BUTTON_BOOK = "Book"
    BOOKED = "Booked"
