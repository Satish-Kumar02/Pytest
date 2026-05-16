# How to Run MailHog for Email Testing

## Option 1: Docker (Recommended for Tests)

### Start MailHog with Docker Compose
This is the easiest method - MailHog runs alongside your tests:

```bash
cd Pytest
docker-compose up
```

MailHog Web UI will be available at: **http://localhost:8025**

### Or Start Just MailHog (if you only want to test emails)

```bash
docker run -p 1025:1025 -p 8025:8025 mailhog/mailhog:latest
```

Then run your tests:
```bash
pytest tests/ -v -m email
```

## Option 2: Install MailHog Locally (Windows)

### Using Chocolatey
If you have Chocolatey installed:
```bash
choco install mailhog
```

### Using scoop
```bash
scoop install mailhog
```

### Manual Download
1. Download from: https://github.com/mailhog/MailHog/releases
2. Extract the .exe file
3. Run: `MailHog.exe`

MailHog will automatically start on:
- SMTP: localhost:1025
- Web UI: http://localhost:8025

## Option 3: Using Go (If you have Go installed)

```bash
go install github.com/mailhog/MailHog@latest
~/go/bin/MailHog
```

## Running Tests with MailHog

### Run all email tests (if MailHog is running)
```bash
pytest tests/ -v -m email
```

### Run specific email test
```bash
pytest tests/test_email_integration.py::TestEmailIntegration::test_send_registration_confirmation -v
```

### Skip email tests (if MailHog is not running)
```bash
pytest tests/ -v -m "not email"
```

## Configuration

The email tests automatically detect your environment:
- **Docker**: Uses `mailhog:1025` (inside Docker containers)
- **Local**: Uses `localhost:1025` (on your machine)

To override, set the environment variable:
```bash
# Force Docker mode
set ENVIRONMENT=docker

# Force local mode  
set ENVIRONMENT=local

# Run tests
pytest tests/ -v -m email
```

## Troubleshooting

### Error: "Failed to resolve 'mailhog'"
This means MailHog is not running. Start it:
```bash
docker run -p 1025:1025 -p 8025:8025 mailhog/mailhog:latest
```

### Error: "Connection refused on localhost:1025"
MailHog is not running on your machine. Either:
1. Start MailHog locally: `MailHog.exe` or `mailhog`
2. Or use Docker: `docker run -p 1025:1025 -p 8025:8025 mailhog/mailhog:latest`
3. Or skip email tests: `pytest -m "not email"`

### Can't access Web UI at localhost:8025
- Make sure MailHog is running
- Check your firewall settings
- Try accessing from: http://127.0.0.1:8025

## Email Test Examples

### Basic Usage in Your Tests

```python
def test_send_email(email_helper, receiver_email):
    """Test sending email to sathiskumark192@gmail.com"""
    email_helper.send_email(
        sender="noreply@tutorialsninja.com",
        receiver=receiver_email,
        subject="Welcome",
        body="Hello User!"
    )
    
    # Verify email was sent to MailHog
    assert email_helper.verify_email_received(receiver_email)
```

### View Emails in MailHog
1. Open http://localhost:8025
2. All sent emails appear in the inbox
3. Click an email to see full details (headers, body, attachments)

## Notes

- MailHog is for **testing only** - emails do NOT go to real addresses
- All emails are captured and stored in memory (lost on restart)
- Perfect for development and CI/CD pipelines
- Receiver email configured to: **sathiskumark192@gmail.com**

## Quick Commands

```bash
# Start MailHog in Docker
docker run -p 1025:1025 -p 8025:8025 mailhog/mailhog:latest

# Run tests with docker-compose
cd Pytest && docker-compose up

# Run only email tests
pytest -v -m email

# Run tests without email tests
pytest -v -m "not email"

# View MailHog Web UI
# http://localhost:8025
```
