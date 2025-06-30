# import smtplib
# import requests
import smtplib
from email.mime.text import MIMEText
from config import EMAIL_RECEIVER

# from config import EMAIL_RECEIVER
# from local_config import MAILGUN_APIKEY

# from email.mime.text import MIMEText

# import smtplib
# from email.mime.text import MIMEText
# from config import EMAIL_RECEIVER

# SMTP_HOST = "sandbox.email.org"
# SMTP_PORT = 587
# SMTP_USERNAME = "your_username"
# SMTP_PASSWORD = "YOUR_PASWORD"

# def send_smtp_email(subject, body):
#     msg = MIMEText(body)
#     msg["subjecr"] = subject
#     msg["from"] = "PRIVATE_PERSON"
#     msg["to"] = EMAIL_RECEIVER
#     try:
#         with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
#             server.starttls()
#             server.login(SMTP_USERNAME, SMTP_PASSWORD)
#             server.sendmail(msg["from"], msg["to"], msg.as_string())
#             print("send mail.")
#     except Exception as e:
#         print(e)


# def send_api_email(subject, body):
#     return requests.post(
#         "https://api.mailgun.net/v3/inprobes/messages",
#         auth=("api", MAILGUN_APIKEY),
#         data={
#             "from": "Hosein finance@inprobes.com",
#             "to": ["hs.ramezanpoor@gmail.com", "hosein@inprobes.com"],
#             "subject": subject,
#             "text": body
#         }
#     )


# def send_smtp_email(subject, body):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = "finance@inprobes.com"
#     msg['To'] = EMAIL_RECEIVER

#     with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
#         mail_server.login('postmaster@mg.inprobes.com', MAILGUN_APIKEY)
#         mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
#         # mail_server.quit()


# information of Mailtrap
MAILTRAP_HOST = "sandbox.smtp.mailtrap.io"
MAILTRAP_PORT = 2525
MAILTRAP_USERNAME = "de5a82e8de1420"
MAILTRAP_PASSWORD = "ab364d24d6e6d0"

def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "Private Person <from@example.com>"
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
        server.starttls()
        server.login(MAILTRAP_USERNAME, MAILTRAP_PASSWORD)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

