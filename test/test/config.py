class BaseConfig:
    SECRET_KEY = 'HELLO WORLD'
    INDEX_PER_PAGE = 6
    ADMIN_PER_PAGE = 10

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:aitak@localhost/test?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    'dev': DevelopmentConfig
}
