# -*- encoding: utf-8 -*-
from flask import request, redirect, session, render_template
from flask_login import login_user
from app.models.models import User
from app.utils import create_uuid
from app.models import db
from app.router.user import user_bp


@user_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect("/")
    else:
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        remember_me = request.form.get("remember-me", None)
        print(username, password, remember_me)
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password:
            login_user(user)
            if remember_me:
                uuid = create_uuid(username)
                user.uuid = uuid
                db.session.commit()
                session["login"] = uuid
                return redirect("/index")
            else:
                return redirect("/index")
        else:
            return redirect("/register")


@user_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        uuid = create_uuid(username)
        user = User(uuid=uuid, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect("/")

@user_bp.route("/index", methods=["get"])
def home():
    print("******write session to redis*******")
    session["a"] = "a"
    return "index"
