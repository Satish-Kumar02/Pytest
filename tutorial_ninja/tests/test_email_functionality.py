import pytest
from Utility.email_helper import EmailHelper


pytestmark = pytest.mark.email  # Mark all tests in this file as email tests


class TestEmailFunctionality:
    """Test email functionality using MailHog"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup email helper and clear emails before each test"""
        self.email_helper = EmailHelper()
        # Clear emails before test
        self.email_helper.clear_all_emails()
        yield
        # Cleanup after test
        self.email_helper.clear_all_emails()
    
    def test_send_simple_email(self):
        """Test sending a simple email"""
        sender = "noreply@tutorialsninja.com"
        receiver = "sathiskumark192@gmail.com"
        subject = "Test Email"
        body = "This is a test email"
        
        # Send email
        result = self.email_helper.send_email(sender, receiver, subject, body)
        assert result is True
        
        # Verify email was received
        assert self.email_helper.verify_email_received(receiver) is True
    
    def test_send_html_email(self):
        """Test sending an HTML email"""
        sender = "noreply@tutorialsninja.com"
        receiver = "sathiskumark192@gmail.com"
        subject = "Welcome Email"
        body = "<html><body><h1>Welcome!</h1><p>Thank you for registering.</p></body></html>"
        
        # Send HTML email
        result = self.email_helper.send_email(sender, receiver, subject, body, html=True)
        assert result is True
        
        # Verify email
        assert self.email_helper.verify_email_received(receiver, subject) is True
    
    def test_find_email_by_receiver(self):
        """Test finding email by receiver address"""
        sender = "noreply@tutorialsninja.com"
        receiver = "sathiskumark192@gmail.com"
        subject = "Account Confirmation"
        body = "Please confirm your account"
        
        # Send email
        self.email_helper.send_email(sender, receiver, subject, body)
        
        # Find email by receiver
        email = self.email_helper.find_email_by_receiver(receiver)
        assert email is not None
        assert any(addr['Address'] == receiver for addr in email['To'])
    
    def test_find_email_by_subject(self):
        """Test finding email by subject"""
        sender = "noreply@tutorialsninja.com"
        receiver = "sathiskumark192@gmail.com"
        subject = "Password Reset"
        body = "Click here to reset your password"
        
        # Send email
        self.email_helper.send_email(sender, receiver, subject, body)
        
        # Find email by subject
        email = self.email_helper.find_email_by_subject("Password Reset")
        assert email is not None
    
    def test_get_latest_email(self):
        """Test retrieving the latest email"""
        sender = "noreply@tutorialsninja.com"
        receiver = "user@example.com"
        subject = "Latest Test"
        body = "This is the latest email"
        
        # Send email
        self.email_helper.send_email(sender, receiver, subject, body)
        
        # Get latest email
        latest_email = self.email_helper.get_latest_email()
        assert latest_email is not None
        assert any(addr['Address'] == receiver for addr in latest_email['To'])
    
    def test_get_all_emails(self):
        """Test retrieving all emails"""
        # Send multiple emails
        for i in range(3):
            self.email_helper.send_email(
                f"sender{i}@example.com",
                f"receiver{i}@example.com",
                f"Subject {i}",
                f"Body {i}"
            )
        
        # Get all emails
        emails = self.email_helper.get_all_emails()
        assert len(emails) == 3
    
    def test_clear_emails(self):
        """Test clearing all emails"""
        # Send an email
        self.email_helper.send_email(
            "sender@example.com",
            "receiver@example.com",
            "Test",
            "Body"
        )
        
        # Verify email exists
        assert len(self.email_helper.get_all_emails()) == 1
        
        # Clear emails
        result = self.email_helper.clear_all_emails()
        assert result is True
        
        # Verify emails are cleared
        assert len(self.email_helper.get_all_emails()) == 0


class TestEmailInRegistrationFlow:
    """Example: Test email in user registration flow"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup email helper"""
        self.email_helper = EmailHelper()
        self.email_helper.clear_all_emails()
        yield
        self.email_helper.clear_all_emails()
    
    def test_user_registration_sends_confirmation_email(self):
        """
        Test that user registration sends a confirmation email
        
        In a real scenario, this would:
        1. Register a new user on the website
        2. Verify confirmation email is sent
        3. Extract confirmation link
        4. Click link to verify account
        """
        user_email = "newuser@example.com"
        
        # Simulate registration email being sent
        self.email_helper.send_email(
            sender="noreply@tutorialsninja.com",
            receiver=user_email,
            subject="Email Confirmation Required",
            body="Click here to confirm your email: https://tutorialsninja.com/confirm?token=abc123"
        )
        
        # Assert confirmation email was received
        assert self.email_helper.verify_email_received(user_email, "Email Confirmation") is True
        
        # Find email and verify content
        email = self.email_helper.find_email_by_receiver(user_email)
        assert email is not None
        assert "confirm" in email['Content']['Body'].lower()
