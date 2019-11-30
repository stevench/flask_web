# -*- encoding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager
from flask_session import Session
from config import config

mail = Mail()
moment = Moment()
sess = Session()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'author.login'


def create_app(config_name):
    from . import api, echarts, models, router
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)
    api.init_app(app)
    echarts.init_app(app)
    models.init_app(app)
    router.init_app(app)

    return app
