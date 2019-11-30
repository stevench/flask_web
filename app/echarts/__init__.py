# -*- encoding: utf-8 -*-
from flask import Blueprint

echarts_bp = Blueprint('echarts', __name__)

from . import base

def init_app(app):
    app.register_blueprint(echarts_bp)
