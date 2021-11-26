class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    UPLOAD_FOLDER = 'static/images/'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    FLASK_SECRET = SECRET_KEY
    MONGO_URI=''

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DB_HOST = '' # not a docker link