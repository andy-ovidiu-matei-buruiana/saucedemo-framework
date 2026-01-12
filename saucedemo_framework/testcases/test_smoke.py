from pages.login_page import LoginPage

def test_smoke(browser, timeout):
    # create Login Page object
    login = LoginPage(browser, timeout)
    # open page
    login.open()

    assert "Swag Labs" in browser.title