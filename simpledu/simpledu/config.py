class BaseConfig:
    SECRET_KEY = 'hello world'

class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqldb://root:aitak@localhost:3306/simpledu?charset=utf8')

class ProConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    pass

configs = {
    'dev': DevConfig,
    'pro': ProConfig,
    'test': TestConfig
}
