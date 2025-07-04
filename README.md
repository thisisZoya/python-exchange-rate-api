# 📈 Python Exchange Report Automation

This project is a simple yet powerful automation system for generating reports, sending them via email and SMS (using Twilio), and running periodically via `cron`.

---

## 🧰 Project Structure

```
exchange/
├── main.py                # Main entry point
├── config.py              # Configuration for email, Twilio, and file paths
├── mail.py                # Sends emails with report attachments
├── notification.py        # Sends SMS using Twilio
├── report_sender.py       # Generates reports and triggers sending
├── requirement            # Project dependencies (requests, twilio)
└── README.md              # Documentation
```

---

## 🚀 How It Works

1. `main.py` is executed manually or by a cron job.
2. `report_sender.py` creates a text-based report (e.g., exchange rate, finance, or logs).
3. `mail.py` sends the report as an email attachment.
4. `notification.py` sends an SMS notification using Twilio.
5. The execution log is written to a file.

---

## ⚙️ Configuration (`config.py`)

```python
# Email
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
RECEIVER_EMAIL = 'receiver@example.com'

# SMS (Twilio)
TWILIO_ACCOUNT_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_FROM_NUMBER = '+1234567890'
TO_PHONE_NUMBER = '+19876543210'

# Report path
REPORT_FILE_PATH = 'report.txt'
```

---

## 📧 Email Sending

Uses Python's `smtplib` and `email` libraries to send reports via email with attachments. Credentials and recipient settings are in `config.py`.

---

## 📱 SMS Notifications with Twilio

`notification.py` uses the official Twilio SDK to send SMS alerts like "Report sent".

Example usage:
```python
from notification import send_sms
send_sms("📢 New report has been sent.")
```

---

## ⏱ Cron Job Setup

To run the script every 2 minutes:

```cron
*/2 * * * * /Users/hussain/Projects/exchange/venv/bin/python /Users/hussain/Projects/exchange/exchange/main.py >> /Users/hussain/cron.log 2>&1
```

To edit your crontab:
```bash
crontab -e
```

Output logs are stored in `cron.log`.

---

## 🛠 Install Dependencies

```bash
pip install -r requirement
```

Content of `requirement`:

```
requests
twilio
```

---

## ✅ Quick Test

Run the script manually to test:

```bash
python main.py
```

If everything is configured properly, it will:
- generate a report
- send it via email
- send an SMS notification

---

## 💡 Future Improvements

- Fetch real-time exchange rates from APIs (e.g., exchangeratesapi.io)
- Send alerts to Telegram
- Save reports to a database
- Add a dashboard with Flask or Streamlit
- Convert to a REST API

---

## 👨‍💻 Developer

Project by [Hossein Mousavi](https://github.com/hu3ein)  
Feel free to collaborate, suggest improvements, or fork this repository.