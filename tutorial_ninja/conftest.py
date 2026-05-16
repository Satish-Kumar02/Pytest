"""
Pytest fixtures for email testing
"""
import pytest
import sys
import os
import requests

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Utility.email_helper import EmailHelper
from Configurations.email_config import EmailConfig, EmailTemplates, RECEIVER_EMAIL


def is_mailhog_available():
    """Check if MailHog is available"""
    try:
        response = requests.get(f"http://{EmailConfig.SMTP_HOST}:8025/api/v1/messages", timeout=2)
        return response.status_code == 200
    except:
        return False


# Mark email tests to skip if MailHog is not available
mailhog_available = is_mailhog_available()


def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "email: mark test as email test (requires MailHog)"
    )


@pytest.fixture
def email_helper():
    """Fixture to provide EmailHelper instance"""
    helper = EmailHelper(
        smtp_host=EmailConfig.SMTP_HOST,
        smtp_port=EmailConfig.SMTP_PORT,
        mailhog_api_url=EmailConfig.API_URL
    )
    yield helper
    # Cleanup: Clear all emails after test
    if EmailConfig.ENV in ['docker', 'local']:
        helper.clear_all_emails()


@pytest.fixture
def receiver_email():
    """Fixture to provide the test receiver email"""
    return RECEIVER_EMAIL


@pytest.fixture
def sender_email():
    """Fixture to provide the sender email"""
    return EmailConfig.FROM_EMAIL


@pytest.fixture
def email_templates():
    """Fixture to provide email templates"""
    return EmailTemplates


@pytest.fixture
def setup_email_environment(email_helper):
    """Setup email environment (clear emails before test)"""
    if EmailConfig.ENV in ['docker', 'local']:
        email_helper.clear_all_emails()
    yield
    if EmailConfig.ENV in ['docker', 'local']:
        email_helper.clear_all_emails()


# Autouse fixture to clear emails before each test
@pytest.fixture(autouse=True)
def auto_cleanup_emails(email_helper):
    """Automatically clear emails before and after each test"""
    if EmailConfig.ENV in ['docker', 'local']:
        email_helper.clear_all_emails()
    yield
    if EmailConfig.ENV in ['docker', 'local']:
        email_helper.clear_all_emails()
