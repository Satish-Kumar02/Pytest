# TutorialsNinja Demo - Selenium Pytest Automation Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-9.0.3-green.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.21.0-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

A comprehensive, production-ready **UI test automation framework** for the [TutorialsNinja Demo](https://tutorialsninja.com/demo/) e-commerce website. Built with Python, Pytest, Selenium WebDriver, and Allure reporting.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Viewing Reports](#viewing-reports)
- [Project Architecture](#project-architecture)
- [Test Markers](#test-markers)
- [Docker Support](#docker-support)
- [Contributing](#contributing)
- [References](#references)

---

## 🎯 Overview

This is a **Page Object Model (POM) based automation framework** designed to test the TutorialsNinja e-commerce demo application. The framework emphasizes:

- **Maintainability**: Clean code structure with reusable components
- **Scalability**: Easy to add new tests and pages
- **Reliability**: Robust wait strategies and error handling
- **Reporting**: Detailed Allure reports with screenshots
- **Portability**: Docker support for CI/CD pipelines

**Website Under Test**: [https://tutorialsninja.com/demo/](https://tutorialsninja.com/demo/)

---

## ✨ Features

- ✅ **Page Object Model (POM)** - Organized page classes for maintainability
- ✅ **Reusable Components** - Shared UI components (Navbar, SearchBar, ProductPage, CurrencyDropdown)
- ✅ **Base Page Utilities** - Common Selenium methods (click, type, wait, scroll)
- ✅ **Allure Reporting** - Beautiful, detailed test reports with screenshots and logs
- ✅ **Screenshot Capture** - Automatic screenshots on test failures
- ✅ **Test Markers** - Organize tests with pytest markers (e.g., @pytest.mark.product)
- ✅ **Configuration Management** - Externalized configuration using config.ini
- ✅ **WebDriver Manager** - Automatic browser driver management
- ✅ **Pytest HTML Reports** - Alternative HTML test reports
- ✅ **Docker Support** - Containerized testing environment
- ✅ **Cross-Browser Support** - Configured for Chrome (easily extensible)

---

## 🛠 Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Programming language |
| **Pytest** | 9.0.3 | Test framework |
| **Selenium WebDriver** | 4.21.0 | Browser automation |
| **Allure Pytest** | 2.15.3 | Test reporting |
| **WebDriver Manager** | 4.0.2 | Browser driver management |
| **Pytest HTML** | 4.1.1 | HTML reports |
| **Docker** | Latest | Containerization |

---

## 📁 Project Structure

```
tutorial_ninja/
│
├── page_objects/               # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py            # Base class with common Selenium methods
│   ├── home_page.py            # Home page object
│   ├── log_in.py               # Login page object
│   └── search_results.py        # Search results page object
│
├── components/                 # Reusable UI components
│   ├── __init__.py
│   ├── navbar.py               # Navigation bar component
│   ├── search_bar.py           # Search bar component
│   ├── product_page.py         # Product page component
│   └── currency_dropdown.py     # Currency dropdown component
│
├── tests/                      # Test cases
│   ├── __init__.py
│   └── test_*.py               # Test files (organized by feature)
│
├── Configurations/             # Configuration files
│   └── config.ini              # App URL, browser, etc.
│
├── Reports/                    # Test execution reports
│   └── allure-results/         # Allure report data
│
├── allure-report/              # Generated Allure HTML report
│   ├── index.html
│   ├── app.js
│   ├── styles.css
│   └── data/
│
├── screenshots/                # Failure screenshots
│   └── [screenshot_files].png
│
├── Utility/                    # Helper utilities
│   └── [utility modules]
│
├── file/                       # Test data files
│   └── test.txt
│
├── conftest.py                 # Pytest configuration & fixtures
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── .dockerignore               # Docker ignore file
└── __init__.py

```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/)
- **Chrome Browser** - [Download](https://www.google.com/chrome/)
- **pip** - Comes with Python
- **Docker** (optional) - [Download](https://www.docker.com/)

Verify installations:
```bash
python --version      # Should show Python 3.8+
pip --version         # Should show pip version
git --version         # Should show git version
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Satish-Kumar02/Pytest.git
cd Pytest
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:
```bash
pip list
```

### 4. Verify WebDriver Manager

The framework uses `webdriver-manager` to automatically download the correct ChromeDriver. No manual setup needed!

---

## ⚙️ Configuration

### Application Configuration (`tutorial_ninja/Configurations/config.ini`)

```ini
[app]
url = https://tutorialsninja.com/demo/    # Base URL of the application
browser = chrome                           # Browser type (chrome, firefox, edge)
```

**Customize for different environments:**

```ini
# Development
url = https://tutorialsninja-dev.com/demo/

# Production
url = https://tutorialsninja.com/demo/
```

### Pytest Configuration (`tutorial_ninja/pytest.ini`)

```ini
[pytest]
pythonpath = .                    # Python path for imports
testpaths = tests                 # Directory containing tests
addopts = -ra -q                  # Show all summary info, quiet mode
markers =
    product: marks tests as product tests
```

---

## 🧪 Running Tests

### Run All Tests

```bash
pytest --alluredir=Reports
```

### Run Specific Test File

```bash
pytest tutorial_ninja/tests/test_login.py --alluredir=Reports
```

### Run Tests with Specific Marker

```bash
pytest -m product --alluredir=Reports
```

### Run Tests Excluding Specific Marker

```bash
pytest -m "not product" --alluredir=Reports
```

### Run with Verbose Output

```bash
pytest -v --alluredir=Reports
```

### Run with Detailed Logging

```bash
pytest -v -s --alluredir=Reports
```

### Run with HTML Report

```bash
pytest --html=Reports/report.html --self-contained-html --alluredir=Reports
```

### Run Tests in Parallel (requires pytest-xdist)

```bash
pytest -n auto --alluredir=Reports
```

### Run Tests with Custom Timeout

```bash
pytest --timeout=300 --alluredir=Reports
```

### Run Tests and Stop on First Failure

```bash
pytest -x --alluredir=Reports
```

---

## 📊 Viewing Reports

### Allure Report

Generate and view Allure report:

```bash
# Generate report
pytest --alluredir=Reports

# View report (requires Allure command line)
allure serve Reports
```

The report will open in your default browser showing:
- Test execution summary
- Test details and logs
- Screenshots on failure
- Timeline and history
- Trends and statistics

**Install Allure (if not installed):**

**Windows (using Scoop):**
```bash
scoop install allure
```

**macOS (using Homebrew):**
```bash
brew install allure
```

**Linux/All OS (using npm):**
```bash
npm install -g allure-commandline
```

### HTML Report

```bash
pytest --html=Reports/report.html --self-contained-html
```

Open `Reports/report.html` in your browser.

### Screenshots

Failed test screenshots are automatically saved to `tutorial_ninja/screenshots/`

---

## 🏗 Project Architecture

### Page Object Model (POM)

The framework follows the **Page Object Model** design pattern:

```python
# page_objects/home_page.py
from selenium.webdriver.common.by import By
from page_objects.base_page import basepage

class HomePage(basepage):
    SEARCH_BOX = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-default")
    
    def search_product(self, product_name):
        self.type(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
```

### Base Page

The `base_page.py` provides common Selenium operations:

```python
class basepage:
    def click(self, locator):           # Click element
    def type(self, locator, text):      # Type text
    def find_element(self, by, locator) # Find single element
    def find_elements(self, by, locator) # Find multiple elements
```

### Components

Reusable UI components are modularized:

```python
# components/navbar.py
class NavBar(basepage):
    PROFILE_ICON = (By.ID, "profile")
    
    def click_profile(self):
        self.click(self.PROFILE_ICON)
```

### Test Structure

```python
# tests/test_login.py
import pytest
from page_objects.log_in import LoginPage

class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("user@example.com", "password")
        # Assert
```

---

## 🏷 Test Markers

Organize tests using pytest markers:

### Available Markers

```ini
@pytest.mark.product    # Product-related tests
@pytest.mark.login      # Login tests
@pytest.mark.search     # Search functionality tests
@pytest.mark.checkout   # Checkout tests
@pytest.mark.slow       # Tests that take longer to run
```

### Usage Examples

```python
@pytest.mark.product
def test_product_search():
    # Test code
    pass

@pytest.mark.login
def test_user_login():
    # Test code
    pass
```

### Running by Marker

```bash
# Run only product tests
pytest -m product

# Run only login tests
pytest -m login

# Run all except slow tests
pytest -m "not slow"

# Run product OR login tests
pytest -m "product or login"
```

---

## 🐳 Docker Support

### Build Docker Image

```bash
docker build -t pytest-automation .
```

### Run Tests in Docker

```bash
docker run --rm pytest-automation pytest --alluredir=Reports
```

### Run Tests with Custom Parameters

```bash
docker run --rm pytest-automation pytest -v -m product --alluredir=Reports
```

### Docker Compose (if available)

```bash
docker-compose up
```

### Dockerfile Overview

The `Dockerfile` includes:
- Python 3.10 base image
- All dependencies installed
- Chrome browser and ChromeDriver
- Working directory configured
- Tests ready to run

---

## 🔧 Troubleshooting

### Issue: ChromeDriver Not Found

**Solution:**
```bash
pip install --upgrade webdriver-manager
```

### Issue: Tests Timeout

**Solution:** Increase timeout in `page_objects/base_page.py`:
```python
def __init__(self, driver, timeout=30):  # Increase from 20 to 30
    self.wait = WebDriverWait(driver, timeout)
```

### Issue: Element Not Found

**Solution:** Ensure correct locators in page objects and check website structure:
```python
# Verify locator with browser DevTools
# Right-click → Inspect → Find the element
```

### Issue: Screenshot Directory Not Found

**Solution:** Create screenshots directory:
```bash
mkdir -p tutorial_ninja/screenshots
```

### Issue: Module Import Errors

**Solution:**
```bash
# Ensure pythonpath is set correctly in pytest.ini
# Or add to conftest.py:
import sys
sys.path.insert(0, os.path.abspath('.'))
```

---

## 📝 Best Practices

1. **Keep Page Objects Simple** - One page per file
2. **Use Descriptive Locators** - Name locators clearly
3. **Wait for Elements** - Use WebDriverWait instead of sleep()
4. **Organize Tests** - Group related tests in classes
5. **Use Fixtures** - Leverage conftest.py for setup/teardown
6. **Take Screenshots** - Capture on failures for debugging
7. **Use Markers** - Categorize tests for targeted execution
8. **Document Tests** - Add docstrings to test methods
9. **Clean Logs** - Check logs for debugging information
10. **Version Control** - Commit reports and screenshots to .gitignore

---

## 🔗 References

### Documentation
- [Selenium Python Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

### Useful Links
- **Application**: [TutorialsNinja Demo](https://tutorialsninja.com/demo/)
- **Selenium Locators Guide**: [Internal Wiki](https://pythonseleniumpytest.atlassian.net/wiki/spaces/SA/pages/1310721/Selenium+Locators)
- **Pytest Structure Plan**: [Internal Wiki](https://pythonseleniumpytest.atlassian.net/wiki/spaces/SA/pages/28180499/Pytest)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👤 Author

**Satish Kumar**

- GitHub: [@Satish-Kumar02](https://github.com/Satish-Kumar02)
- Email: satish.kumar@example.com

---

## ❓ FAQ

**Q: How do I add a new test?**
A: Create a new file in `tests/` directory following the naming convention `test_*.py` and use page objects.

**Q: Can I run tests in parallel?**
A: Yes, install `pytest-xdist` and run: `pytest -n auto`

**Q: How do I extend for other browsers?**
A: Update `config.ini` and modify the browser initialization in `conftest.py`.

**Q: Where are test data files stored?**
A: Use the `file/` directory for test data and read them in your tests.

**Q: How do I skip a test?**
A: Use `@pytest.mark.skip` or `@pytest.mark.skipif(condition)`

---

## 📞 Support

For issues, questions, or suggestions:
1. Open an **Issue** on GitHub
2. Check existing **Issues** for solutions
3. Review the **Documentation** and **References**
4. Check the **Troubleshooting** section above

---

**Last Updated**: May 2026
**Status**: ✅ Active Development
**Python**: 3.8+
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
- No Docker for env stabilisation and Kubernetes for orchestration yet
- No CD integration currently