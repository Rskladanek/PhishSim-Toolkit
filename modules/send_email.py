import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_fake_email(sender_email, recipient_email, sender_name, subject, body_html,
                    smtp_host='localhost', smtp_port=1025):
    """Send a fake email in a test environment (no real delivery)."""
    msg = MIMEMultipart("alternative")
    # "false" sender is established
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body_html, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.set_debuglevel(1)
            server.send_message(msg)
            print("Message sent successfully (in a test environment).")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # python3 -m smtpd -c DebuggingServer -n localhost:1025
    send_fake_email(
        sender_email="no-reply@paypal.com",
        recipient_email="test@localdomain",
        sender_name="Paypal Security",
        subject="Important Security Notice",
        body_html="<p>Please verify your account details.</p>"
    )
