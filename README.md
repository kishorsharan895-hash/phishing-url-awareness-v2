# Phishing URL Awareness Checker

## About
Phishing URL Awareness Checker is a beginner-friendly Python cybersecurity project that identifies common warning signs in URLs.

## Features
- Checks for unusually long URLs.
- Detects the `@` symbol in URLs.
- Identifies IP addresses used as hostnames.
- Checks for multiple subdomains.
- Detects suspicious keywords such as login, verify, and password.
- Warns when a URL uses HTTP instead of HTTPS.
- Displays warning signs in the terminal.

## Technologies Used
- Python 3
- `urllib.parse`
- `ipaddress`
- `re` (Regular Expressions)

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project in Visual Studio Code.
4. Open `phishing_checker.py`.
5. Run the Python file.
6. Enter a URL when prompted.

## Sample URL
`http://example.com/login`

## Disclaimer
This is an educational project. It checks URL text for common warning signs and cannot guarantee whether a website is safe or malicious. Do not enter passwords or other sensitive information on suspicious websites.

## Author
Kishor Kumar
