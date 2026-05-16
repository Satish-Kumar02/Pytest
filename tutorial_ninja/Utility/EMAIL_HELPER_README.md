# Email Testing with MailHog

This guide explains how to use the `EmailHelper` class for testing email functionality in your Pytest automation tests.

## Prerequisites

Ensure your `docker-compose.yml` includes MailHog service:

```yaml
mailhog:
    image: mailhog/mailhog:latest
    ports:
      - "1025:1025"    # SMTP port
      - "8025:8025"    # Web UI port
```

## Installation

The `EmailHelper` class is located in:
```
tutorial_ninja/Utility/email_helper.py
```

## Usage

### Basic Setup

```python
from Utility.email_helper import EmailHelper

# Initialize EmailHelper (for Docker usage)
email_helper = EmailHelper()

# Or with custom configuration
email_helper = EmailHelper(
    smtp_host="localhost",      # For local testing
    smtp_port=1025,
    mailhog_api_url="http://localhost:8025/api/v1/messages"
)
```

### Send an Email

```python
email_helper.send_email(
    sender="noreply@example.com",
    receiver="user@example.com",
    subject="Welcome",
    body="Hello User!"
)
```

### Send HTML Email

```python
html_body = """
<html>
  <body>
    <h1>Welcome!</h1>
    <p>Thank you for registering.</p>
    <a href="https://example.com/confirm">Confirm Email</a>
  </body>
</html>
"""

email_helper.send_email(
    sender="noreply@example.com",
    receiver="user@example.com",
    subject="Confirm Your Email",
    body=html_body,
    html=True
)
```

### Verify Email Received

```python
# Simple verification
if email_helper.verify_email_received("user@example.com"):
    print("Email received!")

# With subject verification
if email_helper.verify_email_received("user@example.com", "Welcome"):
    print("Welcome email received!")
```

### Find Emails

```python
# Find by receiver
email = email_helper.find_email_by_receiver("user@example.com")

# Find by subject
email = email_helper.find_email_by_subject("Password Reset")

# Get latest email
latest = email_helper.get_latest_email()

# Get all emails
all_emails = email_helper.get_all_emails()
```

### Clear Emails

```python
# Clear all emails from MailHog
email_helper.clear_all_emails()
```

## Complete Test Example

```python
import pytest
from Utility.email_helper import EmailHelper

class TestUserRegistration:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.email_helper = EmailHelper()
        self.email_helper.clear_all_emails()
        yield
        self.email_helper.clear_all_emails()
    
    def test_registration_sends_confirmation_email(self, driver):
        # 1. Register user
        # ... your Selenium code ...
        new_user_email = "testuser@example.com"
        
        # 2. Simulate email being sent (or it happens in app)
        self.email_helper.send_email(
            sender="noreply@tutorialsninja.com",
            receiver=new_user_email,
            subject="Confirm Your Email",
            body="Click here to confirm"
        )
        
        # 3. Verify email was sent
        assert self.email_helper.verify_email_received(new_user_email)
        
        # 4. Extract email content if needed
        email = self.email_helper.find_email_by_receiver(new_user_email)
        assert "Confirm" in email['Content']['Headers']['Subject'][0]
```

## MailHog Web UI

Access the MailHog Web UI at: **http://localhost:8025**

Here you can:
- View all captured emails
- See email headers and body
- Search emails
- Release emails to real mailbox (optional)

## Viewing Emails in Docker

When running tests in Docker:

```bash
docker-compose up
```

MailHog Web UI: **http://localhost:8025**

## Methods Reference

### `send_email(sender, receiver, subject, body, html=False)`
Send an email via SMTP

### `verify_email_received(receiver, subject=None)`
Check if email was received (optionally with specific subject)

### `find_email_by_receiver(receiver)`
Find email by recipient address

### `find_email_by_subject(subject)`
Find email by subject line

### `get_latest_email()`
Get the most recent email

### `get_all_emails()`
Get list of all emails

### `clear_all_emails()`
Delete all emails from MailHog

## Troubleshooting

**Issue: Cannot connect to MailHog**
- Ensure Docker is running
- Check `docker-compose.yml` has MailHog service
- Verify SMTP host is correct ("mailhog" in Docker, "localhost" locally)

**Issue: Emails not appearing**
- Verify no exceptions in `send_email()` call
- Check MailHog Web UI is accessible
- Ensure `clear_all_emails()` is called in setup

**Issue: HTML content not showing**
- Make sure to set `html=True` when sending HTML emails
- Use proper HTML tags

## Real-World Scenario

```python
def test_password_reset_flow(self):
    # Step 1: Request password reset
    # (Selenium code to fill form and submit)
    
    # Step 2: Verify reset email sent
    email = self.email_helper.find_email_by_subject("Password Reset")
    assert email is not None
    
    # Step 3: Extract reset link from email body
    body = email['Content']['Body']
    import re
    reset_link = re.search(r'(https://[^\s]+)', body).group(1)
    
    # Step 4: Navigate to reset link
    driver.get(reset_link)
    
    # Step 5: Complete password reset
    # (Selenium code to enter new password)
```

## Notes

- Emails are temporary in MailHog (reset on container restart)
- MailHog does NOT deliver emails to real addresses
- Perfect for development and testing environments
- See `test_email_functionality.py` for comprehensive examples
