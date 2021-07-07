from hashlib import sha512
from db_manager import DBManager


class Authenticator():
    def __init__(self, privkey_path='./priv.key'):
        with open(privkey_path, 'r') as f:
            self.privkey = f.read()
        self.manager = DBManager()

    def create_token(self, username):
        return sha512((username + self.privkey).encode()).hexdigest()

    def authenticate_token(self, username, token):
        return token == sha512((username + self.privkey).encode()).hexdigest()

    def process_login_request(self, request):
        headers = request.headers
        username = headers.get('Username')
        password = headers.get('Password')
        token = headers.get('Token')
        if token is not None and username is not None:
            if self.authenticate_token(username, token):
                return 'auth success'
            return 'auth failed'
        elif username is not None and password is not None:
            success = self.manager.check_password(username, password)
            if success:
                return self.create_token(username)
            return 'auth failed'

        return "error"