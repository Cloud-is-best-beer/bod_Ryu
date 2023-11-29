import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
#                             os.path.join(BASE_DIR, 'bod.db'))

# {0}=db user / {1}=db password
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@localhost:3306/bod?charset=utf8'.format('root','1234')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session사용에 필요한 비밀키
SECRET_KEY = "my_key"
