# -*- encoding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from .base import db


class User(UserMixin, db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(256), nullable=False)
    username = db.Column(db.String(256), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

#加载用户回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
