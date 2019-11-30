# -*- encoding: utf-8 -*-
import os
import redis

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base config class."""
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'yon do not know who i am'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SUBJECT_PREFIX = '[Steven]'
    MAIL_SENDER = 'Steven Admin <steven@qq.com>'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Development config class."""
    DEBUG = True
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'steven'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'steven'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL_MYSQL') or \
                              'mysql+pymysql://root:steven@localhost:3306/flask?charset=utf8mb4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = False
    #SESSION_KEY_PERFIX = 'session:'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379,db=0)


class TestingConfig(Config):
    """Testing config class."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
                              'sqlite:///' + os.path.join(base_dir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
                              'sqlite:///' + os.path.join(base_dir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
