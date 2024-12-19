from modules.app import app
from modules.send_email import send_fake_email


def main():
    """Main function to run the phishing simulation."""
    print("Phishing Simulation Project")
    print("----------------------------")

    # Start the Flask server
    print("[1] Starting phishing server...")
    app.run(host="0.0.0.0", port=5000, debug=True)

    # Optionally send a test email
    print("\n[2] Sending a test email (test environment)...")
    send_fake_email(
        sender_email="no-reply@paypal.com",
        recipient_email="test@localdomain",
        sender_name="Paypal Security",
        subject="Important Security Notice",
        body_html="<p>Please verify your account details.</p>"
    )


if __name__ == "__main__":
    main()