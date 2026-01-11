from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.timeout = timeout

    def _find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

    def _find_all(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                locator
            )
        )

    def _wait_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

    def _wait_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(
                locator
            )
        )

    def _wait_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

    def _click(self, locator):
        self._wait_clickable(locator).click()

    def _wait_text_present(self, locator, text):
        return self.wait.until(
            EC.text_to_be_present_in_element(
                locator,
                text
            )
        )

    def _wait_url_contains(self, partial_url):
        return self.wait.until(
            EC.url_contains(
                partial_url
            )
        )

    def _type(self, locator, value):
        # wait until element is visible
        el = self._wait_visible(locator)

        # wait until element is enabled
        self.wait.until(
            lambda d: el.is_enabled()
        )
        # focus element
        el.click()
        el.clear()
        el.send_keys(value)

        # wait until value is actually set
        self.wait.until(
            lambda d: el.get_attribute("value") == value
        )
