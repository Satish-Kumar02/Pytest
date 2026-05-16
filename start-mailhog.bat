@echo off
REM Start MailHog for email testing
REM This script starts MailHog in Docker

echo Starting MailHog for email testing...
echo.
echo MailHog will be available at:
echo   - SMTP: localhost:1025
echo   - Web UI: http://localhost:8025
echo.
echo Press Ctrl+C to stop MailHog
echo.

docker run -p 1025:1025 -p 8025:8025 mailhog/mailhog:latest

pause
