import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'bod.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session사용에 필요한 비밀키
SECRET_KEY = "key123"
