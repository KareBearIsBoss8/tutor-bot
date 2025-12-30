# email_utils.py
import os
import requests

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")          # verified sender in SendGrid
EMAIL_TO = "karolenazhou@gmail.com"           # fixed recipient

def send_question_email(question: str) -> None:
    if not (SENDGRID_API_KEY and EMAIL_FROM):
        return  # silently skip if not configured

    payload = {
        "personalizations": [{"to": [{"email": EMAIL_TO}]}],
        "from": {"email": EMAIL_FROM},
        "subject": "New question submitted",
        "content": [{"type": "text/plain", "value": question}],
    }
    headers = {
        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content-Type": "application/json",
    }

    r = requests.post("https://api.sendgrid.com/v3/mail/send", json=payload, headers=headers, timeout=15)
    r.raise_for_status()
