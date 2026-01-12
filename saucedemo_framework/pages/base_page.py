from typing import Tuple, TypeVar, Callable, Optional, List, cast
import sys
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = Tuple[str, str]
# any type
T = TypeVar("T")

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.timeout = timeout
        self._select_all_key = (
            Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        )

    def _retry(self, action: Callable[[], T], retries: int = 2) -> T:
        last: Optional[Exception] = None
        for _ in range(retries + 1):
            try:
                return action()
            except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                last = e
        raise last # type: ignore

    # ---------- waits / finds ----------
    def _find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def _find_all(self, locator: Locator) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def _wait_visible(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _is_visible(self, locator: Locator, timeout: int = 1) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def _wait_invisible(self, locator: Locator) -> bool:
        result = self.wait.until(EC.invisibility_of_element_located(locator))
        # assure mypy that result is bool
        return cast(bool, result)

    def _wait_clickable(self, locator: Locator) -> WebElement:
        return  self.wait.until(EC.element_to_be_clickable(locator))

    def _wait_text_present(self, locator: Locator, text: str) -> bool:
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def _wait_url_contains(self, partial_url: str) -> bool:
        return self.wait.until(EC.url_contains(partial_url))

    # ---------- actions ----------
    def _click(self, locator: Locator) -> None:
        def _do() -> None:
            self._wait_clickable(locator).click()

        try:
            self._retry(_do, retries=2)
        except ElementClickInterceptedException:
            # last resort: JS click
            el = self._find(locator)
            self.driver.execute_script("arguments[0].click();", el)

    def _type(self, locator: Locator, value: str, verify: bool = True) -> None:
        value = "" if value is None else str(value)

        def _do() -> None:
            el = self._wait_visible(locator)
            el.click()

            # cross-platform clear
            el.send_keys(self._select_all_key, "a")
            el.send_keys(Keys.BACKSPACE)

            el.send_keys(value)

            if verify:
                self.wait.until(lambda d: self._wait_visible(locator).get_attribute("value") == value)

        self._retry(_do, retries=2)

    # ---------- shortcut methods ----------
    def _text(self, locator: Locator) -> str:
        return self._wait_visible(locator).text.strip()