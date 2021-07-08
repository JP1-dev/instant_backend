from flask import Flask, request
import authentication
import requests


app = Flask(__name__)

auth = authentication.Authenticator()


@app.route('/login', methods=['GET', 'POST'])
def login():
    rsp = auth.process_login_request(request)
    return rsp


@app.route('/register', methods=['GET','POST'])
def register():
    status = requests.post('http://localhost:8555', data=request.data)
    return 'ok'


@app.route('/')
def index():
    return "up and running:)"

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=8080)

