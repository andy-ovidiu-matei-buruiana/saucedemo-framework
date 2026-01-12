import os
from datetime import datetime

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


# -------- pytest html report config ---------

def pytest_html_report_title(report):
    report.title = "SauceDemo Selenium Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project: SauceDemo Automation",
        "Framework: pytest + Selenium",
    ])

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("browser")
    if driver is None:
        return

    if report.failed:
        reports_dir = os.path.join(os.getcwd(), "saucedemo_framework/reports")
        screenshots_dir = os.path.join(reports_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(
            c if c.isalnum() or c in "-_." else "_"
            for c in item.nodeid
        )
        png_path = os.path.join(
            screenshots_dir, f"{safe_name}_{timestamp}.png"
        )

        driver.save_screenshot(png_path)

        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.image(png_path))
        report.extras = extras

# ------- pytest CLI options --------

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--timeout",
        action="store",
        default="10",
        help="Default explicit wait timeout (seconds)",
        type=int
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge", "remote"])

# -------- test fixtures ----------

from flows.login_flow import LoginFlow
from models.login_user import LogInUserInfo
from pages.inventory_page import InventoryPage
from testdata.users import VALID_USERS, PASSWORD

@pytest.fixture
def browser(request: pytest.FixtureRequest):
    browser_name: str = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        # Disable password manager + credential prompts
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        # reduce random Chrome UI interruptions
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-first-run")
        # use guest to remove password leak prompts
        options.add_argument("--guest")

        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.switch_to.window(driver.current_window_handle)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def timeout(request: pytest.FixtureRequest) -> int:
    return request.config.getoption("--timeout")

@pytest.fixture
def inventory_page(browser: WebDriver, timeout: int) -> InventoryPage:
    user = LogInUserInfo(VALID_USERS[0], PASSWORD)
    inventory = LoginFlow.login_successful(browser, timeout, user)
    inventory.is_loaded()
    return inventory