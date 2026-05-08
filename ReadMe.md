# Confluence link

# Selenium locators: https://pythonseleniumpytest.atlassian.net/wiki/spaces/SA/pages/1310721/Selenium+Locators

# Pytest structure plan: https://pythonseleniumpytest.atlassian.net/wiki/spaces/SA/pages/28180499/Pytest

# Selenium Pytest Automation Framework

UI test automation framework built using:
- Python
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Allure reporting

# Project structure

project_root/
│
├── page_objects/ # Page classes (HomePage, LoginPage)
├── components/ # Reusable UI components (Navbar, SearchBar)
├── tests/ # Test cases
├── conftest.py # Fixtures (browser setup)
├── base_page.py # Selenium wrapper methods
├── pytest.ini # Pytest config
└── requirements.txt

## Setup

```bash
git clone <repo_url>
cd <project>

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

# 4. How to Run Tests

```md
# Run Tests

Run all tests:
```bash
pytest --alluredir=Reports

# 5. Markers (you already use them, so document them)

```md
# Markers

- navbar → Navbar related tests
- login → Login functionality
- search → Search feature

## Allure Report

Generate report:
```bash
pytest --alluredir=reports
allure serve reports

### 7. Key Design Decisions (this is where you stand out)

```md
## Framework Design

- Page Object Model (POM) for maintainability
- Components used for reusable UI elements (e.g., Navbar)
- BasePage abstracts Selenium operations
- Tests focus on behavior, not locators

## Limitations

- No CD integration currently