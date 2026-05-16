"""
Email Configuration for different environments
"""
import os


class EmailConfig:
    """
    Email configuration for development, testing, and production environments
    """
    
    ENV = os.getenv('ENVIRONMENT', 'local')
    
    # Default receiver email for testing
    RECEIVER_EMAIL = "sathiskumark192@gmail.com"
    
    if ENV == 'docker':
        # Docker + MailHog Configuration
        SMTP_HOST = "mailhog"
        SMTP_PORT = 1025
        FROM_EMAIL = "noreply@tutorialsninja.com"
        API_URL = "http://mailhog:8025/api/v1/messages"
        USE_TLS = False
        USE_SSL = False
    
    elif ENV == 'local':
        # Local Development + MailHog
        SMTP_HOST = "localhost"
        SMTP_PORT = 1025
        FROM_EMAIL = "noreply@tutorialsninja.com"
        API_URL = "http://localhost:8025/api/v1/messages"
        USE_TLS = False
        USE_SSL = False
    
    elif ENV == 'gmail':
        # Gmail Configuration (for real email testing)
        SMTP_HOST = "smtp.gmail.com"
        SMTP_PORT = 587
        FROM_EMAIL = os.getenv('GMAIL_USER', 'your-email@gmail.com')
        GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD', 'your-app-password')
        API_URL = None  # Gmail doesn't have API for this
        USE_TLS = True
        USE_SSL = False
    
    else:  # production
        # Production SMTP Server
        SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.example.com')
        SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
        FROM_EMAIL = os.getenv('FROM_EMAIL', 'noreply@tutorialsninja.com')
        API_URL = None
        USE_TLS = True
        USE_SSL = False


# Email templates
class EmailTemplates:
    """Email templates for different scenarios"""
    
    @staticmethod
    def registration_confirmation(token):
        """User registration confirmation email"""
        return {
            'subject': 'Confirm Your Email - TutorialsNinja',
            'html': f"""
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h1>Welcome to TutorialsNinja!</h1>
                <p>Thank you for registering.</p>
                <p>Please confirm your email by clicking the link below:</p>
                <a href="https://tutorialsninja.com/confirm?token={token}" 
                   style="background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    Confirm Email
                </a>
                <p>Or copy and paste this link:</p>
                <p>https://tutorialsninja.com/confirm?token={token}</p>
                <hr>
                <p>If you didn't create this account, please ignore this email.</p>
            </body>
            </html>
            """
        }
    
    @staticmethod
    def password_reset(token):
        """Password reset email"""
        return {
            'subject': 'Reset Your Password - TutorialsNinja',
            'html': f"""
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h1>Password Reset Request</h1>
                <p>We received a request to reset your password.</p>
                <p>Click the link below to reset your password:</p>
                <a href="https://tutorialsninja.com/reset-password?token={token}" 
                   style="background-color: #dc3545; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    Reset Password
                </a>
                <p>This link expires in 24 hours.</p>
                <hr>
                <p>If you didn't request this, please ignore this email.</p>
            </body>
            </html>
            """
        }
    
    @staticmethod
    def order_confirmation(order_id, total):
        """Order confirmation email"""
        return {
            'subject': f'Order Confirmation #{order_id} - TutorialsNinja',
            'html': f"""
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h1>Order Confirmed!</h1>
                <p>Thank you for your purchase.</p>
                <p><strong>Order ID:</strong> {order_id}</p>
                <p><strong>Total:</strong> ${total}</p>
                <p>You can track your order in your account dashboard.</p>
                <a href="https://tutorialsninja.com/orders" 
                   style="background-color: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    View Order
                </a>
                <hr>
                <p>Thank you for shopping with us!</p>
            </body>
            </html>
            """
        }
    
    @staticmethod
    def newsletter_subscription(unsubscribe_link):
        """Newsletter subscription confirmation"""
        return {
            'subject': 'Welcome to TutorialsNinja Newsletter',
            'html': f"""
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h1>Newsletter Subscription Confirmed!</h1>
                <p>You've successfully subscribed to our newsletter.</p>
                <p>You'll now receive the latest tutorials, updates, and exclusive content.</p>
                <hr>
                <p>
                    <a href="{unsubscribe_link}">Unsubscribe</a> | 
                    <a href="https://tutorialsninja.com/settings">Update Preferences</a>
                </p>
            </body>
            </html>
            """
        }


# Quick reference
RECEIVER_EMAIL = EmailConfig.RECEIVER_EMAIL
SENDER_EMAIL = EmailConfig.FROM_EMAIL
