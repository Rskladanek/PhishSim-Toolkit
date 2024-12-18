from modules.app import app
from modules.send_email import send_fake_email

def main():
    print("Phishing Simulation Project")
    print("----------------------------")

    # Uruchomienie serwera Flask
    print("[1] Uruchamianie serwera phishingowego...")
    app.run(host="0.0.0.0", port=5000, debug=True)

    # Opcjonalne wysłanie testowego maila
    print("\n[2] Wysyłanie testowego maila (testowe środowisko)...")
    send_fake_email(
        sender_email="no-reply@paypal.com",
        recipient_email="test@localdomain",
        sender_name="Paypal Security",
        subject="Important Security Notice",
        body_html="<p>Please verify your account details.</p>"
    )

if __name__ == "__main__":
    main()
