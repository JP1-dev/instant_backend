from flask import Flask, request
import authentication

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    rsp = authentication.process_login_request(request)
    return rsp


if __name__ == '__main__':
    app.run(host='localhost',port=4200,debug=True)