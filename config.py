# -*- encoding: utf-8 -*-

class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass


class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    #Mysql connection
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:steven@127.0.0.1:3306/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
