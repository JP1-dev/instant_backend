from flask import Flask, request
import authentication

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    rsp = authentication.process_login_request(request)
    return rsp

@app.route('/')
def index():
    return "up and running:)"

