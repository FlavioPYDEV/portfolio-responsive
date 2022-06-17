from flask import Flask, render_template, redirect
from flask_mail import Mail, Message
from config import email,senha

app = Flask(__name__)
app.secret_key = 'juquinha'

mail_settings = {
    "MAIN_SERVER": 'smtp.gmail.com',
    "MAIL.PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSEL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSOWRD": senha
}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)