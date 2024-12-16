
# Phishing Simulation Project

## Overview
This project is **a work in progress** and aims to simulate phishing attacks for **ethical and educational purposes only**. The key components include a fake website resembling a legitimate login page and a Python script for sending spoofed emails. This project can be used for testing security awareness in controlled environments.

---

## Project Structure
The project is organized as follows:
```
project/
│
├── modules/
│   ├── app.py           # Main Flask application for serving the phishing page
│   ├── send_email.py    # Script for sending spoofed emails
│
├── templates/
│   ├── index.html       # Fake login page template
│   ├── facebook.svg     # Facebook-like logo
│
├── main.py              # Entry point for running the project
├── logins.txt           # File for storing captured credentials (for testing purposes only)
├── README.md            # Project documentation
├── requirements.txt     # requirements for the project
└── .gitignore           # Ignored files
```

---

## Fake Login Page Preview
Below is an image preview of the current `index.html`, which mimics the Facebook login page for testing:

![Fake Facebook Login](image.png)

The login page collects entered credentials for **testing only**.

---

## Goals

### 1. Develop a Fake Phishing Website
- Clone the appearance of a legitimate login page.
- Capture and log credentials entered into the form.
- Serve the page locally using Flask.

### 2. Implement Email Spoofing Script
- Send emails that appear to originate from trusted sources.
- Use Python's `smtplib` library to send spoofed messages.
- Include HTML body with phishing links.

### 3. Create an Ethical Framework
- Clearly outline **legal boundaries** and **ethical considerations**.
- Ensure written consent from targets before testing.
- Provide disclaimers in both project files and documentation.

---

## Installation and Setup

### Prerequisites
- Python 3.x installed
- Flask
- SMTP server (local or external)
- Ngrok (for exposing local servers to the internet)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/phishing-simulation.git
   cd phishing-simulation
   ```

2. **Install Required Libraries**
   ```bash
   pip -r requirements.txt
   ```

3. **Run the Fake Website**
   ```bash
   python3 modules/app.py
   ```
   The website will be served locally at `http://127.0.0.1:5000`.


4. **Send Test Emails**
   NOT WORKING YET

5. **Test the Workflow**
   - Use Ngrok to expose your Flask server online.
   - Test the fake login page and email delivery.

---

## Legal and Ethical Considerations
**Warning:** This project is for **educational and ethical security testing** purposes only. Unauthorized usage is strictly prohibited.

- **Consent:** Obtain explicit written consent before performing any tests.
- **Legality:** Ensure all actions comply with local and international laws.
- **Usage:** The project is intended to raise awareness about phishing threats.

---

## Status
- ✅ Project structure and setup defined.
- ✅ Basic phishing page implemented.
- ✅ Email spoofing script functional.
- 🔧 Further testing and refinement ongoing.

---

## Preview
**Index.html** (Fake Facebook Login):
- Serves as the fake phishing page.

### Screenshot
![Phishing Login Page](obraz.png)

---

## Next Steps
1. Improve the fake login page's responsiveness and UI accuracy.
2. Add logging mechanisms to store captured credentials securely.
3. Refine the email spoofing script with additional customization.

---

## Contributing
Feel free to submit pull requests or report issues to enhance the project.

---

### Disclaimer
This project should **never be used for malicious purposes**. Always prioritize ethical considerations and legal compliance when using or testing this tool.
