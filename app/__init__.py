# -*- encoding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from config import config

mail = Mail()
moment = Moment()


def create_app(config_name):
    from . import models, router
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    models.init_app(app)
    router.init_app(app)

    return app
