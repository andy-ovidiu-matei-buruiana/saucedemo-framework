# SauceDemo Automation Framework

End-to-end UI automation framework for [saucedemo.com](https://www.saucedemo.com) built with **Python, pytest, Selenium WebDriver**, following **Page Object Model (POM)** and clean test architecture principles.

This project is designed as a **learning opportunity but made in production style** framework, emphasizing:
- maintainability
- clear separation of concerns
- explicit waits & stability
- extensibility (browsers, flows, reports)

---

## Tech Stack

- **Python** 3.10+
- **pytest** – test runner
- **Selenium WebDriver** – browser automation
- **pytest-html** – HTML reports
- **mypy** – static typing
- **Chrome / Firefox / Edge** – supported browsers

---

## Project Structure

```
SAUCEDEMO
│   .gitignore
│   mypy.ini
│   pytest.ini
│   README.md
│   requirements.txt
│
└───saucedemo_framework
    │   conftest.py
    │
    ├───components
    │       __init__.py
    │       header.py
    │
    ├───flows
    │       __init__.py
    │       checkout_flow.py
    │       login_flow.py
    │
    ├───models
    │       __init__.py
    │       checkout_user.py
    │       login_user.py
    │
    ├───pages
    │       __init__.py
    │       base_page.py
    │       cart_page.py
    │       checkout_step_one_page.py
    │       checkout_step_two_page.py
    │       complete_page.py
    │       inventory_page.py
    │       login_page.py
    │
    ├───reports
    │   │   report.html
    │   │
    │   ├───assets
    │   │       style.css
    │   │
    │   └───screenshots
    │           *.png
    │
    ├───testcases
    │       __init__.py
    │       test_add_to_cart.py
    │       test_checkout.py
    │       test_checkout_wrong_information.py
    │       test_login.py
    │       test_login_exists.py
    │       test_remove_from_cart.py
    │       test_smoke.py
    │       test_sort.py
    │
    ├───testdata
            __init__.py
            items.py
            sort.py
            users.py
            user_information.py

```

---

## Design Principles

### Page Object Model (POM)
- Each page encapsulates:
  - locators
  - actions
  - page-level assertions
- No Selenium logic inside tests

### BasePage Abstraction
- Centralized:
  - explicit waits
  - click / type helpers
  - retry logic for flaky UI actions

### Flows
- High-level business actions (e.g. login)
- Keep tests short and readable
- Hide technical Selenium details

### Components
- Shared UI sections (e.g. header)
- Reused across multiple pages

---

## Test Types Covered

- Smoke tests
- Login (valid & invalid users)
- Add / remove from cart
- Sorting (price & name)
- Checkout (valid & invalid data)
- UI presence & navigation checks

---

## Running Tests

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest
```

### Run a specific test
```bash
pytest -k test_add_to_cart
```

### Run with browser selection
```bash
pytest --browser=firefox
```

Supported browsers:
- `chrome` (default)
- `firefox`
- `edge`

---

## Custom Timeout

Default explicit wait timeout is **10 seconds**.

Override via CLI:
```bash
pytest --timeout=20
```

---

## HTML Reports

HTML reports are automatically generated after each run.

Location:
```
reports/report_<timestamp>.html
```

### Features:
- Test summary
- Failure details
- Screenshots on failure
- Execution time

Open the report directly in a browser.

---

## Screenshots on Failure

- Automatically captured on test failure
- Stored in:
```
reports/screenshots/
```
- Linked inside the HTML report

---

## Static Typing

The framework supports **mypy** for static analysis:
- Page Objects are strictly typed
- Tests remain flexible
- Helps catch:
  - incorrect return types
  - invalid method usage
  - broken refactors

Run:
```bash
mypy saucedemo_framework/pages
```

---

## Future Improvements

Planned extensions:
- Parallel execution (pytest-xdist)
- CI integration (GitHub Actions)
- Dockerized Selenium
- API + UI hybrid tests
- Visual regression testing

---

## Author

Built as a **learning automation project** to practice:
- pytest best practices
- Selenium stability patterns
- test architecture design
- professional automation workflows

