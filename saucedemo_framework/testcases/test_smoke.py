from pages.login_page import LoginPage

def test_smoke(browser):
    # create Login Page object
    login = LoginPage(browser, 10)
    # open page
    login.open()

    assert "Swag Labs" in browser.title