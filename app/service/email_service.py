import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings


async def send_email(email: str, subject: str, body: str):
    try:
        # Create message
        message = MIMEMultipart()
        message["From"] = settings.SENDER_EMAIL
        message["To"] = email
        message["Subject"] = subject

        # Add body to email (strip leading whitespace from multiline strings)
        message.attach(MIMEText(body.strip(), "plain"))

        # Create SSL context
        context = ssl.create_default_context()

        # Send email
        with smtplib.SMTP_SSL(
            settings.SMTP_SERVER, settings.SMTP_PORT, context=context
        ) as server:
            server.login(settings.SENDER_EMAIL, settings.SENDER_PASSWORD)
            server.send_message(message)

        return {"message": "Email sent!"}
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and App Password.")
    except Exception as e:
        print(f"An error occurred: {e}")
