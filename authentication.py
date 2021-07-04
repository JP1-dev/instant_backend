import psycopg2
from hashlib import sha256


def process_login_request(request):
    print(request.method)
    return "ok"