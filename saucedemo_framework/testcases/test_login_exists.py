from pages.login_page import LoginPage


def test_login_exists(browser):
    # create Login Page object
    login = LoginPage(browser, 10)
    # open page
    login.open()

    login.is_loaded()
