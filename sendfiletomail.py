import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime

# تنظیمات ایمیل
SMTP_HOST = "smtp.mailgun.org"        # یا smtp.gmail.com
SMTP_PORT = 587
SMTP_USERNAME = "postmaster@mg.inprobes.com"
SMTP_PASSWORD = "your_mailgun_s mtp_password"
SENDER_EMAIL = SMTP_USERNAME
RECEIVER_EMAIL = "hosein@inprobes.com"

# 1️⃣ ایجاد گزارش
report_content = f"""
گزارش سیستم - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

همه چیز خوبه :)
"""
report_filename = "report.txt"

with open(report_filename, "w", encoding="utf-8") as f:
    f.write(report_content)

# 2️⃣ ساخت ایمیل
msg = MIMEMultipart()
msg['Subject'] = "📊 گزارش روزانه سیستم"
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL

# متن ساده ایمیل
msg.attach(MIMEText("سلام حسین جان، گزارش پیوست شده رو ببین 🌟", "plain"))

# 3️⃣ اضافه کردن فایل پیوست
with open(report_filename, "rb") as f:
    part = MIMEApplication(f.read(), Name=report_filename)
    part['Content-Disposition'] = f'attachment; filename="{report_filename}"'
    msg.attach(part)

# 4️⃣ ارسال ایمیل
try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        print("✅ ایمیل با ضمیمه با موفقیت ارسال شد.")
except Exception as e:
    print("❌ خطا در ارسال ایمیل:", e)
