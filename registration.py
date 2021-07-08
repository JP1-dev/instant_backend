from db_manager import DBManager
from flask import Flask, url_for, request
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def mail(email):
    sender_email = ''
    sender_password = ''
    mail_subject = "Confirmation"
    mail_content = "Here is the confirmationslink for Instant"

    message = MIMEMultipart()
    message['From'] = "Instant"
    message['To'] = email
    message['Subject'] = mail_subject
    message.attach(MIMEText(mail_content, 'plain'))
    whole_message = message.as_string()

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_email, sender_password)
    text = message.as_string()
    session.sendmail(sender_email, email, whole_message)
    session.quit()


def generate_id():
    return ''.join(random.choice(string.digits + string.ascii_letters) for i in range(142))


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def receive():
    data = json.loads(request.data.decode())
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    gender = data.get('gender')
    tel = data.get('tel')
    return 'ok'


@app.route('/<id>')
def confirm(id):
    return id


if __name__ == '__main__':
    app.run(host='localhost',port=8555,debug=True)

