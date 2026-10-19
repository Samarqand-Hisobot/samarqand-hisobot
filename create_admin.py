"""Create the first administrator safely from the terminal."""
from getpass import getpass
from app import app, db, User
from werkzeug.security import generate_password_hash
with app.app_context():
    username = input('Administrator login: ').strip()
    password = getpass('Administrator password (at least 8 characters): ')
    if not username or len(password) < 8:
        raise SystemExit('Login bo‘sh bo‘lmasin, parol kamida 8 belgidan iborat bo‘lsin.')
    if User.query.filter_by(username=username).first():
        raise SystemExit('Bu login allaqachon mavjud.')
    db.session.add(User(username=username, password_hash=generate_password_hash(password), role='admin'))
    db.session.commit()
    print('Administrator yaratildi. Endi python app.py buyrug‘i bilan dasturni ishga tushiring.')
