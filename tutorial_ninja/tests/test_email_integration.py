"""
Integration tests for email functionality with Sathish Kumar's email
"""
import pytest
from Configurations.email_config import EmailConfig, EmailTemplates, RECEIVER_EMAIL, SENDER_EMAIL


pytestmark = pytest.mark.email  # Mark all tests in this file as email tests


class TestEmailIntegration:
    """Integration tests for email functionality"""
    
    def test_send_registration_confirmation(self, email_helper, receiver_email):
        """Test sending registration confirmation email"""
        token = "abc123def456"
        template = EmailTemplates.registration_confirmation(token)
        
        # Send email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject=template['subject'],
            body=template['html'],
            html=True
        )
        
        # Verify email was received
        assert email_helper.verify_email_received(receiver_email, "Confirm Your Email")
        
        # Verify email contains token
        email = email_helper.find_email_by_receiver(receiver_email)
        assert token in email['Content']['Body']
    
    def test_send_password_reset_email(self, email_helper, receiver_email):
        """Test sending password reset email"""
        reset_token = "reset_xyz789"
        template = EmailTemplates.password_reset(reset_token)
        
        # Send email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject=template['subject'],
            body=template['html'],
            html=True
        )
        
        # Verify
        assert email_helper.verify_email_received(receiver_email, "Password Reset")
        
        # Extract and verify reset link
        email = email_helper.find_email_by_receiver(receiver_email)
        assert "reset-password" in email['Content']['Body'].lower()
        assert reset_token in email['Content']['Body']
    
    def test_send_order_confirmation(self, email_helper, receiver_email):
        """Test sending order confirmation email"""
        order_id = "ORD-2026-001"
        total = "149.99"
        template = EmailTemplates.order_confirmation(order_id, total)
        
        # Send email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject=template['subject'],
            body=template['html'],
            html=True
        )
        
        # Verify
        assert email_helper.verify_email_received(receiver_email)
        
        # Verify order details
        email = email_helper.find_email_by_receiver(receiver_email)
        assert order_id in email['Content']['Body']
        assert total in email['Content']['Body']
    
    def test_send_newsletter_subscription(self, email_helper, receiver_email):
        """Test sending newsletter subscription email"""
        unsubscribe_link = "https://tutorialsninja.com/unsubscribe?token=xyz"
        template = EmailTemplates.newsletter_subscription(unsubscribe_link)
        
        # Send email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject=template['subject'],
            body=template['html'],
            html=True
        )
        
        # Verify
        assert email_helper.verify_email_received(receiver_email, "Newsletter")
        
        # Verify unsubscribe link
        email = email_helper.find_email_by_receiver(receiver_email)
        assert "unsubscribe" in email['Content']['Body'].lower()
    
    def test_verify_receiver_email_is_correct(self, receiver_email):
        """Verify that receiver email is set correctly"""
        assert receiver_email == RECEIVER_EMAIL
        assert receiver_email == "sathiskumark192@gmail.com"
    
    def test_verify_sender_email_is_correct(self, sender_email):
        """Verify that sender email is correct"""
        assert sender_email == SENDER_EMAIL
        assert sender_email == "noreply@tutorialsninja.com"


class TestEmailScenarios:
    """Real-world email testing scenarios"""
    
    def test_user_registration_flow_with_email(self, email_helper, receiver_email):
        """
        Simulate complete user registration flow with email verification
        
        Scenario:
        1. User registers on website
        2. Confirmation email is sent
        3. User clicks link in email
        4. Account is verified
        """
        # Step 1: Simulate registration (in real test, this would be Selenium)
        registration_token = "reg_token_12345"
        
        # Step 2: Send confirmation email
        template = EmailTemplates.registration_confirmation(registration_token)
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject=template['subject'],
            body=template['html'],
            html=True
        )
        
        # Step 3: Verify email in MailHog
        email = email_helper.find_email_by_receiver(receiver_email)
        assert email is not None
        
        # Step 4: Extract confirmation link
        body = email['Content']['Body']
        assert f"https://tutorialsninja.com/confirm?token={registration_token}" in body
        
        # In real scenario, user would click this link
        # For testing, we just verify it's there
        assert "Confirm Email" in body
    
    def test_password_reset_flow_with_email(self, email_helper, receiver_email):
        """
        Simulate password reset flow with email
        
        Scenario:
        1. User requests password reset
        2. Reset email is sent
        3. User clicks reset link
        """
        reset_token = "reset_token_67890"
        
        # Send reset email
        template = EmailTemplates.password_reset(reset_token)
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject=template['subject'],
            body=template['html'],
            html=True
        )
        
        # Verify reset email
        assert email_helper.verify_email_received(receiver_email)
        
        # Extract reset link
        email = email_helper.find_email_by_receiver(receiver_email)
        body = email['Content']['Body']
        assert f"token={reset_token}" in body
        assert "expires in 24 hours" in body.lower()
    
    def test_multiple_emails_to_same_recipient(self, email_helper, receiver_email):
        """Test sending multiple emails to the same recipient"""
        
        # Send first email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject="First Email",
            body="This is the first email"
        )
        
        # Send second email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject="Second Email",
            body="This is the second email"
        )
        
        # Send third email
        email_helper.send_email(
            sender=SENDER_EMAIL,
            receiver=receiver_email,
            subject="Third Email",
            body="This is the third email"
        )
        
        # Verify all emails are received
        all_emails = email_helper.get_all_emails()
        assert len(all_emails) == 3
        
        # Verify we can find each by subject
        assert email_helper.find_email_by_subject("First Email") is not None
        assert email_helper.find_email_by_subject("Second Email") is not None
        assert email_helper.find_email_by_subject("Third Email") is not None


class TestEmailConfiguration:
    """Test email configuration settings"""
    
    def test_current_environment(self):
        """Verify current environment configuration"""
        assert EmailConfig.ENV in ['docker', 'local', 'gmail', 'production']
        print(f"Running in {EmailConfig.ENV} environment")
    
    def test_smtp_configuration(self):
        """Verify SMTP configuration"""
        assert EmailConfig.SMTP_HOST is not None
        assert EmailConfig.SMTP_PORT > 0
        assert EmailConfig.FROM_EMAIL is not None
    
    def test_receiver_email_configuration(self):
        """Verify receiver email is properly configured"""
        assert RECEIVER_EMAIL == "sathiskumark192@gmail.com"
        assert "@gmail.com" in RECEIVER_EMAIL
    
    def test_email_templates_exist(self):
        """Verify all email templates exist"""
        templates = EmailTemplates
        
        assert hasattr(templates, 'registration_confirmation')
        assert hasattr(templates, 'password_reset')
        assert hasattr(templates, 'order_confirmation')
        assert hasattr(templates, 'newsletter_subscription')
    
    def test_email_template_content(self):
        """Verify email templates have required content"""
        # Test registration template
        reg_template = EmailTemplates.registration_confirmation("token123")
        assert 'subject' in reg_template
        assert 'html' in reg_template
        assert reg_template['subject'] != ""
        assert 'token123' in reg_template['html']
        
        # Test password reset template
        reset_template = EmailTemplates.password_reset("reset456")
        assert 'subject' in reset_template
        assert 'html' in reset_template
        assert 'reset456' in reset_template['html']
