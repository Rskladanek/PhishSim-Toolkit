import smtplib
from email.mime.text import MIMEText


def send_fake_email(sender_email, recipient_email, sender_name, subject, body):
    msg = MIMEText(body)
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = recipient_email
    msg['Subject'] = subject

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  # SMTP credentials
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Message sent successfully.")


# Function call
send_fake_email(
    sender_email="bank@example.com",
    recipient_email="target@example.com",
    sender_name="Your Bank",
    subject="Urgent: Update Your Information",
    body="Click here to update your information: http://your-fake-site.com"
)
