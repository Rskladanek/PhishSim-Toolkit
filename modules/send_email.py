import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
it's more complicated than u can imagine
"""

def send_fake_email(sender_email, recipient_email, sender_name, subject, body_html, smtp_host='localhost', smtp_port=25):
    msg = MIMEMultipart("alternative")
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body_html, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            # Debugging SMTP
            server.set_debuglevel(1)
            server.send_message(msg)
            print("Message sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    send_fake_email(
        sender_email="reply@movaq.jethrough.com",
        recipient_email="remek.skladanek@wp.pl",
        sender_name="Support Team",
        subject="Verify Your Account",
        body_html="<p>Click here to verify: <a href='http://fake-link.com'>Verify</a></p>"
    )
