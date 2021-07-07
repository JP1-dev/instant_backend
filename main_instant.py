from flask import Flask, request
import authentication

app = Flask(__name__)

auth = authentication.Authenticator()

@app.route('/login', methods=['GET', 'POST'])
def login():
    rsp = auth.process_login_request(request)
    return rsp

@app.route('/')
def index():
    return "up and running:)"

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=8080)

