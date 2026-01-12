from pages.login_page import LoginPage


def test_login_exists(browser, timeout):
    # create Login Page object
    login = LoginPage(browser, timeout)
    # open page
    login.open()

    login.is_loaded()
