class BaseConfig:
    SECRET_KEY = 'HELLO WORLD'

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:aitak@localhost/test?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    'dev': DevelopmentConfig
}
