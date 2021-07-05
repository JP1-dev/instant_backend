import psycopg2
from hashlib import sha256


def connect():
    conn = psycopg2.connect(
        host = 'localhost',
        port = 5432,
        database = 'instant',
        user = 'postgres',
        password = 'pw'
    )

def process_login_request(request):
    print(request.method)
    return "ok"