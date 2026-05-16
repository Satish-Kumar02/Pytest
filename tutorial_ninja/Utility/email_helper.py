import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailHelper:
    """Helper class for sending and verifying emails using MailHog"""
    
    def __init__(self, smtp_host="mailhog", smtp_port=1025, mailhog_api_url="http://mailhog:8025/api/v1/messages"):
        """
        Initialize EmailHelper with SMTP and MailHog API configuration
        
        Args:
            smtp_host (str): SMTP server host (default: mailhog for Docker)
            smtp_port (int): SMTP server port (default: 1025)
            mailhog_api_url (str): MailHog API endpoint for retrieving emails
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.mailhog_api_url = mailhog_api_url
    
    def send_email(self, sender, receiver, subject, body, html=False):
        """
        Send email through MailHog SMTP server
        
        Args:
            sender (str): Sender email address
            receiver (str): Recipient email address
            subject (str): Email subject
            body (str): Email body content
            html (bool): Whether body is HTML (default: False)
        
        Returns:
            bool: True if email sent successfully
        
        Raises:
            Exception: If email sending fails
        """
        try:
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = subject
            
            # Attach body as HTML or plain text
            content_type = 'html' if html else 'plain'
            message.attach(MIMEText(body, content_type))
            
            server.send_message(message)
            server.quit()
            
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            raise
    
    def get_all_emails(self):
        """
        Retrieve all emails from MailHog API
        
        Returns:
            list: List of email objects
        """
        try:
            response = requests.get(self.mailhog_api_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error retrieving emails: {str(e)}")
            return []
    
    def get_latest_email(self):
        """
        Get the most recent email from MailHog
        
        Returns:
            dict: Latest email object or None
        """
        emails = self.get_all_emails()
        return emails[0] if emails else None
    
    def find_email_by_receiver(self, receiver):
        """
        Find email by receiver address
        
        Args:
            receiver (str): Recipient email address
        
        Returns:
            dict: Email object or None
        """
        emails = self.get_all_emails()
        for email in emails:
            if email['To'] and any(addr['Address'] == receiver for addr in email['To']):
                return email
        return None
    
    def find_email_by_subject(self, subject):
        """
        Find email by subject line
        
        Args:
            subject (str): Email subject to search for
        
        Returns:
            dict: Email object or None
        """
        emails = self.get_all_emails()
        for email in emails:
            if email['Content']['Headers']['Subject'] and subject in email['Content']['Headers']['Subject'][0]:
                return email
        return None
    
    def clear_all_emails(self):
        """
        Delete all emails from MailHog
        
        Returns:
            bool: True if successful
        """
        try:
            response = requests.delete(self.mailhog_api_url)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error clearing emails: {str(e)}")
            return False
    
    def verify_email_received(self, receiver, subject=None):
        """
        Verify that an email was received by a specific recipient
        
        Args:
            receiver (str): Recipient email address
            subject (str): Optional subject to verify
        
        Returns:
            bool: True if email found
        """
        email = self.find_email_by_receiver(receiver)
        if email is None:
            return False
        
        if subject:
            email_subject = email['Content']['Headers'].get('Subject', [''])[0]
            return subject in email_subject
        
        return True
