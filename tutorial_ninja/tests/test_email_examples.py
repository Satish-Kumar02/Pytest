"""
Quick reference guide for using email testing in your tests
This file shows how to use the email helper in your existing test files
"""

# ============================================================================
# SIMPLE USAGE - Copy/Paste These Examples into Your Test Files
# ============================================================================

import pytest

# Add this marker to skip tests if MailHog is not running
pytestmark = pytest.mark.email

# Example 1: Basic Email Test
def test_send_simple_email(email_helper, receiver_email):
    """Send and verify a simple email"""
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject="Test Email",
        body="This is a test email"
    )
    
    # Verify email was received
    assert email_helper.verify_email_received(receiver_email)


# Example 2: HTML Email with Template
def test_send_html_email(email_helper, receiver_email, email_templates):
    """Send HTML email using templates"""
    template = email_templates.registration_confirmation("token123")
    
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject=template['subject'],
        body=template['html'],
        html=True
    )
    
    # Verify
    assert email_helper.verify_email_received(receiver_email, "Confirm Your Email")


# Example 3: Find and Extract Email Content
def test_extract_email_content(email_helper, receiver_email):
    """Send email and extract content"""
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject="Action Required",
        body="Please click: https://example.com/verify?token=abc123"
    )
    
    # Find the email
    email = email_helper.find_email_by_receiver(receiver_email)
    
    # Extract details
    body = email['Content']['Body']
    subject = email['Content']['Headers']['Subject'][0]
    
    # Verify content
    assert "token=abc123" in body
    assert "Action Required" in subject


# Example 4: Test Email in Registration Flow
def test_registration_sends_email(driver, email_helper, receiver_email):
    """Test that registration flow sends confirmation email"""
    # Your Selenium registration code here
    # ... fill form, click register ...
    
    # Send the confirmation email
    from Configurations.email_config import EmailTemplates, SENDER_EMAIL
    
    token = "reg_token_xyz"
    template = EmailTemplates.registration_confirmation(token)
    
    email_helper.send_email(
        sender=SENDER_EMAIL,
        receiver=receiver_email,
        subject=template['subject'],
        body=template['html'],
        html=True
    )
    
    # Verify email
    assert email_helper.verify_email_received(receiver_email)
    
    # Extract confirmation link
    email = email_helper.find_email_by_receiver(receiver_email)
    assert token in email['Content']['Body']


# ============================================================================
# USING IN EXISTING TEST FILES
# ============================================================================

"""
To use email testing in your existing test files (like test_login.py, test_search.py):

1. Add these imports at the top:
   from Configurations.email_config import EmailConfig, RECEIVER_EMAIL, SENDER_EMAIL
   from Utility.email_helper import EmailHelper

2. Add email_helper and receiver_email fixtures to your test function:
   def test_my_feature(driver, email_helper, receiver_email):
       # Your test code
       pass

3. Use them in the test:
   email_helper.send_email(
       sender=SENDER_EMAIL,
       receiver=receiver_email,
       subject="Test",
       body="Body"
   )

The fixtures are automatically available because they're defined in conftest.py
"""


# ============================================================================
# RECEIVER EMAIL INFORMATION
# ============================================================================

"""
Receiver Email: sathiskumark192@gmail.com
Sender Email: noreply@tutorialsninja.com

All emails sent in tests go to MailHog (Docker environment)
Emails are captured and visible at: http://localhost:8025

In Docker:
- SMTP Host: mailhog
- SMTP Port: 1025

Locally:
- SMTP Host: localhost
- SMTP Port: 1025
"""


# ============================================================================
# COMMON PATTERNS
# ============================================================================

# Pattern 1: Multiple recipients
def test_email_to_multiple_recipients(email_helper, receiver_email):
    """Example of sending to multiple recipients"""
    recipients = [
        receiver_email,
        "admin@tutorialsninja.com",
        "support@tutorialsninja.com"
    ]
    
    for recipient in recipients:
        email_helper.send_email(
            sender="noreply@tutorialsninja.com",
            receiver=recipient,
            subject="System Notification",
            body="Important update"
        )
    
    # Verify all emails
    for recipient in recipients:
        assert email_helper.verify_email_received(recipient)


# Pattern 2: Email with specific content
def test_email_contains_specific_text(email_helper, receiver_email):
    """Verify email contains specific text"""
    content = "Your verification code is: 123456"
    
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject="Verification Code",
        body=content
    )
    
    # Verify content
    email = email_helper.find_email_by_receiver(receiver_email)
    assert "123456" in email['Content']['Body']
    assert "Verification" in email['Content']['Headers']['Subject'][0]


# Pattern 3: Using email templates
def test_with_all_templates(email_helper, receiver_email, email_templates):
    """Example using different email templates"""
    
    # Registration template
    reg_email = email_templates.registration_confirmation("token1")
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject=reg_email['subject'],
        body=reg_email['html'],
        html=True
    )
    
    # Password reset template
    reset_email = email_templates.password_reset("token2")
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject=reset_email['subject'],
        body=reset_email['html'],
        html=True
    )
    
    # Order confirmation template
    order_email = email_templates.order_confirmation("ORD-001", "99.99")
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject=order_email['subject'],
        body=order_email['html'],
        html=True
    )
    
    # Verify all 3 emails
    all_emails = email_helper.get_all_emails()
    assert len(all_emails) == 3


# ============================================================================
# DEBUGGING TIPS
# ============================================================================

"""
1. View all emails in MailHog:
   http://localhost:8025
   
2. Get all emails in test:
   all_emails = email_helper.get_all_emails()
   print(all_emails)
   
3. Get latest email:
   latest = email_helper.get_latest_email()
   
4. Find email by subject:
   email = email_helper.find_email_by_subject("Confirm Your Email")
   
5. Clear emails:
   email_helper.clear_all_emails()
   
6. Check email body:
   email = email_helper.find_email_by_receiver(receiver_email)
   body = email['Content']['Body']
   print(body)
"""
